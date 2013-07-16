#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from formulario_pelicula import Ui_Actor
import controller

class Form(QtGui.QDialog):
	isEdited = False
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Actor()
		self.ui.setupUi(self)
		self.set_signals()
		self.build_combobox()
		
	def set_signals(self):
		"""
		Función que conecta señales a las acciones dentro de la interfaz
		del programa.
		"""
		self.ui.accept.clicked.connect(self.accept_action)
		self.ui.cancel.clicked.connect(self.cancel_action)
		self.ui.btn_plus.clicked.connect(self.add)
		self.ui.btn_minus.clicked.connect(self.delete)
	
	def add(self):
		"""
		Funcion que agrega un actor al reparto de la pelicula, se activa
		al pulsar el boton "+".
		"""
		self.ui.le_descripcion.addItem(self.ui.cb_actores.currentText())
		self.ui.cb_actores.removeItem(self.ui.cb_actores.currentIndex())

	def edit(self,nombre):
		"""
		Funcion que cambia algunas variables y le dice a la aplicacion
		que fue abierta por medio del boton "Editar", por lo que debe
		editar valores de una tabla en vez de agregar un nuevo elemento
		a la tabla.
		"""
		self.isEdited = True
		
		data = controller.search_data_pel(nombre)
		data = data[0]
		self.index = data[0]
		nombre = data[1]
		estreno = data[2]
		director = data[3]
		desc = data[4]

		self.ui.le_nombre.setText(nombre)
		self.ui.le_fecha.setText(estreno)
		self.ui.le_director.setText(director)
		self.ui.te_descripcion.insertPlainText(desc)
		
		actores = controller.actors_from_movie(nombre)
		for i in actores:
			self.ui.le_descripcion.addItem(i[1])
			self.ui.cb_actores.removeItem(self.ui.cb_actores.findText(i[1]))
		
	def delete(self):
		"""
		Quita un actor del reparto, y lo vuelve a agregar al QComboBox.
		Se activa cuando se apreta el boton "-".
		"""
		if(self.ui.le_descripcion.currentItem()):
			self.ui.cb_actores.addItem(self.ui.le_descripcion.currentItem().text())
			self.ui.le_descripcion.takeItem(self.ui.le_descripcion.currentIndex().row())
		else:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un elemento")
			return False
	
	def build_combobox(self):
		"""
		Construye el QComboBox con todos los actores.
		"""
		lista = controller.get_actor_table()		
		for row in lista:
			self.ui.cb_actores.addItem(row[1])
				
	def accept_action(self):
		"""
		Accion que toma la aplicación al precionar el boton "Aceptar".
		Obtiene los nombres en los QLineEdit y los actores en el
		QListWidget y los agrega o edita dependiendo el caso.
		"""
		actores = []
		
		if(self.isEdited):
			controller.clear_relation(self.index)	
			controller.edit_pelicula(self.index,
										self.ui.le_nombre.text(),
										self.ui.le_director.text(),
										self.ui.le_fecha.text(),
										self.ui.te_descripcion.toPlainText())						
		else:
			self.index = controller.add_pelicula(self.ui.le_nombre.text(),
											self.ui.le_director.text(),
											self.ui.le_fecha.text(),
											self.ui.te_descripcion.toPlainText())
			self.index = self.index[0]
			
		for i in xrange(self.ui.le_descripcion.count()):
			actores.append(self.ui.le_descripcion.item(i).text())
		controller.add_relation(self.index,actores)
		self.reject()
		
	def cancel_action(self):
		"""
		Cierra la aplicación sin hacer cambios.
		"""
		self.reject()
		
