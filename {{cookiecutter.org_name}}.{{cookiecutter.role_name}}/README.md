[![Build Status](https://travis-ci.org/{{cookiecutter.org_name}}/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.org_name}}/{{cookiecutter.repo_name}})

# Ansible Role: {{cookiecutter.org_name}}.{{cookiecutter.role_name}}

{{cookiecutter.short_description}}

## Installation

`ansible-galaxy install {{cookiecutter.org_name}}.{{cookiecutter.role_name}}`

## Role Variables

See `defaults/main.yml`

## Example Playbook

```yaml
- hosts: servers
  roles:
  - role: {{cookiecutter.org_name}}.{{cookiecutter.role_name}}
```

## Development and testing

This role uses [Molecule](https://molecule.readthedocs.io/en/latest/#) and [Docker](https://www.docker.com/) for tests.

After installing [Docker](https://www.docker.com/):
```
git clone https://github.com/{{cookiecutter.org_name}}/{{cookiecutter.repo_name}} {{cookiecutter.org_name}}.{{cookiecutter.role_name}}
# Note: folder name {{cookiecutter.org_name}}.{{cookiecutter.role_name}} is required for running tests
cd marvel-nccr.aiida
pip install -r requirements.txt  # Installs molecule
molecule test  # runs tests

## License

MIT

## Contact

Please direct inquiries regarding Quantum Mobile and associated ansible roles to the [AiiDA mailinglist](http://www.aiida.net/mailing-list/).
