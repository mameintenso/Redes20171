import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

renglonhistorial = "" 

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
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

		#Botón para responder
		self.responder = QtGui.QPushButton("Enviar", self)
		self.responder.move(670,570)
		self.responder.resize(140,80)
		self.connect(self.responder, SIGNAL("clicked()"),self.responderclick)
		

		#Historial de mensajes.
		self.historial = QtGui.QTextBrowser(self)
		self.historial.setAcceptRichText(True)
		self.historial.resize(790,530)
		self.historial.move(20,20)

		#Ventana principal
		self.setGeometry(300,300,840,680)
		self.setFixedSize(840,680)
		self.setWindowTitle("Chat")
		self.setWindowIcon(QtGui.QIcon(""))
		self.show()

		#Señales
	def responderclick():
		textoenviado = self.box.text()
		self.historial.setText(textoenviado)

def main():
	app = QtGui.QApplication(sys.argv)
	main= Main()
	main.show()
 
	sys.exit(app.exec_())
 
if __name__ == "__main__":
	main()
