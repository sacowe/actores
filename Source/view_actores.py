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
		self.ui.boton_actores.clicked.connect(self.open_actor)
		self.ui.menu_actor.triggered.connect(self.no)
		self.ui.menu_peliculas.triggered.connect(self.show_peliculas)
		self.ui.boton_editar.clicked.connect(self.show_edit_actor)
		self.ui.boton_add.clicked.connect(self.show_add_actor)
		self.ui.boton_delete.clicked.connect(self.delete_actor)
		self.ui.lista_act.currentItemChanged.connect(self.change_info)

	def load_data(self):
		if self.first_time:
			data = controller.get_actor_table()
			self.first_time = False
		else:
			print "else"
		
		r = 0
		for row in data:
			self.ui.lista_act.addItem(row[1])
			r = r+1

	def change_info(self):
		newName = self.ui.lista_act.currentItem().text()
		newData = controller.search_data_act(newName)
		newData = newData[0]
		nombre = newData[1]
		year = newData[2]
		genero = newData[3]

		self.ui.txt_nombre.setText(nombre)
		self.ui.txt_year.setText(year)
		self.ui.txt_genero.setText(genero)
		self.ui.img.setPixmap(QtGui.QPixmap(newData[4]))

	def open_actor(self):
		print "open_actor"
		
	def show_peliculas(self):
		peliculas = view_peliculas.Form(self)
		self.hide()
		peliculas.show()

		print "show peliculas"
		
	def show_edit_actor(self):
		nombre = self.ui.lista_act.currentItem().text()
		formulario = view_form_actor.Form(self)
		formulario.edit(nombre)
		formulario.exec_()
		#except AttributeError as e:
		#	errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar un actor")
		
	def show_add_actor(self):
		print "show add (P)"
	
	def delete_actor(self):
		print "Deleted"
		
	def no(self):
		print "Nothing should happen"

	def populate(self):
		print "populando..."
		
