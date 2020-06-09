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
            connect(userName, os.environ['weblogic_admin_password'], URL)
        except WLSTException:
            print 'No server is running at '+URL+', the script will start a new server'
    hideDumpStack("false")
    if connected=="false":
        print 'Starting a brand new server at '+URL+' with server name '+adminServerName
        print 'Please see the server log files for startup messages available at '+domainDir
        # If a config.xml exists in the domainDir, WLST will use that config.xml to bring up the server.
        # If you would like WLST to overwrite this directory, you should specify overWriteRootDir='true' as shown below
        # startServer(adminServerName, domName, URL, userName, os.environ['weblogic_admin_password'),domainDir, overWriteRootDir='true']
        _timeOut = Integer(TimeOut)
        # If you want to specify additional JVM arguments, set them using startServerJvmArgs in the property file or below
        _startServerJvmArgs=startServerJvmArgs
        if (_startServerJvmArgs=="" and (System.getProperty("java.vendor").find("Sun")>=0 or System.getProperty("java.vendor").find("Hewlett")>=0)):
            _startServerJvmArgs = " -XX:MaxPermSize=128m"
        if overWriteRootDir=='true':
            startServer(adminServerName, domName, URL, userName, os.environ['weblogic_admin_password'],domainDir, timeout=_timeOut.intValue(), overWriteRootDir='true', block='true', jvmArgs=_startServerJvmArgs)
        else:
            startServer(adminServerName, domName, URL, userName, os.environ['weblogic_admin_password'],domainDir, timeout=_timeOut.intValue(), block='true', jvmArgs=_startServerJvmArgs)
        startedNewServer=1
        print "Started Server. Trying to connect to the server ... "
        connect(userName, os.environ['weblogic_admin_password'], URL)
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
    #Save the changes you have made
    # shutdown the server you have started
    if startedNewServer==1:
        print 'Shutting down the server that is started... '
        shutdown(force='true', block='true')
    print 'Done executing the script.'

def create_JDBCSystemResource(path, beanName):
    cd(path)
    try:
        print "creating mbean of type JDBCSystemResource ... "
        theBean = cmo.lookupJDBCSystemResource(beanName)
        if theBean == None:
            cmo.createJDBCSystemResource(beanName)
    except java.lang.UnsupportedOperationException, usoe:
        pass
    except weblogic.descriptor.BeanAlreadyExistsException,bae:
        pass
    except java.lang.reflect.UndeclaredThrowableException,udt:
        pass

def create_Property(path, beanName):
    cd(path)
    try:
        print "creating mbean of type Property ... "
        theBean = cmo.lookupProperty(beanName)
        if theBean == None:
            cmo.createProperty(beanName)
    except java.lang.UnsupportedOperationException, usoe:
        pass
    except weblogic.descriptor.BeanAlreadyExistsException,bae:
        pass
    except java.lang.reflect.UndeclaredThrowableException,udt:
        pass
    except TypeError:
        prop = cmo.createProperty()
        prop.setName(beanName)

def setAttributes_JDBCDataSourceParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCDataSourceParams/NDELIUS")
    print "setting attributes for mbean type JDBCDataSourceParams"
    set("GlobalTransactionsProtocol", "None")
    set("JNDINames", jarray.array(["NDELIUS"], String))

def setAttributes_JDBCDataSource_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCDataSource"
    set("Name", "NDELIUS_JTA")

def setAttributesFor_user_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCDriverParams/NDELIUS_JTA/Properties/NDELIUS_JTA/Properties/user")
    print "setting attributes for mbean type JDBCProperty"
    set("Value", "delius_pool")
    set("Name", "user")

def setAttributes_JDBCOracleParams_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCOracleParams/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCOracleParams"
    set("UseDatabaseCredentials", "true")

def setAttributesFor_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS")
    print "setting attributes for mbean type JDBCSystemResource"
    refBean0 = getMBean("/Servers/AdminServer")
    theValue = jarray.array([refBean0], Class.forName("weblogic.management.configuration.TargetMBean"))
    cmo.setTargets(theValue)

def setAttributesFor_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCSystemResource"
    refBean0 = getMBean("/Servers/AdminServer")
    theValue = jarray.array([refBean0], Class.forName("weblogic.management.configuration.TargetMBean"))
    cmo.setTargets(theValue)

def setAttributes_JDBCDataSourceParams_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCDataSourceParams/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCDataSourceParams"
    set("GlobalTransactionsProtocol", "TwoPhaseCommit")
    set("JNDINames", jarray.array(["NDELIUS_JTA"], String))

def setAttributes_JDBCDriverParams_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCDriverParams/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCDriverParams"
    set("Password", os.environ['database_password'])
    set("DriverName", "oracle.jdbc.xa.client.OracleXADataSource")
    set("Url", databaseURL)

def setAttributes_JDBCOracleParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCOracleParams/NDELIUS")
    print "setting attributes for mbean type JDBCOracleParams"
    set("UseDatabaseCredentials", "true")

def setAttributes_JDBCConnectionPoolParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCConnectionPoolParams/NDELIUS")
    print "setting attributes for mbean type JDBCConnectionPoolParams"
    set("TestTableName", "SQL SELECT 1 FROM DUAL")
    set("CredentialMappingEnabled", "true")
    set("MaxCapacity", databaseMaxPoolSize)
    set("MinCapacity", databaseMinPoolSize)
    set("InactiveConnectionTimeoutSeconds", "30")

