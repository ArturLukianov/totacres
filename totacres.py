#!/usr/bin/env python3

import os
import sys
import importlib
import inspect
import time

from transformators.transformator import Transformator
from nodes.ip import IP


ROOT_DIR = "./scans/" + str(time.time())
print(f"[+] Files will be saved to {ROOT_DIR}")
os.mkdir(ROOT_DIR)

## Load transoformator objects from folder
## Not the best way to do it, but it works

transformators = []
transformator_files = os.listdir("transformators/")

for filename in transformator_files:
    if filename.endswith(".py") and not filename.startswith('flycheck'):
        print("[+]", "Loading", filename)
        module_name = filename.split('.')[0]
        module = importlib.import_module(f"transformators.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if inspect.isclass(attribute) and attribute.__module__ == module.__name__ and issubclass(attribute, Transformator):
                transformators.append(attribute)
                transformators[-1].initialize(ROOT_DIR)
                print("[+]", "Loaded", attribute.name, "transformator")


## Here we are initializing array of nodes and creating a node queue
nodes = []
node_queue = [] # TODO: Replace with actual Queue from collections

## We are creating our initial node here
nodes.append(IP(sys.argv[1]))
node_queue.append(nodes[0])

## The main loop (BFS) - apply transformators to every sutiable node
while len(node_queue) != 0:
    current_node = node_queue[0]
    node_queue.pop(0)
    print("[+]", "Processing", str(current_node))
    for transformator in transformators:
        if transformator.input_node == current_node.name:
            print("[+]", "Applying", transformator.name)
            new_nodes = transformator.transform(current_node)
            nodes.extend(new_nodes)
            node_queue.extend(new_nodes)

## Finishing - let's print out all info we got
## TODO: Make a webapp to draw a nice graph in real time
for node in nodes:
    print(str(node))

