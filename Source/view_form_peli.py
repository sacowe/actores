#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from formulario_pelicula import Ui_Actor
import controller

class Form(QtGui.QDialog):
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Actor()
		self.ui.setupUi(self)
		self.set_signals()
		self.build_combobox()
		
	def set_signals(self):
		self.ui.accept.clicked.connect(self.accept_action)
		self.ui.cancel.clicked.connect(self.cancel_action)
		self.ui.btn_plus.clicked.connect(self.add)
		self.ui.btn_minus.clicked.connect(self.delete)
	
	def add(self):
		self.ui.le_descripcion.addItem(self.ui.cb_actores.currentText())
		self.ui.cb_actores.removeItem(self.ui.cb_actores.currentIndex())

	def edit(self,nombre):
		data = controller.search_data_pel(nombre)
		data = data[0]
		nombre = data[1]
		estreno = data[2]
		director = data[3]
		desc = data[4]

		self.ui.le_nombre.setText(nombre)
		self.ui.le_fecha.setText(estreno)
		self.ui.le_director.setText(director)
		self.ui.te_descripcion.insertPlainText(desc)

		
	def delete(self):
		if(self.ui.le_descripcion.currentItem()):
			self.ui.cb_actores.addItem(self.ui.le_descripcion.currentItem().text())
			self.ui.le_descripcion.takeItem(self.ui.le_descripcion.currentIndex().row())
		else:
			errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un elemento")
			return False
	
	def build_combobox(self):
		data = controller.get_actor_table()		
		for row in data:
			self.ui.cb_actores.addItem(row[1])
				
	def accept_action(self):
		actores = []
		index = controller.add_pelicula(self.ui.le_nombre.text(),
										self.ui.le_director.text(),
										self.ui.le_fecha.text(),
										self.ui.te_descripcion.toPlainText())
		for i in xrange(self.ui.le_descripcion.count()):
			actores.append(self.ui.le_descripcion.item(i).text())
		controller.add_relation(index,actores)
		self.reject()
		
	def cancel_action(self):
		self.reject()
		
