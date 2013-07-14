from PySide import QtGui, QtCore
#import controller
from ventana_peliculas import Ui_MainWindow
import crearDB
import view_form_peli
import view_actores

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
		self.ui.boton_add.clicked.connect(self.show_add_peliculas)
		self.ui.boton_delete.clicked.connect(self.delete_peliculas)
		
	def open_actor(self):
		print "open actor"
		
	def show_actor(self):
		actores = view_actores.Form(self)
		self.hide()
		actores.show()
		
		
		print "show actor"
		
	def show_edit_peliculas(self):
		formulario = view_form_peli.Form(self)
		formulario.exec_()
		print "Opening..."
		
	def show_add_peliculas(self):
		print "show add (P)"
	
	def delete_peliculas(self):
		print "Deleted"
		
	def no(self):
		print "Nothing should happen"

	def populate(self):
		print "populando..."
		
