#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc.client

from ApiServer import *

class MyApiClient:

    def __init__(self, proxy_uri=None):
        if proxy_uri is not None:
            self.server = xmlrpc.client.ServerProxy(proxy_uri,
                                                    allow_none=True)
        else:
            self.server = xmlrpc.client.ServerProxy('http://localhost:8000',
                                                    allow_none=True)

    def send_message(self, message):
        print(self.server.sendMessage_wrapper(message))
