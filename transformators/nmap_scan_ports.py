from .transformator import Transformator


class NmapScanPorts(Transformator):
    name = "nmap scan ports"
    input_node = "IP"

    @staticmethod
    def transform(node):
        return []
