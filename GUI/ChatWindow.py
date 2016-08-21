#WindowGUI
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.initUI()

	def initUI(self):

		self.textbox = QtGui.QLabel(self)
		box = QtGui.QLineEdit(self)
		box.move(20,570)
		box.resize(630,80)

		responder = QtGui.QPushButton("Responder",self)
		responder.move(670,570)
		responder.resize(140,80)
        
		









		self.setGeometry(300,300,840,680)
		self.setFixedSize(840,680)
		self.setWindowTitle("Chat")
		self.setWindowIcon(QtGui.QIcon(""))
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	main= Main()
	main.show()
 
	sys.exit(app.exec_())
 
if __name__ == "__main__":
	main()
