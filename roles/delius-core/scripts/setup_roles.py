from java.lang import System
import os


def initConfigToScriptRun():
    global startedNewServer
    loadProperties("/u01/software/domain.properties")
    hideDisplay()
    hideDumpStack("true")
    # try connecting to a running server if it is already running ...
    if connected=="false":
        try:
            URL="t3://"+adminServerListenAddress+":"+adminServerListenPort
            connect(userName, os.environ('weblogic_admin_password'), URL)
        except WLSTException:
            print 'No server is running at '+URL+', the script will start a new server'
    hideDumpStack("false")
    if connected=="false":
        print 'Starting a brand new server at '+URL+' with server name '+adminServerName
        print 'Please see the server log files for startup messages available at '+domainDir
        # If a config.xml exists in the domainDir, WLST will use that config.xml to bring up the server.
        # If you would like WLST to overwrite this directory, you should specify overWriteRootDir='true' as shown below
        # startServer(adminServerName, domName, URL, userName, os.environ('weblogic_admin_password'),domainDir, overWriteRootDir='true')
        _timeOut = Integer(TimeOut)
        # If you want to specify additional JVM arguments, set them using startServerJvmArgs in the property file or below
        _startServerJvmArgs=startServerJvmArgs
        if (_startServerJvmArgs=="" and (System.getProperty("java.vendor").find("Sun")>=0 or System.getProperty("java.vendor").find("Hewlett")>=0)):
            _startServerJvmArgs = " -XX:MaxPermSize=128m"
        if overWriteRootDir=='true':
            startServer(adminServerName, domName, URL, userName, os.environ('weblogic_admin_password'),domainDir, timeout=_timeOut.intValue(), overWriteRootDir='true', block='true', jvmArgs=_startServerJvmArgs)
        else:
            startServer(adminServerName, domName, URL, userName, os.environ('weblogic_admin_password'),domainDir, timeout=_timeOut.intValue(), block='true', jvmArgs=_startServerJvmArgs)
        startedNewServer=1
        print "Started Server. Trying to connect to the server ... "
        connect(userName, os.environ('weblogic_admin_password'), URL)
        if connected=='false':
            stopExecution('You need to be connected.')


def endOfScriptRun():
    global startedNewServer
    #Save the changes you have made
    # shutdown the server you have started
    if startedNewServer==1:
        print 'Shutting down the server that is started... '
        shutdown(force='true', block='true')
    print 'Done executing the script.'


def createSSOUsersRole():
    cd("/SecurityConfiguration/NDelius/Realms/myrealm/RoleMappers/XACMLRoleMapper")
    try:
        print "creating SSOUsers role..."
        cmo.createRole(None, "SSOUsers", None, "")
        cmo.setRoleExpression(None, "SSOUsers", "?weblogic.entitlement.rules.UncheckedPolicy()")
    except weblogic.management.utils.AlreadyExistsException,ae:
        pass


try:
    initConfigToScriptRun()
    createSSOUsersRole()
finally:
    endOfScriptRun()
