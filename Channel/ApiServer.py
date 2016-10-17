#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, QThread
from PyQt4.QtCore import SIGNAL, pyqtSignal

import sys

from threading import Thread

import numpy as np
import xmlrpclib
import cv2
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from cStringIO import StringIO
from Constants.Constants import *
from GUI.ChatWindow import *

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class MyApiServer(Thread):
    def __init__(self, my_ip, my_port, QParent):
        super(MyApiServer, self).__init__()
        self.gui = QParent
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
        #Diccionario que contiene las conversaciones activas
        #hasta ese momento
        self.chats_dictionary = {}
        self.gui = gui
        self.ip = ip
        self.port = port
        self.frames = []

    """**************************************************
    Metodo que sera llamado cuando un contacto quiera establecer
    conexion con este cliente
    **************************************************"""
    def new_chat_wrapper(self, contact_ip, contact_port, username):
        #Un cliente mando a llamar a esta instancia, crea una ventana de
        #chat para automaticamente
        #TODO

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para regresar el texto
    ************************************************** """
    def echo(self, message):
        #TODO

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

    def incommingCall_wrapper(self, calling):
        print 'Establishing audio call connection...'
        self.gui.calling = calling
        self.gui.emit(QtCore.SIGNAL('llamadaEmpezada(bool)'), calling)
        return 'ok.'

    def playAudio(self, audio):
        self.p = pyaudio.PyAudio()
        FORMAT = self.p.get_format_from_width(2)
        self.stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             output=True,
                             frames_per_buffer=CHUNK)
        self.stream.write(audio.data)
        # self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        print 'lel'
        return 'ok.'

    def playAudio_wrapper(self, audio):
        '''
        Receives and plays audio
        '''
        self.gui.emit(QtCore.SIGNAL("audioRecibidio(bytes)"), audio)
        print 'Audio received'
        self.audio_player = Thread(target=self.playAudio,
                                   args=(audio,))
        self.audio_player.setDaemon(True)
        self.audio_player.start()

    def toArray(self, s):
	f = StringIO(s)
	arr = np.lib.format.read_array(f)
	return arr

    def playVideo_wrapper(self, video):
        self.frames.append(self.toArray(video.data))
        video_displayer = Thread(target=self.display_video)
        video_displayer.setDaemon(True)
        video_displayer.start()
        return 'ACK.'

    def display_video(self):
        video_player = Thread(target=self.show_video)
	video_player.setDaemon(True)
	video_player.start()

    def show_video(self):
        while True:
            if len(self.frames) > 0:
                print 'displaying video...\n'
		cv2.imshow('VideoChat', self.frames.pop(0))
	cv2.destroyAllWindows()
