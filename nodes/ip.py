from .node import Node


class IP(Node):
    name = "IP"
    content = None

    def __init__(self, address):
        self.content = address

    def __str__(self):
        return f'{self.content}'
