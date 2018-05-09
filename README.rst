Cookiecutter Ansible Role
=========================

Cookie cutter recipe to easily create `ansible roles`_. 
It infuses antigravity (or maybe not).

.. _`ansible roles`: http://docs.ansible.com/playbooks_roles.html#roles

Features
--------
  * Follows `best practices`_.
  * Only Creates the necessary files and folders.
  * Blazing fast creation, forget about file creation and focus in actions.

.. _`best practices`: http://docs.ansible.com/playbooks_best_practices.html

Usage
-----

    git clone git@github.com:ltalirz/cookiecutter-ansible-role.git
    pip install cookiecutter
    cookiecutter cookiecutter-ansible-role

Inside a `Add <some> name i.e (<example>)` you can go to next section by entering
an empty string.


Example::

    ROLE CONFIGURATION:
    ===================

    Should it have meta info?  [Y/n] 
     - Should it have dependencies?  [Y/n] 
        Add dependency i.e ({role: aptsupercow, var: 'value'}) {role: cool, version: latest}
        Add dependency i.e ({role: aptsupercow, var: 'value'}) 

    Should it have templates?  [Y/n] n

    Should it have files?  [Y/n] y

This will generate this folders (Please note the absence of templates folder)::

    .
    ├── CONTRIBUTORS.txt
    ├── defaults
    │   └── main.yml
    ├── files
    ├── handlers
    │   └── main.yml
    ├── LICENSE.rst
    ├── meta
    │   └── main.yml
    ├── README.rst
    └── tasks
        └── main.yml

Contributions
-------------

All contributions are more than welcome, please do so.


License
-------

* 3-clause BSD license.
* Copyright ©2014, Enrique Paredes
* Enjoy it!
