#!/usr/bin/env python3

from nodes.node import Node


class Flag(Node):
    name = "Flag"

    def __init__(self, flag):
        self.content = flag

    def __str__(self):
        return f'Flag: {self.content}'
