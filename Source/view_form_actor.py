#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from formulario_actor import Ui_Actor
import controller
import shutil

class Form(QtGui.QDialog):
	
	id_act = -1
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Actor()
		self.id_act = -1
		self.ui.setupUi(self)
		self.build_combobox()
		self.set_signals()

	def set_signals(self):
		self.ui.change.clicked.connect(self.change_image)
		self.ui.accept.clicked.connect(self.accept_action)
		self.ui.cancel.clicked.connect(self.cancel_action)

	def edit(self,nombre):
		data = controller.search_data_act(nombre)
		data = data[0]
		nombre_ = data[1]
		birth = data[2]
		genero = data[3]
		self.imagen = data[4]
		self.id_act = data[0]
		
		self.ui.le_nombre.setText(nombre_)
		self.ui.le_birth.setText(birth)
		self.ui.img.setPixmap(QtGui.QPixmap(self.imagen))
		index = self.ui.cb_genero.findText(genero)
		self.ui.cb_genero.setCurrentIndex(index)		

	def change_image(self):
		ventana = QtGui.QFileDialog()
		self.nueva_ruta = ventana.getOpenFileName(self,"Escoga imagen",
		"images/", "Imagenes (*.png *.jpg *.bmp)")
		self.nueva_ruta = self.nueva_ruta[0]
		self.ui.img.setPixmap(QtGui.QPixmap(self.nueva_ruta))

	def guardar_cambios(self):
		#cuando guarda cambios sobreescribe imagen anterior con shutil
		#pendiente: en DB updatear ruta con self.nueva_ruta
		#pendiente: actualizar pixmap en la ventana de actores
		shutil.copy(self.nueva_ruta,self.imagen)

	def build_combobox(self):
		self.ui.cb_genero.addItem("Masculino")
		self.ui.cb_genero.addItem("Femenino")
	
	def accept_action(self):
		if(controller.request_act(self.id_act)):
			controller.edit_actor(self.ui.le_nombre.text(),
			self.ui.le_birth.text(),self.ui.cb_genero.currentText(),
			self.id_act)
		elif(self.id_act<0):
			controller.add_actor(self.ui.le_nombre.text(),
			self.ui.le_birth.text(),self.ui.cb_genero.currentText())
		self.reject()
		
	def cancel_action(self):
		self.reject()
	
