#!/usr/bin/python
# -*- coding: utf-8 -*-

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
		self.load_data()
	
	def set_signals(self):
		"""
		Función que conecta señales a las acciones dentro de la interfaz
		del programa.
		"""
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.show_actor)
		self.ui.boton_editar.clicked.connect(self.show_edit_peliculas)
		self.ui.boton_add.clicked.connect(self.show_add_peliculas)
		self.ui.boton_delete.clicked.connect(self.delete_peliculas)
		self.ui.lista_pel.currentItemChanged.connect(self.change_info)
		self.ui.search_peli.returnPressed.connect(self.load_data)

	def change_info(self):
		"""
		Metodo que carga la informacion del elemento seleccionado en la
		lista, es llamado cada vez que hay un cambio en la seleccion de
		la lista de peliculas.
		"""
		try:
			newName = self.ui.lista_pel.currentItem().text()
			newData = controller.search_data_pel(newName)
			newData = newData[0]
			nombre = newData[1]
			director = newData[3]
			year = newData[2]
			descripcion = newData[4]
		except AttributeError as e:
			nombre = ""
			director = ""
			year = ""
			descripcion = ""

		self.ui.txt_nombre.setText(str(nombre))
		self.ui.txt_director.setText(str(director))
		self.ui.txt_year.setText(str(year))
		self.ui.txt_descripcion.setText(str(descripcion))
		
		self.ui.lista_actores.clear()

		if (nombre != ""):
			data = controller.actors_from_movie(nombre)
			for row in data:
				self.ui.lista_actores.addItem(row[1])
		

	def load_data(self):
		"""
		Carga los datos de la base de datos en la lista de la interfaz,
		tambien carga ciertos elementos dependiendo del criterio de
		busqueda y que se buscó.
		Se llama al inicio y cada vez que se se presiona Enter en la barra
		de busqueda.
		"""
		self.ui.lista_pel.clear()
		
		if (self.ui.search_peli.text()==""):
			data = controller.get_peliculas_table()
		elif (self.ui.combo_filtro.currentIndex()==0):
			data = controller.search_peliculas_name(self.ui.search_peli.text())
		elif (self.ui.combo_filtro.currentIndex()==1):
			data = controller.search_peliculas_direc(self.ui.search_peli.text())
		elif (self.ui.combo_filtro.currentIndex()==2):
			data = controller.search_peliculas_year(self.ui.search_peli.text())

		for row in data:
			self.ui.lista_pel.addItem(row[1])
		
	def open_actor(self):
		"""
		Abre la ventana que muestra la informacíon por actores, con el
		nombre de la pelicula en el buscador para filtrar solo los actores
		que salen en la pelicula seleccionada.
		Se activa al pulsar un boton.
		"""
		try:
			nombre = self.ui.lista_actores.currentItem().text()
			self.actores = view_actores.Form(self)
			self.hide()
			self.actores.show()
			self.actores.ui.search_peli.setText(nombre)
		except AttributeError as e:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un actor del reparto")
				
	def show_actor(self):
		"""
		Abre la ventana de actores y cierra la ventana de peliculas, esta
		ubicada en el menu superior.
		"""
		self.actores = view_actores.Form(self)
		self.hide()
		self.actores.show()
		
	def show_edit_peliculas(self):
		"""
		Abre el formulario para agregar/editar informacion de peliculas,
		para editar informacion de la pelicula seleccionada. Al precionar
		el boton "Editar".
		"""
		nombre = self.ui.lista_pel.currentItem().text()
		formulario = view_form_peli.Form(self)
		formulario.edit(nombre)
		formulario.exec_()
		self.load_data()
		self.change_info()
		#except AttributeError as e:
		#	errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar una pelicula")

	def show_add_peliculas(self):
		"""
		Abre el formulario para agregar/editar peliculas, abre la ventana
		vacia para agregar informacion nueva. Al precionar el boton "+".
		"""
		formulario = view_form_peli.Form(self)
		formulario.exec_()
		self.load_data()
	
	def delete_peliculas(self):
		"""
		Borra la pelicula seleccionada actualmente. Al precionar el boton "-".
		"""
		if(self.ui.lista_pel.currentItem()):
			msgBox = QtGui.QMessageBox.question(self, "Borrar registro","¿Estas seguro de eliminar esta columna?",
												QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
			if msgBox == QtGui.QMessageBox.Yes:
				name = self.ui.lista_pel.currentItem().text()
				controller.delete_peliculas(name)
				self.load_data()
			else:
				return False
		else:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un elemento")
			return False
		
