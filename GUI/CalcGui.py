import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import Qt
from math import sqrt

from Code.Calculator import *

class SimpleCalcGui(QtGui.QWidget):

    def __init__(self):
        super(SimpleCalcGui, self).__init__()
        self.calculator = SimpleCalculator()
        self.initUI()

    def click(self, symbol):
        if symbol in ['+', '-', '=']:
            self.calculator.enter_op(symbol)
        else:
            self.calculator.enter_digit(symbol)
        self.line.setText(str(self.calculator.curr_screen))

    def initUI(self):
        self.line = QtGui.QLineEdit(self)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMaxLength(15)
        self.line.resize(400, 25)
        self.line.setText(str(self.calculator.curr_screen))

        zero = QtGui.QPushButton("0", self)
        zero.move(10,350)
        zero.resize(95,90)
        zero.clicked.connect(lambda : self.click("0"))

        one = QtGui.QPushButton("1",self)
        one.move(10,250)
        one.resize(95,90)
        one.clicked.connect(lambda : self.click("1"))

        two = QtGui.QPushButton("2",self)
        two.move(110,250)
        two.resize(95,90)
        two.clicked.connect(lambda : self.click("2"))

        three = QtGui.QPushButton("3",self)
        three.move(210,250)
        three.resize(95,90)
        three.clicked.connect(lambda : self.click("3"))

        four = QtGui.QPushButton("4",self)
        four.move(10,150)
        four.resize(95,90)
        four.clicked.connect(lambda : self.click("4"))

        five = QtGui.QPushButton("5",self)
        five.move(110,150)
        five.resize(95,90)
        five.clicked.connect(lambda : self.click("5"))

        six = QtGui.QPushButton("6",self)
        six.move(210,150)
        six.resize(95,90)
        six.clicked.connect(lambda : self.click("6"))

        seven = QtGui.QPushButton("7",self)
        seven.move(10,50)
        seven.resize(95,90)
        seven.clicked.connect(lambda : self.click("7"))

        eight = QtGui.QPushButton("8",self)
        eight.move(110,50)
        eight.resize(95,90)
        eight.clicked.connect(lambda : self.click("8"))

        nine = QtGui.QPushButton("9",self)
        nine.move(210,50)
        nine.resize(95,90)
        nine.clicked.connect(lambda : self.click("9"))

        minus = QtGui.QPushButton("-",self)
        minus.move(310,250)
        minus.resize(95,90)
        minus.clicked.connect(lambda : self.click("-"))

        plus = QtGui.QPushButton("+",self)
        plus.move(310,350)
        plus.resize(95,90)
        plus.clicked.connect(lambda : self.click("+"))

        equal = QtGui.QPushButton("=",self)
        equal.move(210,350)
        equal.resize(95,90)
        equal.clicked.connect(lambda : self.click("="))

        self.setGeometry(300,300,520,480)
        self.setFixedSize(520,480)
        self.setWindowTitle("Calculadora Simple")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()


class AdvancedCalcGui(QtGui.QWidget):

    def __init__(self):
        super(AdvancedCalcGui, self).__init__()
        self.calculator = AdvancedCalculator()
        self.initUI()

    def click(self, symbol):
        if symbol in ['+', '-', '/', '*', '=']:
            self.calculator.enter_op(symbol)
        else:
            self.calculator.enter_digit(symbol)
        self.line.setText(str(self.calculator.curr_screen))

    def initUI(self):
        self.line = QtGui.QLineEdit(self)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMaxLength(15)
        self.line.resize(400, 25)
        self.line.setText(str(self.calculator.curr_screen))

        zero = QtGui.QPushButton("0", self)
        zero.move(10,350)
        zero.resize(95,90)
        zero.clicked.connect(lambda : self.click("0"))

        one = QtGui.QPushButton("1",self)
        one.move(10,250)
        one.resize(95,90)
        one.clicked.connect(lambda : self.click("1"))

        two = QtGui.QPushButton("2",self)
        two.move(110,250)
        two.resize(95,90)
        two.clicked.connect(lambda : self.click("2"))

        three = QtGui.QPushButton("3",self)
        three.move(210,250)
        three.resize(95,90)
        three.clicked.connect(lambda : self.click("3"))

        four = QtGui.QPushButton("4",self)
        four.move(10,150)
        four.resize(95,90)
        four.clicked.connect(lambda : self.click("4"))

        five = QtGui.QPushButton("5",self)
        five.move(110,150)
        five.resize(95,90)
        five.clicked.connect(lambda : self.click("5"))

        six = QtGui.QPushButton("6",self)
        six.move(210,150)
        six.resize(95,90)
        six.clicked.connect(lambda : self.click("6"))

        seven = QtGui.QPushButton("7",self)
        seven.move(10,50)
        seven.resize(95,90)
        seven.clicked.connect(lambda : self.click("7"))

        eight = QtGui.QPushButton("8",self)
        eight.move(110,50)
        eight.resize(95,90)
        eight.clicked.connect(lambda : self.click("8"))

        nine = QtGui.QPushButton("9",self)
        nine.move(210,50)
        nine.resize(95,90)
        nine.clicked.connect(lambda : self.click("9"))

        point = QtGui.QPushButton(".",self)
        point.move(110,350)
        point.resize(95,90)
        point.clicked.connect(lambda : self.click("."))

        div = QtGui.QPushButton("/",self)
        div.move(310,50)
        div.resize(95,90)
        div.clicked.connect(lambda : self.click("/"))

        mult = QtGui.QPushButton("*",self)
        mult.move(310,150)
        mult.resize(95,90)
        mult.clicked.connect(lambda : self.click("*"))

        minus = QtGui.QPushButton("-",self)
        minus.move(310,250)
        minus.resize(95,90)
        minus.clicked.connect(lambda : self.click("-"))

        plus = QtGui.QPushButton("+",self)
        plus.move(310,350)
        plus.resize(95,90)
        plus.clicked.connect(lambda : self.click("+"))

        equal = QtGui.QPushButton("=",self)
        equal.move(210,350)
        equal.resize(95,90)
        equal.clicked.connect(lambda : self.click("="))

        self.setGeometry(300,300,520,480)
        self.setFixedSize(520,480)
        self.setWindowTitle("Calculadora Avanzada")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()
