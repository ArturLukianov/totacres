import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.ip_port import IPPort
import os
import subprocess
import xml.etree.ElementTree as ET


class NmapScanPorts(Transformator):
    name = "nmap scan ports"
    input_node = "IP"
    save_to_dir = None

    @staticmethod
    def transform(node):
        if NmapScanPorts.save_to_dir is None:
            print("NmapScanPorts: not initialized, cannot find directory to save files in")
            return []

        with open(os.devnull, "wb") as devnull:
            subprocess.check_call(["nmap", "-p-", "-oX",
                                   os.path.join(NmapScanPorts.save_to_dir, "scan.xml"),
                                   node.content], stdout=devnull, stderr=subprocess.STDOUT)

        tree = ET.parse(os.path.join(NmapScanPorts.save_to_dir, "scan.xml"))
        root = tree.getroot()
        ports = []
        for port in root.find('host').find('ports').findall('port'):
            ports.append(IPPort(node.content, port.get('portid')))
        return ports

    @staticmethod
    def initialize(root_dir):
        NmapScanPorts.save_to_dir = os.path.join(root_dir, "nmap_ports")
        os.mkdir(NmapScanPorts.save_to_dir)
