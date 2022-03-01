#!/usr/bin/env python3


import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.flag import Flag


class FindFlagsInRevshell(Transformator):
    name = 'find flags in revshell'
    input_node = 'ReverseShell'

    @staticmethod
    def transform(node):
        output_nodes = []
        res = node.execute("find / -name flag.txt -or -name flag -or -name user.txt -or -name root.txt 2>/dev/null")
        files = res.split('\n')[1:-1]
        for filename in files:
            filename = filename.strip()
            res = node.execute(f"cat {filename}")
            flag = res.split('\n')[1:-1][0].strip()
            output_nodes.append(Flag(flag))
        return output_nodes
