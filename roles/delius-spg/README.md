delius-spg
=========

Deploy and configure the delius-core ActiveMQ message broker, as well as the NDelius-SPG application for consuming and processing messages from Community Rehabilitation Companies (CRCs).

If `activemq_efs_dns_name` is provided, an EFS is also mounted to enable ActiveMQ to run in High Availability (Active/Passive) mode.


Role Variables
--------------

```yaml
# SPG
spg_jms_url: SPG broker hostname
activemq_data_folder: Used for storing ActiveMQ persistent data eg. unprocessed messages
activemq_efs_dns_name: DNS name for the EFS file system that should be mounted at {{activemq_data_folder}}
```

Example Playbook
----------------

    - hosts: wls
      roles:
        - { role: delius-core }
        - { role: delius-spg }
