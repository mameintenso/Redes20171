#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc.client

class MyApiClient:

    def __init__(self, proxy_uri):
        if proxy_uri is not None:
            self.server = xmlrpc.client.ServerProxy(proxy_uri,
                                                    allow_none=True)

    def send_message(self, message):
        print(self.server.sendMessage_wrapper(message))
