#!/usr/bin/env python3


import sys
sys.path.append('..')

from transformators.transformator import Transformator


class FindFlagsInRevshell(Transformator):
    name = 'find flags in revshell'
    input_node = 'ReverseShell'

    @staticmethod
    def transform(node):
        pass
