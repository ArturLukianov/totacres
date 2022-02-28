#!/usr/bin/env python3

from nodes.node import Node


class HTTPUploadForm(Node):
    name = "HTTPUploadForm"

    def __init__(self, endpoint, filename):
        self.content = (endpoint, filename)

    def __str__(self):
        return f"File upload on {str(self.content[1])} (parameter \"{self.content[1]}\")"
