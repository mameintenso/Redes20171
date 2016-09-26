#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL, pyqtSignal

import sys

from threading import Thread

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

from Constants.Constants import *
from GUI.ChatWindow import *

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class MyApiServer(Thread):
    def __init__(self, my_ip, my_port, gui):
        super(MyApiServer, self).__init__()
        self.gui = gui
        self.my_ip = my_ip
        self.my_port = my_port
        if my_port is not None:
            self.server = SimpleXMLRPCServer((my_ip, int(my_port)),
                                             requestHandler=RequestHandler,
                                             allow_none=True)
        self.server.register_instance(FunctionWrapper(self.gui,
                                                      self.my_ip,
                                                      self.my_port))
        self.server.register_introspection_functions()

    def run(self):
        print 'Listening on port ' + self.my_port + '...'
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print '\nKeyboard interrupt received, exiting.'
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
        print 'Message received:' + message
        self.gui.update_chat('\nyour friend says: ', message)
        return 'ACK.'

    def incommingCall_wrapper(self):
        # self.gui.emit(QtCore.SIGNAL("llamadaEmpezada(QString)"), 'lel')
        # self.trigger = pyqtSignal()
        # self.trigger.connect(self.gui.incomming_audio_call)
        print 'Establishing audio call connection...'
        # self.trigger.emit()
        self.gui.incomming_audio_call()
        return 'ok.'

    def playAudio_wrapper(self, audio):
        '''
        Receives and plays audio
        '''
        self.gui.emit(QtCore.SIGNAL("audioRecibidio(bytes)"), audio)
        print 'Audio received'
        self.p = pyaudio.PyAudio()
        FORMAT = self.p.get_format_from_width(2)
        self.stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             output=True,
                             frames_per_buffer=CHUNK)
        self.stream.write(audio.data)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        return 'ok.'
