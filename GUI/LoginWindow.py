#GUI LOGIN.
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.initUI()
 
	def initUI(self):
		self.label1 = QtGui.QLabel('¿Cuál es mi puerto', self)
		self.label1.move(20,45)

		self.line = QtGui.QLineEdit(self)
		self.line.move(20,70)
		self.line.setReadOnly(True)
		self.line.setAlignment(Qt.AlignLeft)
		self.line.resize(380,45)

		self.label2 = QtGui.QLabel('¿Cuál es el puerto del contacto?:', self)
		self.label2.move(20,180)
		
		self.line = QtGui.QLineEdit(self)
		self.line.move(20,220)
		self.line.setReadOnly(True)
		self.line.setAlignment(Qt.AlignLeft)
		self.line.resize(380,45)

		acceder = QtGui.QPushButton("Acceder",self)
		acceder.move(300,280)
		acceder.resize(80,60)
        

		
		self.setGeometry(300,300,420,350)
		self.setFixedSize(420,350)
		self.setWindowTitle("Login")
		self.setWindowIcon(QtGui.QIcon(""))
		self.show()
def main():
	app = QtGui.QApplication(sys.argv)
	main= Main()
	main.show()
 
	sys.exit(app.exec_())
 
if __name__ == "__main__":
	main()
