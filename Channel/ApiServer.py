#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class MyApiServer(Thread):
    def __init__(self, my_ip, my_port=None):
        super(MyApiServer, self).__init__()
        if my_port is not None:
            self.server = SimpleXMLRPCServer((my_ip, int(my_port)),
                                             requestHandler=RequestHandler,
                                             allow_none=True)
        else:
            self.server = SimpleXMLRPCServer((my_ip, 8000),
                                             requestHandler=RequestHandler,
                                             allow_none=True)
        self.server.register_instance(FunctionWrapper())
        self.server.register_introspection_functions()

    def run(self):
        print('Listening on port', self.my_port, '...')
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            self.server.server_close()
            sys.exit(0)

class FunctionWrapper:
    def __init__(self):
        pass

    def sendMessage_wrapper(self, message):
        """
        Procedimiento que ofrece nuestro servidor, este metodo sera llamado
        por el cliente con el que estamos hablando, debe de
        hacer lo necesario para mostrar el texto en nuestra pantalla.
        """
        print('Message received:', message)
        return 'ACK.'
