#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import socket
import time

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

from threading import Thread

from Channel.Channel import *

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

class Chat(QtGui.QMainWindow):

    def __init__(self, local, local_port, cont_ip, cont_port):
        QtGui.QMainWindow.__init__(self)

        self.chat_history = ''

        # setup port and IP variables
        self.local = local
        if local:
            self.local_ip = 'localhost'
            self.contact_port = cont_port
            self.contact_ip='localhost'
        else:
            self.local_ip = get_local_ip()
            self.contact_port = cont_port
            self.contact_ip = cont_ip
        self.local_port = local_port

        # initialize channel
        self.channel = Channel(self.local_ip,
                               self.local_port,
                               self.contact_ip,
                               self.contact_port,
                               self)

        # initialize interface
        self.initUI()

    def initUI(self):
        self.textbox = QtGui.QLabel(self)
        self.textbox.move(15,15)
        self.textbox.resize(730,600)

	#Línea donde se escribe
        self.box = QtGui.QLineEdit(self)
        self.box.move(20,570)
        self.box.resize(630,80)
        self.box.setTextMargins(15,10,40,20)

        #Historial de mensajes.
        self.historial = QtGui.QTextBrowser(self)
        self.historial.setAcceptRichText(True)
        self.historial.resize(790,530)
        self.historial.move(20,20)

        #Botón para responder
        self.responder = QtGui.QPushButton("Enviar", self)
        self.responder.move(670,570)
        self.responder.resize(95,80)
        self.connect(self.responder, QtCore.SIGNAL("clicked()"), self.responderclick)

        # button to start an audio call
        self.call = QtGui.QPushButton("Llamar", self)
        self.call.move(750, 570)
        self.call.resize(95, 80)
        self.connect(self.call, QtCore.SIGNAL("clicked()"), self.audio_call)

        #Ventana principal
        self.setGeometry(300,300,840,680)
        self.setFixedSize(840,680)
        self.setWindowTitle("Chat")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def responderclick(self):
        # send message
        self.channel.api_client.send_message(self.box.text())

        self.update_chat('\nyou say: ', self.box.text())
        self.box.clear()

    def update_chat(self, header, message):
        # update chat history
        self.chat_history = header + message
        self.historial.append(self.chat_history)

    def audio_call(self):
        self.update_chat('', '\nLlamada de voz iniciada...')
        # msg = QtGui.QMessageBox(self)
        # msg.setText('Llamada en curso...')
        # msg.setStandardButtons(QtGui.QMessageBox.Cancel)
        # code = msg.exec_()
        # print 'Starting call ' + str(code)
        # self.channel.start_audio_call()
        self.audio_call_window = AudioCallWindow(self)

    def incomming_audio_call(self):
        print 'ioasdfjosd'
        # self.emit(QtCore.SIGNAL("audioCall()"), AudioCallWindow(self))
        print 'lelelele'
        self.update_chat('', '\nLlamada de voz iniciada...')
        # self.inc_call_window = AudioCallWindow(self)

class AudioCallWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.initUI()

    def initUI(self):
        self.textbox = QtGui.QLabel(self)
        self.textbox.move(15,15)
        self.textbox.resize(730,600)

        self.stop = QtGui.QPushButton("Detener", self)
        self.stop.move(750, 570)
        self.stop.resize(95, 80)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.chat_gui.channel.start_audio_call()
        self.show()
        # self.setText('Llamada de voz en curso')
        # self.setStandardButtons(QtGui.QMessageBox.Cancel)
        # code = self.exec_()
        # print 'Starting call ' + str(code)

    def stop_call(self):
        self.chat_gui.update_chat('','\nLlamada de voz finalizada...')
        self.close()
