#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QLabel

from Constants.Constants import *
from Code.Calculator import *
from Code.DataBase import *
from .CalcGui import *

class Welcome(QtGui.QWidget):
    """
    Implements the first view
    """
    def __init__(self):
        super(Welcome, self).__init__()
        self.initGUI()

    def initGUI(self):
        # log in button
        login = QtGui.QPushButton('Ingresar')
        login.clicked.connect(lambda: self.access(True))

        # sign in button
        signin = QtGui.QPushButton('Registrarse')
        signin.clicked.connect(lambda: self.access(False))

        grid = QtGui.QGridLayout()
        grid.addWidget(login, 0, 0)
        grid.addWidget(signin, 1, 0)

        # final setups
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Bienvenido(a)')
        self.show()

    def access(self, login):
        self.close()
        if login:
            login_window = Login()
        else:
            signin_window = Signin()


class SelectCalc(QtGui.QWidget):
    """
    Implements a view to select a calculator
    """
    def __init__(self):
        super(SelectCalc, self).__init__()
        self.initGUI()

    def initGUI(self):
        # simple calculator button
        simple = QtGui.QPushButton('Calculadora Simple')
        simple.clicked.connect(lambda: self.access(True))

        # advanced calculator button
        advanced = QtGui.QPushButton('Calculadora Avanzada')
        advanced.clicked.connect(lambda: self.access(False))

        grid = QtGui.QGridLayout()
        grid.addWidget(simple, 0, 0)
        grid.addWidget(advanced, 1, 0)

        # final setups
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Seleccione la calculadora que desea utilizar')
        self.show()

    def access(self, simple):
        self.close()
        if simple:
            simple_window = SimpleCalcGui()
        else:
            advanced_window = AdvancedCalcGui()


class Signin(QtGui.QWidget):

    def __init__(self):
        super(Signin, self).__init__()
        self.initGUI()

    def initGUI(self):
        # username
        username = QtGui.QLabel('Nombre de usuario', self)
        username_widget = QtGui.QLineEdit(self)

        # password
        password = QtGui.QLabel('Contraseña', self)
        password_widget = QtGui.QLineEdit(self)
        password_widget.setEchoMode(QtGui.QLineEdit.Password)
        password_widget.show()

        signin_button = QtGui.QPushButton('Registrarse')
        signin_button.clicked.connect(lambda: self.access(username_widget.text(),
                                                          password_widget.text()))

        # position of the credentials in the GUI
        grid = QtGui.QGridLayout()
        grid.addWidget(username, 0, 0)
        grid.addWidget(username_widget, 0, 1)
        grid.addWidget(password, 1, 0)
        grid.addWidget(password_widget, 1, 1)
        grid.addWidget(signin_button, 2, 2)

        # final setups
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Darse de Alta')
        self.show()

    def error_box(self, label):
        """
        Displays an error box
        """
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(label)
        msg.setWindowTitle("Error Fatal")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        retval = msg.exec_()

    def access(self, username=None, password=None):
        db = decrypt_file()

        try:
            encrypt_word(username)
            encrypt_word(password)
        except IndexError:
            self.error_box('Sólo se permiten carácteres alfanuméricos.')
        if username in db.keys():
            # display a message box indicating an error
            self.error_box('El nombre de usuario introducido ya existe.')
        else:
            encrypt_file({username : password})
            self.close()
            self.calc = SelectCalc()

class Login(QtGui.QWidget):

    def __init__(self):
        super(Login, self).__init__()
        self.initGUI()

    def initGUI(self):
        # username
        username = QtGui.QLabel('Nombre de usuario', self)
        username_widget = QtGui.QLineEdit(self)

        # password
        password = QtGui.QLabel('Contraseña', self)
        password_widget = QtGui.QLineEdit(self)
        password_widget.setEchoMode(QtGui.QLineEdit.Password)
        password_widget.show()

        login_button = QtGui.QPushButton('Ingresar')
        login_button.clicked.connect(lambda: self.access(username_widget.text(),
                                                         password_widget.text()))

        # position of the credentials in the GUI
        grid = QtGui.QGridLayout()
        grid.addWidget(username, 0, 0)
        grid.addWidget(username_widget, 0, 1)
        grid.addWidget(password, 1, 0)
        grid.addWidget(password_widget, 1, 1)
        grid.addWidget(login_button, 2, 2)

        # final setups
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Iniciar Sesión')
        self.show()

    def error_box(self, label):
        """
        Displays an error box
        """
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(label)
        msg.setWindowTitle("Error Fatal")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        retval = msg.exec_()

    def access(self, username=None, password=None):
        db = decrypt_file()
        try:
            if username in db.keys() and password == db[username]:
                self.close()
                self.calc = SelectCalc()
            else:
                # display a message box indicating an error
                self.error_box('Sus datos son inválidos.')
        except IndexError:
            # display a message box indicating an error
            self.error_box('Su entrada sólo puede contener carácteres alfanuméricos.')
