#!/usr/bin/env python3

from nodes.node import Node


class LocalUser(Node):
    name = "LocalUser"

    def __init__(self, username, password=None):
        self.content = username

    def __str__(self):
        return 'User: ' + self.content
