from PySide import QtGui, QtCore
#import controller
from w_peliculas import Ui_MainWindow
import crearDB

class Form(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_signals()
	
	def set_signals(self):
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.show_actor)
		self.ui.menu_peliculas.triggered.connect(self.no)
		self.ui.boton_editar.clicked.connect(self.show_edit_peliculas)
		self.ui.boton_agregar_peli.clicked.connect(self.show_add_peliculas)
		
	def open_actor(self):
		print "open actor"
		
	def show_actor(self):
		print "show actor"
		
	def show_edit_peliculas(self):
		print "show edit (P)"
		
	def show_add_peliculas(self):
		print "show add (P)"
		
	def no(self):
		print "Nothing should happen"

	def populate(self):
		print "populando..."
		
