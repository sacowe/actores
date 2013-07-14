#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from formulario_pelicula import Ui_Actor

class Form(QtGui.QDialog):
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Actor()
		self.ui.setupUi(self)

	
