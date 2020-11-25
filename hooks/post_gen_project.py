#!/usr/bin/env python
import os
import shutil

REMOVE_FOLDERS = {
    'full': [],
    'minimal': ['files', 'handlers', 'templates'],
}


def configure_role():
    structure = "{{ cookiecutter.structure }}"
    for folder_name in REMOVE_FOLDERS.get(structure, []):
        if os.path.exists(folder_name):
            shutil.rmtree(folder_name)


if __name__ == '__main__':
    configure_role()
