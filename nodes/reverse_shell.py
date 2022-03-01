#!/usr/bin/env python3

from nodes.node import Node


class ReverseShell(Node):
    name = "ReverseShell"

    def __init__(self, conn):
        while True:
            data = conn.recv(1024)
            if b'$' in data:
                break
        self.content = conn

    def __str__(self):
        return 'ReverseShell'

    def execute(self, command):
        self.content.send((command + '\n').encode())
        result = ''
        while True:
            data = self.content.recv(1024)
            result += data.decode()
            if b'$' in data:
                break
        return result
