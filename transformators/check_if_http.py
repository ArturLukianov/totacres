#!/usr/bin/env python3
import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.http import HTTP
import urllib.request
import urllib.error


class CheckHTTP(Transformator):
    name = "check if port is http"
    input_node = "IPPort"

    @staticmethod
    def transform(node):
        try:
            urllib.request.urlopen(f"http://{node.content[0]}:{node.content[1]}/", timeout=3)
            return [HTTP(node.content[0], node.content[1])]
        except urllib.error.URLError:
            return []
