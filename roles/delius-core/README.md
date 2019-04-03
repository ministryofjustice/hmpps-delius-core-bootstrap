delius-core
=========

Apply the standard NDelius configuration to a weblogic host and deploy the NDelius-ear.ear file.
 
Config includes applying the weblogic datasource + security configuration, as well as adding the following files to the domain root:
* `NDelius.properties`
* `nomis-api.properties`
* `log4j.xml`
* `password.keyfile`

Role Variables
--------------

```yaml
# Artefact locations
s3_dependencies_bucket:

# Server/WebLogic config
domain_name: WebLogic domain name - must match configured AMI value
jvm_mem_args: WebLogic JVM arguments
server_name: Name to give the admin server
weblogic_admin_username: Username to connect to WebLogic
weblogic_admin_password: Password to connect to WebLogic
server_listen_address: IP Address to publish on
server_listen_port: Port to publish on

# Database
database_url: JDBC URL for the database connection
setup_datasources: Whether to setup or skip setting up the database connection

# Alfresco
alfresco_host: Alfresco hostname
alfresco_port: Alfresco port
alfresco_office_host: Alfresco hostname for opening Office documents
alfresco_office_port: Alfresco port for opening Office documents

# SPG
spg_host: SPG broker hostname

# LDAP
ldap_host: LDAP master hostname for writing to
ldap_readonly_host: LDAP slave hostname for reading from
ldap_port: LDAP port
ldap_principal: Username to connect to LDAP with
ldap_admin_password: Password to use for connecting to LDAP
partition_id: LDAP partition ID
ldap_base: Default base
ldap_user_base: Base where users are located
ldap_group_base: Base where groups are located

# App Config
ndelius_display_name: Display name on front-end of application
ndelius_training_mode: development, training or production
ndelius_log_level: Output log level
ndelius_analytics_tag: Google analytics tag
ldap_passfile: Where the LDAP password file should be located

# New Tech
newtech_search_url: New tech URL
newtech_pdfgenerator_url: New tech URL
newtech_pdfgenerator_templates: Template names designated for PDF generation (pipe-separated)
newtech_pdfgenerator_secret: PDF generator shared key

# User Management Tool
usermanagement_url: UMT url
usermanagement_secret: UMT shared key

# NOMIS
nomis_url: NOMIS url
nomis_client_id: NOMIS OAuth id
nomis_client_secret: NOMIS OAuth secret
```

Example Playbook
----------------

    - hosts: wln
      roles:
        - { role: delius-core }

License
-------

BSD
