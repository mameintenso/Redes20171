#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

import sys

from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class MyApiServer(Thread):
    def __init__(self, my_ip, my_port, gui):
        super(MyApiServer, self).__init__()

        self.my_ip = my_ip
        self.my_port = my_port
        if my_port is not None:
            self.server = SimpleXMLRPCServer((my_ip, int(my_port)),
                                             requestHandler=RequestHandler,
                                             allow_none=True)
        self.server.register_instance(FunctionWrapper(gui, my_ip, my_port))
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
    def __init__(self, gui, ip, port):
        self.gui = gui
        self.ip = ip
        self.port = port

    def sendMessage_wrapper(self, message):
        """
        Procedimiento que ofrece nuestro servidor, este metodo sera llamado
        por el cliente con el que estamos hablando, debe de
        hacer lo necesario para mostrar el texto en nuestra pantalla.
        """
        self.gui.emit(QtCore.SIGNAL("agregarMensaje(QString)"), message)
        print('Message received:', message)
        self.gui.update_chat('\nyour friend says: ', message, self.ip, self.port)
        return 'ACK.'
