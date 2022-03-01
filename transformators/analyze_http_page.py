#!/usr/bin/env python3

import sys
sys.path.append('..')

from transformators.transformator import Transformator
from nodes.http_upload_form import HTTPUploadForm
import urllib.request
import urllib.error
import html.parser


class AnalyzeParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_in_form = False
        self.form = None

    def handle_starttag(self, tag, attrs):
        if tag == 'form':
            self.is_in_form = True
            self.form = []
            return

        if self.is_in_form and tag == 'input':
            type_ = None
            name = None
            value = None
            for attrname, attrval in attrs:
                if attrname == 'type':
                    type_ = attrval
                elif attrname == 'name':
                    name = attrval
                elif attrname == 'value':
                    value = attrval
            self.form.append({'type': type_, 'name': name, 'value': value})

    def handle_endtag(self, tag):
        if tag == 'form':
            self.is_in_form = False


class AnalyzeHTTPPage(Transformator):
    name = "analyze http page"
    input_node = "HTTPEndpoint"

    @staticmethod
    def transform(node):
        try:
            with urllib.request.urlopen(str(node)) as r:
                html = r.read()
            parser = AnalyzeParser()
            parser.feed(html.decode())
            output_nodes = []
            if parser.form is not None and any([x['type'] == 'file' for x in parser.form]):
                output_nodes.append(HTTPUploadForm(node, parser.form, parser.form[0]['name']))
            return output_nodes
        except urllib.error.HTTPError:
            return []
