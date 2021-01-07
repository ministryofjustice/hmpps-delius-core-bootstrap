delius-interfaces
=========

Deploy the delius-core REST/SOAP endpoints for DSS, IAPS, OASYS, CaseNotes.

Dependencies
------------

* delius-core

Example Playbook
----------------

    - hosts: wli
      roles:
        - { role: delius-core }
        - { role: delius-interfaces }
