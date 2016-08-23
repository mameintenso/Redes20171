import sys
import socket

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

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
        self.responder.resize(140,80)
        self.connect(self.responder, QtCore.SIGNAL("clicked()"), self.responderclick)

        #Ventana principal
        self.setGeometry(300,300,840,680)
        self.setFixedSize(840,680)
        self.setWindowTitle("Chat")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def responderclick(self):
        # send message
        self.channel.api_client.send_message(self.box.text())

        self.update_chat('\nyou say: ', self.box.text(), self.local_ip, self.local_port)
        self.box.clear()

    def update_chat(self, header, message, ip, port):
        # update chat history
        self.chat_history = header + message
        self.historial.append(self.chat_history)
