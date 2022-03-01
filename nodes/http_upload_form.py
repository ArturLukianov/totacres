#!/usr/bin/env python3

from nodes.node import Node


class HTTPUploadForm(Node):
    name = "HTTPUploadForm"

    def __init__(self, endpoint, form, inputname):
        self.content = (endpoint, form, inputname)

    def __str__(self):
        return f"File upload on {str(self.content[0])} (parameter \"{self.content[2]}\")"
