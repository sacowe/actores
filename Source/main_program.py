#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import view_peliculas
from PySide import QtGui, QtCore

class Main(QtGui.QMainWindow):
	
	def __init__(self, parent = None):
		super(Main, self).__init__()
		mainwin = view_peliculas.Form(self)
		mainwin.show()

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()



