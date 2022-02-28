#!/usr/bin/env python3

import sys
sys.path.append("..")

from transformators.transformator import Transformator
from nodes.http_endpoint import HTTPEndpoint
import os
import subprocess


class GobusterFindSubdirs(Transformator):
    name = "gobuster find subdirs and endpoint"
    input_node = "HTTP"
    save_to_dir = None

    @staticmethod
    def initialize(root_dir):
        GobusterFindSubdirs.save_to_dir = os.path.join(root_dir, "gobuster")
        os.mkdir(GobusterFindSubdirs.save_to_dir)

    @staticmethod
    def transform(node):
        if GobusterFindSubdirs.save_to_dir is None:
            print("GobusterFindSubdirs: not initialized, cannot find directory to save files in")
            return []

        with open(os.devnull, "wb") as devnull:
            subprocess.check_call(["gobuster", "dir", "-w", "./resources/common.txt",
                                   "-o", os.path.join(GobusterFindSubdirs.save_to_dir, "scan.txt"),
                                   "-u", str(node)], stdout=devnull, stderr=subprocess.STDOUT)

            endpoints = []

            with open(os.path.join(GobusterFindSubdirs.save_to_dir, "scan.txt")) as f:
                for line in f.readlines():
                    if len(line.strip()) == 0:
                        continue
                    path = line.split('(Status')[0].strip()
                    endpoints.append(HTTPEndpoint(node, path))

            return endpoints
