# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from distutils.version import LooseVersion

import sys

import ansible


try:
    # Version 2.0+
    from ansible.plugins.callback import CallbackBase
except ImportError:
    CallbackBase = object


def print_red_bold(text):
    print('\x1b[31;1m' + text + '\x1b[0m')


class CallbackModule(CallbackBase):
    def __init__(self):
        # Can't use `on_X` because this isn't forwards compatible with Ansible 2.0+
        required_version = '2.1.0'
        installed_version = ansible.__version__
        if LooseVersion(installed_version) < LooseVersion(required_version):
            print_red_bold(
                "drupal-vm restriction: only Ansible version greater than {version} is supported.\n"
                .format(version=required_version)
            )
            sys.exit(1)
