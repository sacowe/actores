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
	
	def build_combobox(self):
		data = controller.get_actor_table()
		
		for row in data:
			self.ui.cb_actores.addItem(row[1])
				
	def accept_action(self):
		print "lol"
		
	def cancel_action(self):
		self.reject()
		
