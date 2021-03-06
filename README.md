[![Build Status](https://travis-ci.org/marvel-nccr/cookiecutter-ansible-role.svg?branch=master)](https://travis-ci.org/marvel-nccr/cookiecutter-ansible-role)

# Cookiecutter for Ansible Role

Cookie cutter recipe for quickly creating new [ansible
roles](http://docs.ansible.com/playbooks_roles.html#roles)
for the [marvel-nccr](https://galaxy.ansible.com/marvel-nccr) ansible galaxy namespace.

See also the [ansible docs](https://docs.ansible.com/ansible-container/roles/writing.html#writing-roles) on writing roles.

## Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/marvel-nccr/cookiecutter-ansible-role.git
```

Note: for the ansible-galaxy badge in the `README.md`, you will need to update it with the correct ID once the role has been uploaded: `ansible-galaxy role info marvel-nccr.test`.

## License

See [LICENSE](LICENSE) file.
