from java.lang import System


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
        if (_startServerJvmArgs=="" and (System.getProperty("java.vendor").find("Sun")>=0 or System.getProperty("java.vendor").find("Hewlett")>=0)):
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
    set("Password", deliusPoolPassword)
    set("DriverName", "oracle.jdbc.xa.client.OracleXADataSource")
    set("Url", "jdbc:oracle:thin:@"+applicationDatabaseHost+":"+applicationDatabasePort+":"+applicationDatabaseSID)

def setAttributes_JDBCOracleParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCOracleParams/NDELIUS")
    print "setting attributes for mbean type JDBCOracleParams"
    set("UseDatabaseCredentials", "true")

def setAttributes_JDBCConnectionPoolParams_NDELIUS():
    cd("/JDBCSystemResources/NDELIUS/JDBCResource/NDELIUS/JDBCConnectionPoolParams/NDELIUS")
    print "setting attributes for mbean type JDBCConnectionPoolParams"
    set("TestTableName", "SQL SELECT 1 FROM DUAL")
    set("CredentialMappingEnabled", "true")

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
    set("Password", deliusPoolPassword)
    set("DriverName", "oracle.jdbc.OracleDriver")
    set("Url", "jdbc:oracle:thin:@"+applicationDatabaseHost+":"+applicationDatabasePort+":"+applicationDatabaseSID)

def setAttributes_JDBCConnectionPoolParams_NDELIUS_JTA():
    cd("/JDBCSystemResources/NDELIUS_JTA/JDBCResource/NDELIUS_JTA/JDBCConnectionPoolParams/NDELIUS_JTA")
    print "setting attributes for mbean type JDBCConnectionPoolParams"
    set("TestTableName", "SQL SELECT 1 FROM DUAL")
    set("CredentialMappingEnabled", "true")

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
    endTransaction()
finally:
    endOfScriptRun()
