from PySide import QtGui, QtCore
#import controller
from w_peliculas import Ui_MainWindow

class Form(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_signals()
	
	def set_signals(self):
		self.ui.menu_peliculas.clicked.connect(self.change_to_actor())
		
	def change_to_actor(self):
		print "lol"
		
