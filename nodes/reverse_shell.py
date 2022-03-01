#!/usr/bin/env python3

from nodes.node import Node


class ReverseShell(Node):
    name = "ReverseShell"

    def __init__(self, conn):
        self.content = conn

    def __str__(self):
        return 'ReverseShell'

    def execute(self, command):
        self.content.send(command.encode())
        return self.content.recv(4096)
