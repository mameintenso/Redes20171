#! /usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import absolute_import

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from GUI.ChatWindow import *
from Channel.DirectoryChannel import *


class LoginOneComputer(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.label1 = QtGui.QLabel('Puerto del servidor de contactos', self)
        self.label1.resize(380,45)
        self.label1.move(20,45)

        self.line = QtGui.QLineEdit(self)
        self.line.move(20,90)
        self.line.resize(380,45)

        self.label2 = QtGui.QLabel('Nombre de usuario', self)
        self.label2.resize(380,45)
        self.label2.move(20,180)

        self.line2 = QtGui.QLineEdit(self)
        self.line2.move(20,220)
        self.line2.resize(380,45)

        self.acceder = QtGui.QPushButton("Acceder", self)
        self.acceder.move(300,280)
        self.acceder.resize(80,60)
        self.connect(self.acceder, QtCore.SIGNAL('clicked()'), self.direct_chat)

        self.setGeometry(300,300,420,350)
        self.setFixedSize(420,350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def direct_chat(self):
        self.directory = Directory_W(direct_port=self.line.text(),
                                     username=self.line2.text())
        self.close()

class LoginTwoComputers(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.label0 = QtGui.QLabel('IP del servidor de contactos', self)
        self.label0.resize(380,45)
        self.label0.move(20,45)

        self.line0 = QtGui.QLineEdit(self)
        self.line0.move(20,90)
        self.line0.resize(380,45)

        self.label2 = QtGui.QLabel('Nombre de usuario', self)
        self.label2.resize(380,45)
        self.label2.move(20,180)

        self.line2 = QtGui.QLineEdit(self)
        self.line2.move(20,220)
        self.line2.resize(380,45)

        self.acceder = QtGui.QPushButton("Acceder",self)
        self.acceder.move(300,280)
        self.acceder.resize(80,60)
        self.connect(self.acceder, QtCore.SIGNAL('clicked()'), self.direct_chat)

        self.setGeometry(300,300,420,350)
        self.setFixedSize(420,350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def direct_chat(self):
        self.directory = Directory_W(direct_ip=self.line0.text(),
                                     username=self.line2.text())
        self.close()


class Directory_W(QtGui.QMainWindow):

    def __init__(self, direct_port=None, direct_ip=None, username=None):
        QtGui.QMainWindow.__init__(self)
        self.direct_port = direct_port
        self.direct_ip = direct_ip
        self.username = username
        self.initUI()

    def initUI(self):
        if self.direct_port:
            self.label0 = QtGui.QLabel('Mi puerto', self)
        else:
            self.label0 = QtGui.QLabel(u'Mi dirección IP', self)
        self.label0.resize(380,45)
        self.label0.move(20,45)

        if self.direct_port:
            self.line0 = QtGui.QLineEdit(self)
        else:
            def_content = QtCore.QString(get_ip_address())
            self.line0 = QtGui.QLineEdit(def_content, self)
        self.line0.move(20,90)
        self.line0.resize(380,45)

        self.acceder = QtGui.QPushButton(u"Iniciar Sesión",self)
        self.acceder.move(300,280)
        self.acceder.resize(125,60)
        self.connect(self.acceder, QtCore.SIGNAL('clicked()'), self.login)

        self.setGeometry(300,300,420,350)
        self.setFixedSize(420,350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def login(self):
        if self.direct_port:
            my_port = int(self.line0.text())
            print 'connecting to server at port ' + self.direct_port + '...'
            self.direct_channel = DirectoryChannel(self,
                                                   directory_port=self.direct_port,
                                                   my_port=my_port,
                                                   username=self.username)
        else:
            my_port = None
            print 'connecting to server with IP ' + self.direct_ip + '...'
            self.direct_channel = DirectoryChannel(self,
                                                   directory_ip=self.direct_ip,
                                                   username=self.username)

        if self.direct_channel.connect():
            print 'connection succeeded!'
        else:
            print 'FATAL ERROR!!'
            self.close()
            sys.exit(-1)
        self.contact_window = ContactWindow(self.direct_channel,
                                            self.username,
                                            my_port)
        self.close()


class ContactWindow(QtGui.QMainWindow):

    def __init__(self, direct_channel, username, my_port):
        QtGui.QMainWindow.__init__(self)
        self.direct_channel = direct_channel
        self.my_port = my_port
        self.username = username
        self.contacts = self.direct_channel.get_contacts()
        print 'contacts:\n' + str(self.contacts)
        self.initUI()

    def initUI(self):
        # list of online contacts
        self.contact_label = QtGui.QLabel('Nombres de usuario', self)
        self.contact_label.resize(380, 45)
        self.contact_label.move(10, 10)
        self.contact_widget = QtGui.QListWidget(self)
        self.contact_widget.resize(380, 450)
        self.contact_widget.move(10, 65)
        for user in self.contacts.keys():
            self.contact_widget.addItem(str(user))
        self.contact_widget.itemClicked.connect(self.clicked_contact)

        # widgets for information visualization
        self.cont_ip_label = QtGui.QLabel(u'Dirección IP del contacto seleccionado', self)
        self.cont_ip_label.resize(380, 45)
        self.cont_ip_label.move(455, 10)

        self.cont_ip_line = QtGui.QLineEdit(self)
        self.cont_ip_line.setReadOnly(True)
        self.cont_ip_line.resize(380, 45)
        self.cont_ip_line.move(455, 65)

        self.cont_port_label = QtGui.QLabel(u'Puerto del contacto seleccionado',
                                            self)
        self.cont_port_label.resize(380, 45)
        self.cont_port_label.move(455, 150)

        self.cont_port_line = QtGui.QLineEdit(self)
        self.cont_port_line.setReadOnly(True)
        self.cont_port_line.resize(380, 45)
        self.cont_port_line.move(455, 205)

        # chat button
        self.start_chat = QtGui.QPushButton("Conversar", self)
        self.start_chat.move(570, 400)
        self.start_chat.resize(95, 80)
        self.connect(self.start_chat,
                     QtCore.SIGNAL("clicked()"), self.start_my_chat)

        # reload contacts button
        self.update = QtGui.QPushButton("Actualizar\ncontactos", self)
        self.update.move(670, 400)
        self.update.resize(95, 80)
        self.connect(self.update, QtCore.SIGNAL("clicked()"), self.update_list)

        # logout
        self.logout_button = QtGui.QPushButton(u"Cerrar sesión", self)
        self.logout_button.move(570, 570)
        self.logout_button.resize(190, 80)
        self.connect(self.logout_button, QtCore.SIGNAL("clicked()"), self.logout)

        self.setGeometry(300, 300, 840, 680)
        self.setFixedSize(840, 680)
        self.setWindowTitle(u"Lista de contactos en línea")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def start_my_chat(self):
        # start my own chat GUI
        if self.contact:
            if self.my_port:
                # initialize request channel
                self.req_channel = RequestChannel(self,
                                                  str(self.my_port),
                                                  contact_ip=str(self.cont_ip_line.text()),
                                                  contact_port=str(self.cont_port_line.text()),
                                                  server=self.direct_channel.get_api_server())
                self.chat = Chat(openfriendgui=True,
                                 myname=self.username,
                                 friendname=self.contact,
                                 channel=self.req_channel)
            else:
                # initialize request channel
                self.req_channel = RequestChannel(self,
                                                  str(CHAT_PORT),
                                                  contact_ip=str(self.cont_ip_line.text()),
                                                  contact_port=str(self.cont_port_line.text()),
                                                  server=self.direct_channel.get_api_server())
                self.chat = Chat(openfriendgui=True,
                                 friendname=self.contact,
                                 myname=self.username,
                                 channel=self.req_channel)

    def clicked_contact(self, item):
        self.contact = str(item.text())
        ip = QtCore.QString(self.contacts[self.contact][IP_CONTACT])
        port = QtCore.QString(self.contacts[self.contact][PORT_CONTACT])
        self.cont_ip_line.setText(ip)
        self.cont_port_line.setText(port)

    def update_list(self):
        print 'updating contact list...'
        self.contacts = self.direct_channel.get_contacts()
        print 'contacts:\n' + str(self.contacts)
        self.contact_widget.clear()
        for user in self.contacts.keys():
            self.contact_widget.addItem(str(user))
        self.contact_widget.itemClicked.connect(self.clicked_contact)

    def logout(self):
        print 'logging out...'
        self.direct_channel.disconnect()
        print 'BYE!'
        self.close()
        sys.exit(0)
