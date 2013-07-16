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
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.show_actor)
#		self.ui.menu_peliculas.triggered.connect(self.no)
		self.ui.boton_editar.clicked.connect(self.show_edit_peliculas)
		self.ui.boton_add.clicked.connect(self.show_add_peliculas)
		self.ui.boton_delete.clicked.connect(self.delete_peliculas)
		self.ui.lista_pel.currentItemChanged.connect(self.change_info)
		self.ui.search_peli.returnPressed.connect(self.load_data)

	def change_info(self):
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
		self.ui.txt_nombre.setText(nombre)
		self.ui.txt_director.setText(director)
		self.ui.txt_year.setText(year)
		self.ui.txt_descripcion.setText(descripcion)
		
		self.ui.lista_actores.clear()
		if (nombre != ""):
			data = controller.actors_from_movie(nombre)
			for row in data:
				self.ui.lista_actores.addItem(row[1])
		

	def load_data(self):
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
		print "open actor"
		
	def show_actor(self):
		self.actores = view_actores.Form(self)
		self.hide()
		self.actores.show()
		
	def show_edit_peliculas(self):
		formulario = view_form_peli.Form(self)
		formulario.exec_()
		
	def show_add_peliculas(self):
		formulario = view_form_peli.Form(self)
		formulario.exec_()
	
	def delete_peliculas(self):
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

	def populate(self):
		print "populando..."
		
