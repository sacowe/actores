from PySide import QtGui, QtCore
import controller
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
		self.first_time = True
		self.load_data()
	
	def set_signals(self):
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.show_actor)
		self.ui.menu_peliculas.triggered.connect(self.no)
		self.ui.boton_editar.clicked.connect(self.show_edit_peliculas)
		self.ui.boton_add.clicked.connect(self.show_add_peliculas)
		self.ui.boton_delete.clicked.connect(self.delete_peliculas)
		self.ui.lista_pel.currentItemChanged.connect(self.change_info)

	def change_info(self):
		newName = self.ui.lista_pel.currentItem().text()
		newData = controller.search_data(newName)
		newData = newData[0]
		nombre = newData[1]
		director = newData[3]
		year = newData[2]
		self.ui.txt_nombre.setText(nombre)
		self.ui.txt_director.setText(director)
		self.ui.txt_year.setText(year)

	def load_data(self):
		if self.first_time:
			data = controller.get_peliculas_table()
			self.first_time = False
		else:
			print "else"
		
		r = 0
		for row in data:
			self.ui.lista_pel.addItem(row[1])
			r = r+1

		

		
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
		
