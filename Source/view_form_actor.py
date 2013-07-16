#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from formulario_actor import Ui_Actor
import controller

class Form(QtGui.QDialog):
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Actor()
		self.ui.setupUi(self)

	def edit(self,nombre):
		data = controller.search_data_act(nombre)
		data = data[0]
		nombre_ = data[1]
		birth = data[2]
		genero = data[3]
		imagen = data[4]

		self.ui.le_nombre.setText(nombre_)
		self.ui.le_birth.setText(birth)
		self.ui.img.setPixmap(QtGui.QPixmap(imagen))

	
