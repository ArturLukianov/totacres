#!/usr/bin/env python3

from nodes.node import Node


class HTTPSubdir(Node):
    name = "HTTPSubdir"

    def __init__(self, http, subdir):
        self.content = (http, subdir)

    def __str__(self):
        return f"{str(self.http)}{self.subdir}"
