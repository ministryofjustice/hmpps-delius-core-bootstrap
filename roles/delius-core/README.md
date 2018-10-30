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

See the list of variable defaults in [defaults/main.yml](defaults/main.yml). Additional variables are listed below:
```yaml
dependencies_s3_bucket: S3 bucket name, local filesystem will be used if not specified
database_host: Database hostname
oid_host: LDAP hostname, app will run in test mode if this is not specified
ndelius_display_name: NDelius display name for homepage
ndelius_training_mode: development/training/production
ndelius_log_level: Log level eg. TRACE/DEBUG/INFO/WARN/ERROR
ndelius_analytics_tag: Google analytics account tag
newtech_search_url: URL of NewTech national search screen
newtech_pdfgenerator_url: URL of NewTech PDF generator screen
usermanagement_url: URL of user management tool
nomis_url: URL of NOMIS API gateway
```

Example Playbook
----------------

    - hosts: wln
      roles:
        - { role: delius-core }

License
-------

BSD