def setAttributesFor_user_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCDriverParams/NDELIUS/Properties/NDELIUS/Properties/user")
    print "setting attributes for mbean type JDBCProperty"
    set("Value", "delius_pool")
    set("Name", "user")

def setAttributes_JDBCDataSource_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS")
    print "setting attributes for mbean type JDBCDataSource"
    set("Name", "NDELIUS")

def setAttributes_JDBCDriverParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCDriverParams/NDELIUS")
    print "setting attributes for mbean type JDBCDriverParams"
    set("Password", os.environ['database_password'])
    set("DriverName", "oracle.jdbc.OracleDriver")
    set("Url", databaseURL)

def setAttributes_JDBCConnectionPoolParams_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCConnectionPoolParams/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCConnectionPoolParams"
    set("TestTableName", "SQL SELECT 1 FROM DUAL")
    set("MaxCapacity", databaseMaxPoolSize)
    set("MinCapacity", databaseMinPoolSize)
    set("CredentialMappingEnabled", "true")

## PERSISTENCE_STORE postgres DB

def setAttributesFor_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE")
    print "setting attributes for mbean type JDBCSystemResource"
    refBean0 = getMBean("/Servers/AdminServer")
    theValue = jarray.array([refBean0], Class.forName("weblogic.management.configuration.TargetMBean"))
    cmo.setTargets(theValue)

def setAttributesFor_user_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCDriverParams/PERSISTENCE_STORE/Properties/PERSISTENCE_STORE/Properties/user")
    print "setting attributes for mbean type JDBCProperty"
    set("Value", "postgres")
    set("Name", "user")

def setAttributes_JDBCDataSourceParams_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCDataSourceParams/PERSISTENCE_STORE")
    print "setting attributes for mbean type JDBCDataSourceParams"
    set("GlobalTransactionsProtocol", "None")
    set("JNDINames", jarray.array(["PERSISTENCE_STORE"], String))

#def setAttributes_JDBCOracleParams_PERSISTENCE_STORE():
#    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCOracleParams/PERSISTENCE_STORE")
#    print "setting attributes for mbean type JDBCOracleParams"
#    set("UseDatabaseCredentials", "true")

def setAttributes_JDBCConnectionPoolParams_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCConnectionPoolParams/PERSISTENCE_STORE")
    print "setting attributes for mbean type JDBCConnectionPoolParams"
    set("TestTableName", "SQL SELECT 1")
    #set("CredentialMappingEnabled", "true")
    set("MaxCapacity", 20)
    set("MinCapacity", 10)
    #set("InactiveConnectionTimeoutSeconds", "30")

def setAttributes_JDBCDataSource_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE")
    print "setting attributes for mbean type JDBCDataSource"
    set("Name", "PERSISTENCE_STORE")

def setAttributes_JDBCDriverParams_PERSISTENCE_STORE():
    cd("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCDriverParams/PERSISTENCE_STORE")
    print "setting attributes for mbean type JDBCDriverParams"
    set("Password", os.environ['ps_database_password'])
    set("DriverName", "org.postgresql.Driver")
    set("Url", psDatabaseURL)

try:
    initConfigToScriptRun()
    startTransaction()
    create_JDBCSystemResource("/", "NDELIUS")
    create_Property("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCDriverParams/NDELIUS/Properties/NDELIUS", "user")
    create_JDBCSystemResource("/", "NDELIUS_JTA")
    create_Property("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCDriverParams/NDELIUS_JTA/Properties/NDELIUS_JTA", "user")
    setAttributesFor_NDELIUS()
    setAttributesFor_NDELIUS_JTA()
    setAttributesFor_user_NDELIUS()
    setAttributesFor_user_NDELIUS_JTA()
    setAttributes_JDBCDataSourceParams_NDELIUS()
    setAttributes_JDBCDataSource_NDELIUS_JTA()
    setAttributes_JDBCOracleParams_NDELIUS_JTA()
    setAttributes_JDBCDataSourceParams_NDELIUS_JTA()
    setAttributes_JDBCDriverParams_NDELIUS_JTA()
    setAttributes_JDBCOracleParams_NDELIUS()
    setAttributes_JDBCConnectionPoolParams_NDELIUS()
    setAttributes_JDBCDataSource_NDELIUS()
    setAttributes_JDBCDriverParams_NDELIUS()
    setAttributes_JDBCConnectionPoolParams_NDELIUS_JTA()
    # PERSISTENCE_STORE
    create_JDBCSystemResource("/", "PERSISTENCE_STORE")
    create_Property("/JDBCSystemResources/PERSISTENCE_STORE/JDBCResource/PERSISTENCE_STORE/JDBCDriverParams/PERSISTENCE_STORE/Properties/PERSISTENCE_STORE", "user")
    setAttributesFor_PERSISTENCE_STORE()
    setAttributesFor_user_PERSISTENCE_STORE()
    setAttributes_JDBCDataSourceParams_PERSISTENCE_STORE()
    #setAttributes_JDBCOracleParams_PERSISTENCE_STORE()
    setAttributes_JDBCConnectionPoolParams_PERSISTENCE_STORE()
    setAttributes_JDBCDataSource_PERSISTENCE_STORE()
    setAttributes_JDBCDriverParams_PERSISTENCE_STORE()
    endTransaction()
finally:
    endOfScriptRun()
