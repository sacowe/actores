# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_peliculas.ui'
#
# Created: Thu Jun 27 11:42:40 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_peli = QtGui.QLineEdit(self.centralwidget)
        self.search_peli.setGeometry(QtCore.QRect(30, 10, 171, 27))
        self.search_peli.setObjectName("search_peli")
        self.lista_pel = QtGui.QListView(self.centralwidget)
        self.lista_pel.setGeometry(QtCore.QRect(30, 50, 261, 271))
        self.lista_pel.setObjectName("lista_pel")
        self.combo_filtro = QtGui.QComboBox(self.centralwidget)
        self.combo_filtro.setGeometry(QtCore.QRect(210, 10, 81, 27))
        self.combo_filtro.setObjectName("combo_filtro")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.img_view = QtGui.QGraphicsView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(340, 30, 161, 191))
        self.img_view.setObjectName("img_view")
        self.label_nom = QtGui.QLabel(self.centralwidget)
        self.label_nom.setGeometry(QtCore.QRect(400, 240, 121, 17))
        self.label_nom.setText("")
        self.label_nom.setObjectName("label_nom")
        self.text_nom = QtGui.QLabel(self.centralwidget)
        self.text_nom.setGeometry(QtCore.QRect(320, 240, 66, 17))
        self.text_nom.setObjectName("text_nom")
        self.text_yr = QtGui.QLabel(self.centralwidget)
        self.text_yr.setGeometry(QtCore.QRect(320, 260, 66, 17))
        self.text_yr.setObjectName("text_yr")
        self.text_gen = QtGui.QLabel(self.centralwidget)
        self.text_gen.setGeometry(QtCore.QRect(320, 280, 66, 17))
        self.text_gen.setObjectName("text_gen")
        self.text_dir = QtGui.QLabel(self.centralwidget)
        self.text_dir.setGeometry(QtCore.QRect(320, 300, 66, 17))
        self.text_dir.setObjectName("text_dir")
        self.label_nom_2 = QtGui.QLabel(self.centralwidget)
        self.label_nom_2.setGeometry(QtCore.QRect(360, 260, 111, 17))
        self.label_nom_2.setText("")
        self.label_nom_2.setObjectName("label_nom_2")
        self.label_nom_4 = QtGui.QLabel(self.centralwidget)
        self.label_nom_4.setGeometry(QtCore.QRect(380, 280, 121, 17))
        self.label_nom_4.setText("")
        self.label_nom_4.setObjectName("label_nom_4")
        self.label_nom_3 = QtGui.QLabel(self.centralwidget)
        self.label_nom_3.setGeometry(QtCore.QRect(380, 300, 121, 20))
        self.label_nom_3.setText("")
        self.label_nom_3.setObjectName("label_nom_3")
        self.boton_actores = QtGui.QPushButton(self.centralwidget)
        self.boton_actores.setGeometry(QtCore.QRect(360, 330, 98, 27))
        self.boton_actores.setObjectName("boton_actores")
        self.boton_agregar_peli = QtGui.QPushButton(self.centralwidget)
        self.boton_agregar_peli.setGeometry(QtCore.QRect(160, 330, 131, 27))
        self.boton_agregar_peli.setObjectName("boton_agregar_peli")
        self.boton_editar = QtGui.QPushButton(self.centralwidget)
        self.boton_editar.setGeometry(QtCore.QRect(30, 330, 111, 27))
        self.boton_editar.setObjectName("boton_editar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 25))
        self.menubar.setObjectName("menubar")
        self.menu_ver = QtGui.QMenu(self.menubar)
        self.menu_ver.setObjectName("menu_ver")
        MainWindow.setMenuBar(self.menubar)
        self.menu_actores = QtGui.QAction(MainWindow)
        self.menu_actores.setObjectName("menu_actores")
        self.menu_peliculas = QtGui.QAction(MainWindow)
        self.menu_peliculas.setObjectName("menu_peliculas")
        self.menu_ver.addAction(self.menu_actores)
        self.menu_ver.addAction(self.menu_peliculas)
        self.menubar.addAction(self.menu_ver.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.search_peli.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Ingrese nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(0, QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(1, QtGui.QApplication.translate("MainWindow", "Género", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_filtro.setItemText(2, QtGui.QApplication.translate("MainWindow", "Año", None, QtGui.QApplication.UnicodeUTF8))
        self.text_nom.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.text_yr.setText(QtGui.QApplication.translate("MainWindow", "Año:", None, QtGui.QApplication.UnicodeUTF8))
        self.text_gen.setText(QtGui.QApplication.translate("MainWindow", "Género:", None, QtGui.QApplication.UnicodeUTF8))
        self.text_dir.setText(QtGui.QApplication.translate("MainWindow", "Director:", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_actores.setText(QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_agregar_peli.setText(QtGui.QApplication.translate("MainWindow", "Agregar Película", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ver.setTitle(QtGui.QApplication.translate("MainWindow", "Ver...", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_actores.setText(QtGui.QApplication.translate("MainWindow", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_peliculas.setText(QtGui.QApplication.translate("MainWindow", "Actores", None, QtGui.QApplication.UnicodeUTF8))
