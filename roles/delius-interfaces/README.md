delius-interfaces
=========

Deploy the delius-core REST/SOAP endpoints for DSS, IAPS, OASYS, CaseNotes.

Role Variables
--------------

See the list of variable defaults in [defaults/main.yml](defaults/main.yml). Additional variables are listed below:
```yaml
dependencies_s3_bucket: S3 bucket name, local filesystem will be used if not specified
```

Dependencies
------------

* delius-core

Example Playbook
----------------

    - hosts: wli
      roles:
        - { role: delius-core }
        - { role: delius-interfaces }

License
-------

BSD
