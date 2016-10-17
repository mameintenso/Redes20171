#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import socket
import time
import multiprocessing as mp

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, QMetaObject, Q_ARG
from PyQt4.QtCore import SIGNAL

from threading import Thread

from Channel.Channel import *
from Constants.AuxiliarFunctions import *

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

	# chat typing line
        self.box = QtGui.QLineEdit(self)
        self.box.move(20,570)
        self.box.resize(550,80)
        self.box.setTextMargins(15,10,40,20)

        # message history
        self.historial = QtGui.QTextBrowser(self)
        self.historial.setAcceptRichText(True)
        self.historial.resize(790,530)
        self.historial.move(20,20)

        # answer button
        self.responder = QtGui.QPushButton("Enviar", self)
        self.responder.move(590,570)
        self.responder.resize(95,80)
        self.connect(self.responder, QtCore.SIGNAL("clicked()"), self.responderclick)

        # audio call button
        self.acall = QtGui.QPushButton("Audio\nLlamada", self)
        self.acall.move(670, 570)
        self.acall.resize(95, 80)
        self.connect(self.acall, QtCore.SIGNAL("clicked()"), self.audio_call)

        # video call button
        self.vcall = QtGui.QPushButton("Video\nLlamada", self)
        self.vcall.move(750, 570)
        self.vcall.resize(95, 80)
        self.connect(self.vcall, QtCore.SIGNAL("clicked()"), self.video_call)

        # connect signal to open incomming call window
        self.acalling = False
        self.connect(self,
                     QtCore.SIGNAL("llamadaEmpezada(bool)"),
                     self.incomming_audio_call)

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

    def video_call(self):
        self.channel.start_video_call()
        # self.video_window = VideoWindow(self)

    def audio_call(self):
        self.update_chat('', '\nLlamada de voz iniciada...')
        self.audio_call_window = AudioCallWindow(self)

    def incomming_audio_call(self):
        self.update_chat('', '\nLlamada de voz iniciada...')
        self.inc_call_window = IncommingCallWindow(self, self.acalling)


class VideoWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.initUI()

    def initUI(self):
        self.stop = QtGui.QPushButton("Detener", self)
        self.stop.move(50, 20)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.setFixedSize(200, 60)
        self.setWindowTitle('Llamada de video')
        self.show()

    def stop_call(self):
        self.chat_gui.update_chat('','\nVideo llamada finalizada...')
        self.close()


class IncommingCallWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui, calling):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.calling = calling
        self.initUI()

    def initUI(self):
        self.stop = QtGui.QPushButton("Detener", self)
        self.stop.move(50, 20)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.setFixedSize(200, 60)
        self.setWindowTitle("Llamada de voz")

        self.stop_thread = Thread(target=self.stop_call)
        self.stop_thread.start()
        self.show()


    def stop_call(self):
        # while self.calling:
        #     pass
        self.chat_gui.update_chat('','\nLlamada de voz finalizada...')
        self.close()


class AudioCallWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.calling = True
        self.call_thread = MyThread(target=self.chat_gui.channel.start_audio_call,
                                    args=(self.calling,))
        self.initUI()

    def initUI(self):
        self.stop = QtGui.QPushButton("Detener", self)
        self.stop.move(50, 20)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.setFixedSize(200, 60)
        self.setWindowTitle("Llamada de voz")
        self.call_thread.start()
        self.show()


    def stop_call(self):
        self.calling = False
        # if not self.call_thread.is_stop():
        #     print '\n\n\noisadfjioasdjfioasjdfioji\n\n\n'
        #     self.call_thread.join()
        self.chat_gui.update_chat('','\nLlamada de voz finalizada...')
        self.close()
