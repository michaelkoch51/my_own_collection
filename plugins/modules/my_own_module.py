#!/usr/bin/python

# Copyright: (c) 2024, Michael Kochnev
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with specified content on the remote host

version_added: "1.0.0"

description:
    - This module creates a text file at the given path with the given content.
    - If the file already exists with the same content, no changes are made
      (idempotency).

options:
    path:
        description: Absolute path to the file to create.
        required: true
        type: str
    content:
        description: Content to write to the file.
        required: true
        type: str

author:
    - Michael Kochnev (@michaelkoch51)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "hello world"
'''

RETURN = r'''
path:
    description: Path to the file that was created.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: Content written to the file.
    type: str
    returned: always
    sample: 'hello world'
'''

import os

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        path='',
        content='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    file_exists = os.path.isfile(path)
    current_content = ''

    if file_exists:
        try:
            with open(path, 'r') as f:
                current_content = f.read()
        except Exception as e:
            module.fail_json(msg='Failed to read file: %s' % str(e), **result)

    if file_exists and current_content == content:
        module.exit_json(**result)

    if module.check_mode:
        result['changed'] = True
        module.exit_json(**result)

    try:
        parent_dir = os.path.dirname(path)
        if parent_dir and not os.path.isdir(parent_dir):
            os.makedirs(parent_dir)
        with open(path, 'w') as f:
            f.write(content)
    except Exception as e:
        module.fail_json(msg='Failed to write file: %s' % str(e), **result)

    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
