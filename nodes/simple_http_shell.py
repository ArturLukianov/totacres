#!/usr/bin/env python3

from nodes.node import Node
import requests


class SimpleHTTPShell(Node):
    name = "SimpleHTTPShell"

    def __init__(self, httpendpoint):
        self.content = httpendpoint

    def __str__(self):
        return f'WebShell: {str(self.content)}'

    def execute(self, command):
        try:
            res = requests.get(str(self.content), params={'q': command}, timeout=3).text
            return res
        except requests.exceptions.ReadTimeout:
            return ''
