#!/usr/bin/env python3

from nodes.node import Node


class HTTP(Node):
    name = "HTTP"
    content = None

    def __init__(self, ip, port):
        self.content = f"http://{ip}:{port}/"

    def __str__(self):
        return self.content
