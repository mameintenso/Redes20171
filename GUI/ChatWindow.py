#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import multiprocessing as mp

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, QMetaObject, Q_ARG, QObject
from PyQt4.QtCore import SIGNAL

from threading import Thread

from Channel.Channels import *
from Constants.AuxiliarFunctions import *
from Constants.Constants import *

class Chat(QtGui.QMainWindow):

    def __init__(self, myname, friendinfo, channel):
        QtGui.QMainWindow.__init__(self)
        self.friendinfo = friendinfo
        self.chat_history = ''

        # channel adjustments
        self.channel = channel
        self.channel.gui = self
        self.channel.api_server.gui = self
        self.channel.api_server.functionWrapper.gui = self
        self.channel.new_connection(myname)

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
        QObject.connect(self.channel.api_server.functionWrapper,
                        QtCore.SIGNAL('message_sent'),
                        self.update_chat,
                        QtCore.Qt.QueuedConnection)

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

        #Ventana principal
        self.setGeometry(300,300,840,680)
        self.setFixedSize(840,680)
        self.setWindowTitle("Conversando con " + self.friendinfo[NAME_CONTACT])
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def responderclick(self):
        self.channel.api_client.send_message(self.box.text())
        self.update_chat('\nusted dice: ', self.box.text())
        self.box.clear()


    def update_chat(self, header, message):
        # update chat history
        self.chat_history = header + message
        self.historial.append(self.chat_history)

    def video_call(self):
        self.video_rec_thread = self.channel.start_video_call()
        self.video_window = VideoWindow(self, self.video_rec_thread)

    def audio_call(self):
        self.update_chat('', '\nLlamada de voz iniciada...')
        self.audio_call_thread = self.channel.start_audio_call()
        if self.audio_call_thread is not None:
            self.audio_call_window = AudioCallWindow(self, self.audio_call_thread)

class VideoWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui, video_thread):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.video_thread = video_thread
        self.initUI()

    def initUI(self):
        self.chat_gui.update_chat('', '\nLlamada de video iniciada...')
        self.stop = QtGui.QPushButton("Terminar", self)
        self.stop.move(50, 20)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.setFixedSize(200, 60)
        self.setWindowTitle('Llamada de video')
        self.show()

    def stop_call(self):
        self.video_thread.stop_video()
        self.chat_gui.update_chat('','\nVideo llamada finalizada...')
        self.close()

class AudioCallWindow(QtGui.QMainWindow):

    def __init__(self, chat_gui, audio_call_thread):
        QtGui.QMainWindow.__init__(self)
        self.chat_gui = chat_gui
        self.audio_call_thread = audio_call_thread
        self.initUI()

    def initUI(self):
        self.stop = QtGui.QPushButton("Detener", self)
        self.stop.move(50, 20)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"), self.stop_call)

        self.setFixedSize(200, 60)
        self.setWindowTitle("Llamada de voz")
        self.show()

    def stop_call(self):
        self.audio_call_thread.stop_call()
        self.chat_gui.update_chat('','\nLlamada de voz finalizada...')
        self.close()
