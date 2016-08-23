#GUI LOGIN.

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from GUI.ChatWindow import *

class LoginOneComputer(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.label1 = QtGui.QLabel('¿Cuál es mi puerto?', self)
        self.label1.resize(380,45)
        self.label1.move(20,45)

        self.line = QtGui.QLineEdit(self)
        self.line.move(20,90)
        self.line.resize(380,45)

        self.label2 = QtGui.QLabel('¿Cuál es el puerto del contacto?', self)
        self.label2.resize(380,45)
        self.label2.move(20,180)

        self.line2 = QtGui.QLineEdit(self)
        self.line2.move(20,220)
        self.line2.resize(380,45)

        self.acceder = QtGui.QPushButton("Acceder", self)
        self.acceder.move(300,280)
        self.acceder.resize(80,60)
        self.connect(self.acceder, QtCore.SIGNAL('clicked()'), self.access_chat)

        self.setGeometry(300,300,420,350)
        self.setFixedSize(420,350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def access_chat(self):
        self.chat = Chat(local=True,
                         local_port=self.line.text(),
                         cont_ip=None,
                         cont_port=self.line2.text())
        self.close()

class LoginTwoComputers(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.label1 = QtGui.QLabel('¿Cuál es la IP del contacto?', self)
        self.label1.resize(380,45)
        self.label1.move(20,45)

        self.line = QtGui.QLineEdit(self)
        self.line.move(20,90)
        self.line.resize(380,45)

        self.acceder = QtGui.QPushButton("Acceder",self)
        self.acceder.move(300,280)
        self.acceder.resize(80,60)
        self.connect(self.acceder, QtCore.SIGNAL('clicked()'), self.access_chat)

        self.setGeometry(300,300,420,350)
        self.setFixedSize(420,350)
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def access_chat(self):
        self.chat = Chat(local=False,
                         local_port='5000',
                         cont_ip=self.line.text(),
                         cont_port='5000')
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    main = LoginTwoComputers()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
