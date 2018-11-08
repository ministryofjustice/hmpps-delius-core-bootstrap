import sys


def initConfigToScriptRun():
    global startedNewServer
    loadProperties("/u01/software/domain.properties")
    hideDisplay()
    hideDumpStack("true")
    # try connecting to a running server if it is already running ...
    if connected=="false":
        try:
            URL="t3://"+adminServerListenAddress+":"+adminServerListenPort
            connect(userName, passWord, URL)
        except WLSTException:
            print 'No server is running at '+URL+', the script will start a new server'
    hideDumpStack("false")
    if connected=="false":
        print 'Starting a brand new server at '+URL+' with server name '+adminServerName
        print 'Please see the server log files for startup messages available at '+domainDir
        # If a config.xml exists in the domainDir, WLST will use that config.xml to bring up the server.
        # If you would like WLST to overwrite this directory, you should specify overWriteRootDir='true' as shown below
        # startServer(adminServerName, domName, URL, userName, passWord,domainDir, overWriteRootDir='true')
        _timeOut = Integer(TimeOut)
        # If you want to specify additional JVM arguments, set them using startServerJvmArgs in the property file or below
        _startServerJvmArgs=startServerJvmArgs
        if _startServerJvmArgs== "" and (System.getProperty("java.vendor").find("Sun") >= 0 or System.getProperty("java.vendor").find("Hewlett") >= 0):
            _startServerJvmArgs = " -XX:MaxPermSize=128m"
        if overWriteRootDir=='true':
            startServer(adminServerName, domName, URL, userName, passWord,domainDir, timeout=_timeOut.intValue(), overWriteRootDir='true', block='true', jvmArgs=_startServerJvmArgs)
        else:
            startServer(adminServerName, domName, URL, userName, passWord,domainDir, timeout=_timeOut.intValue(), block='true', jvmArgs=_startServerJvmArgs)
        startedNewServer=1
        print "Started Server. Trying to connect to the server ... "
        connect(userName, passWord, URL)
        if connected=='false':
            stopExecution('You need to be connected.')


def startTransaction():
    edit()
    startEdit()


def endTransaction():
    startEdit()
    save()
    activate(block="true")


def endOfScriptRun():
    global startedNewServer
    # Save the changes you have made
    # shutdown the server you have started
    if startedNewServer==1:
        print 'Shutting down the server that is started... '
        shutdown(force='true', block='true')
    print 'Done executing the script.'


def deployArtifact(name, artifact, order):
    print "Deploying " + artifact + "... "
    deploy(name, '/u01/software/' + artifact, upload='true', timeout=900000, deploymentOrder=int(order))
    print "Finished deploying " + artifact


try:
    initConfigToScriptRun()
    startTransaction()
    deployArtifact(sys.argv[1], sys.argv[2], sys.argv[3])
    endTransaction()
finally:
    endOfScriptRun()
