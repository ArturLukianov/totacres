#!/usr/bin/env python3
from nodes.node import Node


class IPPort(Node):
    name = "IPPort"
    content = None

    def __init__(self, address, port):
        self.content = (address, port)

    def __str__(self):
        return f'{self.content[0]}:{self.content[1]}'
