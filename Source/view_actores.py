#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ventana_actores import Ui_MainWindow
import view_form_actor
import view_peliculas
import controller

class Form(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_signals()
		self.first_time = True
		self.load_data()
	
	def set_signals(self):
		"""
		Función que conecta señales a las acciones dentro de la interfaz
		del programa.
		"""
		self.ui.menu_peliculas.triggered.connect(self.show_peliculas)
		self.ui.boton_editar.clicked.connect(self.show_edit_actor)
		self.ui.boton_add.clicked.connect(self.show_add_actor)
		self.ui.boton_delete.clicked.connect(self.delete_actor)
		self.ui.lista_act.currentItemChanged.connect(self.change_info)
		self.ui.search_actor.returnPressed.connect(self.load_data)

	def load_data(self):
		"""
		Carga los datos de la base de datos en la lista de la interfaz,
		tambien carga ciertos elementos dependiendo del criterio de
		busqueda y que se buscó.
		Se llama al inicio y cada vez que se se presiona Enter en la barra
		de busqueda.
		"""
		self.ui.lista_act.clear()
		
		if (self.ui.search_actor.text()==""):
			data = controller.get_actor_table()
		elif (self.ui.combo_filtro.currentIndex()==0):
			data = controller.search_actor_name(self.ui.search_actor.text())
		elif (self.ui.combo_filtro.currentIndex()==1):
			data = controller.search_actor_sex(self.ui.search_actor.text())
		
		for row in data:
			self.ui.lista_act.addItem(row[1])

	def change_info(self):
		"""
		Metodo que carga la informacion del elemento seleccionado en la
		lista, es llamado cada vez que hay un cambio en la seleccion de
		la lista de actores.
		"""
		try:
			newName = self.ui.lista_act.currentItem().text()
			newData = controller.search_data_act(newName)
			newData = newData[0]
			nombre = newData[1]
			year = newData[2]
			genero = newData[3]
			img = newData[4]
		except AttributeError as e:
			nombre = ""
			genero = ""
			year = ""
			img = ""

		self.ui.txt_nombre.setText(nombre)
		self.ui.txt_year.setText(year)
		self.ui.txt_genero.setText(genero)
		self.ui.img.setPixmap(QtGui.QPixmap(img))

	def show_peliculas(self):
		"""
		Abre la ventana de peliculas y cierra la ventana de actores, esta
		ubicada en el menu superior.
		"""
		peliculas = view_peliculas.Form(self)
		self.hide()
		peliculas.show()
		
	def show_edit_actor(self):
		"""
		Abre el formulario para agregar/editar informacion de actores,
		para editar informacion de la pelicula seleccionada. Al precionar
		el boton "Editar".
		"""
		try:
			nombre = self.ui.lista_act.currentItem().text()
			formulario = view_form_actor.Form(self)
			formulario.edit(nombre)
			formulario.exec_()
			self.load_data()
		except AttributeError as e:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un actor")
		
	def show_add_actor(self):
		"""
		Abre el formulario para agregar/editar actores, abre la ventana
		vacia para agregar informacion nueva. Al precionar el boton "+".
		"""
		formulario = view_form_actor.Form(self)
		formulario.exec_()
		self.load_data()
		print "show add (P)"
	
	def delete_actor(self):
		"""
		Borra el actor seleccionada actualmente. Al precionar el boton "-".
		"""
		if(self.ui.lista_act.currentItem()):
			msgBox = QtGui.QMessageBox.question(self, "Borrar registro","¿Estas seguro de eliminar esta columna?",
												QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
			if msgBox == QtGui.QMessageBox.Yes:
				name = self.ui.lista_act.currentItem().text()
				controller.delete_actor(name)
				self.load_data()
			else:
				return False
		else:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un elemento")
			return False
		print "Deleted"
