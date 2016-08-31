#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

import sys

from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from Constants.Constants import *
from GUI.ChatWindow import *

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
        QtCore.QSettings.qRegisterMetaType(QtGUI.QTextCursor)
        # self.server.register_instance(RecordAudioWindow(self.gui.channel,
        #                                                 self.gui))

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
        self.gui.update_chat('\nyour friend says: ', message)
        return 'ACK.'

    def startCall_wrapper(self):
        self.gui.emit(QtCore.SIGNAL("llamadaEmpezada()"))
        print('lel')
        self.gui.record_audio()
        # self.gui.audio_window = ChatWindow.RecordAudioWindow(self.gui.channel,
        #                                                      self.gui)
        print('lele2')
        return 'ok.'

    def sendAudio_wrapper(self, audio):
        '''
        Receives and plays audio
        '''
        self.gui.emit(QtCore.SIGNAL("audioRecibidio(bytes)"), audio)
        # self.gui.record_audio()
        print('Audio received')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             frames_per_buffer=CHUNK)
        self.stream.write(audio)
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        return 'ok.'
