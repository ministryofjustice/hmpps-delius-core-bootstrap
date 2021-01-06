Delius-Core WebLogic Bootstrap
=========

A collection of roles used for bootstrapping the National Delius WebLogic EC2 instances.  


Roles
-----

| Name                                         | Description |
| -------------------------------------------- | ----------- |
| [delius-core](roles/delius-core)             | Updates WebLogic configuration (eg. data sources, security, monitoring) and deploys the National Delius core application. |
| [delius-interfaces](roles/delius-interfaces) | Deploys the additional APIs used to support National Delius external interfaces. |
| [delius-spg](roles/delius-spg)               | Deploys the ActiveMQ broker and consumer code to support CRC messaging via the SPG. |

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: delius-core }
         - { role: delius-spg }
License
-------
MIT

Contact
-------

For any issues, please either raise an issue against this GitHub repository or contact the Delius Infrastructure Support team directly via the [#delius_infra_support](https://mojdt.slack.com/archives/CNXK9893K) Slack channel.