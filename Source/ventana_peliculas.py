# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_peliculas.ui'
#
# Created: Mon Jul 15 14:20:55 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_peli = QtGui.QLineEdit(self.centralwidget)
        self.search_peli.setGeometry(QtCore.QRect(30, 10, 171, 27))
        self.search_peli.setObjectName("search_peli")
        self.combo_filtro = QtGui.QComboBox(self.centralwidget)
        self.combo_filtro.setGeometry(QtCore.QRect(210, 10, 81, 27))
        self.combo_filtro.setObjectName("combo_filtro")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.img_view = QtGui.QGraphicsView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(330, 10, 161, 191))
        self.img_view.setObjectName("img_view")
        self.txt_nombre = QtGui.QLabel(self.centralwidget)
        self.txt_nombre.setGeometry(QtCore.QRect(380, 280, 281, 16))
        self.txt_nombre.setText("")
        self.txt_nombre.setObjectName("txt_nombre")
        self.lb_nombre = QtGui.QLabel(self.centralwidget)
        self.lb_nombre.setGeometry(QtCore.QRect(310, 280, 66, 17))
        self.lb_nombre.setObjectName("lb_nombre")
        self.lb_year = QtGui.QLabel(self.centralwidget)
        self.lb_year.setGeometry(QtCore.QRect(550, 300, 66, 17))
        self.lb_year.setObjectName("lb_year")
        self.lb_director = QtGui.QLabel(self.centralwidget)
        self.lb_director.setGeometry(QtCore.QRect(310, 300, 66, 17))
        self.lb_director.setObjectName("lb_director")
        self.txt_year = QtGui.QLabel(self.centralwidget)
        self.txt_year.setGeometry(QtCore.QRect(590, 300, 61, 17))
        self.txt_year.setText("")
        self.txt_year.setObjectName("txt_year")
        self.txt_director = QtGui.QLabel(self.centralwidget)
        self.txt_director.setGeometry(QtCore.QRect(370, 300, 151, 17))
        self.txt_director.setText("")
        self.txt_director.setObjectName("txt_director")
        self.boton_actores = QtGui.QPushButton(self.centralwidget)
        self.boton_actores.setGeometry(QtCore.QRect(390, 330, 151, 27))
        self.boton_actores.setObjectName("boton_actores")
        self.boton_add = QtGui.QPushButton(self.centralwidget)
        self.boton_add.setGeometry(QtCore.QRect(220, 330, 31, 27))
        self.boton_add.setObjectName("boton_add")
        self.boton_editar = QtGui.QPushButton(self.centralwidget)
        self.boton_editar.setGeometry(QtCore.QRect(30, 330, 111, 27))
        self.boton_editar.setObjectName("boton_editar")
        self.boton_delete = QtGui.QPushButton(self.centralwidget)
        self.boton_delete.setGeometry(QtCore.QRect(260, 330, 31, 27))
        self.boton_delete.setObjectName("boton_delete")
        self.lista_actores = QtGui.QListView(self.centralwidget)
        self.lista_actores.setGeometry(QtCore.QRect(500, 40, 171, 161))
        self.lista_actores.setObjectName("lista_actores")
        self.lb_reparto = QtGui.QLabel(self.centralwidget)
        self.lb_reparto.setGeometry(QtCore.QRect(500, 10, 66, 17))
        self.lb_reparto.setObjectName("lb_reparto")
        self.txt_descripcion = QtGui.QTextEdit(self.centralwidget)
        self.txt_descripcion.setGeometry(QtCore.QRect(330, 210, 341, 61))
        self.txt_descripcion.setReadOnly(True)
        self.txt_descripcion.setObjectName("txt_descripcion")
        self.lista_pel = QtGui.QListWidget(self.centralwidget)
        self.lista_pel.setGeometry(QtCore.QRect(30, 50, 261, 271))
        self.lista_pel.setObjectName("lista_pel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 25))
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
        self.search_peli.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Ingrese nombre...", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(0, QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(1, QtGui.QApplication.translate("MainWindow", "Género", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(2, QtGui.QApplication.translate("MainWindow", "Año", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_year.setText(QtGui.QApplication.translate("MainWindow", "Año:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_director.setText(QtGui.QApplication.translate("MainWindow", "Director:", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_actores.setText(QtGui.QApplication.translate("MainWindow", "Buscar actor", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_add.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_delete.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_reparto.setText(QtGui.QApplication.translate("MainWindow", "Reparto:", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ver.setTitle(QtGui.QApplication.translate("MainWindow", "Ver...", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_peliculas.setText(QtGui.QApplication.translate("MainWindow", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_actor.setText(QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))

