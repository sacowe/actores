#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ventana_actores import Ui_MainWindow
import crearDB
import view_form_actor
import view_peliculas

class Form(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui =  Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_signals()
	
	def set_signals(self):
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.no)
		self.ui.menu_peliculas.triggered.connect(self.show_peliculas)
		self.ui.boton_editar.clicked.connect(self.show_edit_actor)
		self.ui.boton_add.clicked.connect(self.show_add_actor)
		self.ui.boton_delete.clicked.connect(self.delete_actor)

	def open_actor(self):
		print "open actor"
		
	def show_peliculas(self):
		peliculas = view_peliculas.Form(self)
		self.hide()
		peliculas.show()
				
		print "show peliculas"
		
	def show_edit_actor(self):
		formulario = view_form_actor.Form(self)
		formulario.exec_()
		print "Opening..."
		
	def show_add_actor(self):
		print "show add (P)"
	
	def delete_actor(self):
		print "Deleted"
		
	def no(self):
		print "Nothing should happen"

	def populate(self):
		print "populando..."
		
