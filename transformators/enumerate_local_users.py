#!/usr/bin/env python3

import sys
sys.path.append('..')

from nodes.local_user import LocalUser
from transformators.transformator import Transformator


class EnumerateLocalUsers(Transformator):
    name = "enumerate local users"
    input_node = "ReverseShell"

    @staticmethod
    def transform(node):
        res = node.execute('cat /etc/passwd')
        users = res.split('\n')[1:-1]
        output_nodes = []
        for user in users:
            username, passwd, uid, gid, descr, home, shell = user.strip().split(':')
            if not shell.endswith('/nologin'):
                output_nodes.append(LocalUser(username))
        return output_nodes
