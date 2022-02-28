#!/usr/bin/env python3

from nodes.node import Node


class HTTPEndpoint(Node):
    name = "HTTPEndpoint"

    def __init__(self, http, endpoint):
        self.content = (http, endpoint)

    def __str__(self):
        return f"{self.content[0]}{self.content[1]}"
