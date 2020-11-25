[![CI](https://github.com/{{ cookiecutter.org_name }}/{{ cookiecutter.repo_name }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.org_name }}/{{ cookiecutter.repo_name }}/actions)
[![Ansible Role](https://img.shields.io/ansible/role/25521.svg)](https://galaxy.ansible.com/{{ cookiecutter.org_name }}/{{ cookiecutter.role_name }})
[![Release](https://img.shields.io/github/tag/{{ cookiecutter.org_name }}/{{ cookiecutter.repo_name }}.svg)](https://github.com/{{ cookiecutter.org_name }}/{{ cookiecutter.repo_name }}/releases)

# Ansible Role: {{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}

{{cookiecutter.short_description}}

## Installation

`ansible-galaxy install {{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}`

## Role Variables

See `defaults/main.yml`

## Example Playbook

```yaml
- hosts: servers
  roles:
  - role: {{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}
```

## Development and testing

This role uses [Molecule](https://molecule.readthedocs.io/en/latest/#) and [Docker](https://www.docker.com/) for tests.

After installing [Docker](https://www.docker.com/):

Clone the repository into a package named `{{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}` (the folder must be named the same as the Ansible Galaxy name)

```bash
git clone https://github.com/{{ cookiecutter.org_name }}/{{ cookiecutter.repo_name }} {{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}
cd {{ cookiecutter.org_name }}.{{ cookiecutter.role_name }}
```

Then run:

```bash
pip install -r requirements.txt  # Installs molecule
molecule test  # runs tests
```

or use tox (see `tox.ini`):

```bash
pip install tox
tox
```

## Code style

Code style is formatted and linted with [pre-commit](https://pre-commit.com/).

```bash
pip install pre-commit
pre-commit run -all
```

## Deployment

Deployment to Ansible Galaxy is automated *via* GitHub Actions.
Simply tag a release `vX.Y.Z` to initiate the CI and release workflow.
Note, the release will only complete if the CI tests pass.

## License

MIT

## Contact

Please direct inquiries regarding Quantum Mobile and associated ansible roles to the [AiiDA mailinglist](http://www.aiida.net/mailing-list/).
