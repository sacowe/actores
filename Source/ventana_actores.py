# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_actores.ui'
#
# Created: Tue Jul 16 23:07:14 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_actor = QtGui.QLineEdit(self.centralwidget)
        self.search_actor.setGeometry(QtCore.QRect(30, 10, 161, 27))
        self.search_actor.setObjectName("search_actor")
        self.combo_filtro = QtGui.QComboBox(self.centralwidget)
        self.combo_filtro.setGeometry(QtCore.QRect(200, 10, 91, 27))
        self.combo_filtro.setObjectName("combo_filtro")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.txt_nombre = QtGui.QLabel(self.centralwidget)
        self.txt_nombre.setGeometry(QtCore.QRect(380, 220, 281, 16))
        self.txt_nombre.setText("")
        self.txt_nombre.setObjectName("txt_nombre")
        self.lb_nombre = QtGui.QLabel(self.centralwidget)
        self.lb_nombre.setGeometry(QtCore.QRect(310, 220, 66, 17))
        self.lb_nombre.setObjectName("lb_nombre")
        self.lb_genero = QtGui.QLabel(self.centralwidget)
        self.lb_genero.setGeometry(QtCore.QRect(310, 260, 66, 17))
        self.lb_genero.setObjectName("lb_genero")
        self.lb_year = QtGui.QLabel(self.centralwidget)
        self.lb_year.setGeometry(QtCore.QRect(310, 240, 81, 17))
        self.lb_year.setObjectName("lb_year")
        self.txt_year = QtGui.QLabel(self.centralwidget)
        self.txt_year.setGeometry(QtCore.QRect(400, 240, 101, 17))
        self.txt_year.setText("")
        self.txt_year.setObjectName("txt_year")
        self.boton_add = QtGui.QPushButton(self.centralwidget)
        self.boton_add.setGeometry(QtCore.QRect(220, 330, 31, 27))
        self.boton_add.setObjectName("boton_add")
        self.boton_editar = QtGui.QPushButton(self.centralwidget)
        self.boton_editar.setGeometry(QtCore.QRect(30, 330, 111, 27))
        self.boton_editar.setObjectName("boton_editar")
        self.boton_delete = QtGui.QPushButton(self.centralwidget)
        self.boton_delete.setGeometry(QtCore.QRect(260, 330, 31, 27))
        self.boton_delete.setObjectName("boton_delete")
        self.lista_act = QtGui.QListWidget(self.centralwidget)
        self.lista_act.setGeometry(QtCore.QRect(30, 50, 256, 271))
        self.lista_act.setObjectName("lista_act")
        self.txt_genero = QtGui.QLabel(self.centralwidget)
        self.txt_genero.setGeometry(QtCore.QRect(370, 260, 101, 17))
        self.txt_genero.setText("")
        self.txt_genero.setObjectName("txt_genero")
        self.img = QtGui.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(330, 10, 161, 191))
        self.img.setText("")
        self.img.setScaledContents(False)
        self.img.setObjectName("img")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 25))
        self.menubar.setObjectName("menubar")
        self.menu_ver = QtGui.QMenu(self.menubar)
        self.menu_ver.setObjectName("menu_ver")
        MainWindow.setMenuBar(self.menubar)
        self.menu_peliculas = QtGui.QAction(MainWindow)
        self.menu_peliculas.setObjectName("menu_peliculas")
        self.menu_actor = QtGui.QAction(MainWindow)
        self.menu_actor.setObjectName("menu_actor")
        self.menu_ver.addAction(self.menu_peliculas)
        self.menu_ver.addAction(self.menu_actor)
        self.menubar.addAction(self.menu_ver.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.search_actor.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Ingrese nombre...", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(0, QtGui.QApplication.translate("MainWindow", "Actor", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(1, QtGui.QApplication.translate("MainWindow", "Género", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_genero.setText(QtGui.QApplication.translate("MainWindow", "Genero:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_year.setText(QtGui.QApplication.translate("MainWindow", "Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_add.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_delete.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ver.setTitle(QtGui.QApplication.translate("MainWindow", "Ver...", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_peliculas.setText(QtGui.QApplication.translate("MainWindow", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_actor.setText(QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))

