# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actores_m.ui'
#
# Created: Thu Jul  4 12:11:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_actores_m(object):
    def setupUi(self, actores_m):
        actores_m.setObjectName("actores_m")
        actores_m.resize(644, 432)
        self.centralwidget = QtGui.QWidget(actores_m)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Layout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.Layout_2.setContentsMargins(0, 0, 0, 0)
        self.Layout_2.setObjectName("Layout_2")
        self.boton_agregar1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_agregar1.setObjectName("boton_agregar1")
        self.Layout_2.addWidget(self.boton_agregar1)
        self.boton_eliminar1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_eliminar1.setObjectName("boton_eliminar1")
        self.Layout_2.addWidget(self.boton_eliminar1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 10, 221, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setObjectName("Layout")
        self.foto1 = QtGui.QGraphicsView(self.verticalLayoutWidget)
        self.foto1.setObjectName("foto1")
        self.Layout.addWidget(self.foto1)
        self.boton_editar1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.boton_editar1.setObjectName("boton_editar1")
        self.Layout.addWidget(self.boton_editar1)
        self.Layout_3 = QtGui.QFormLayout()
        self.Layout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.Layout_3.setObjectName("Layout_3")
        self.Nombre = QtGui.QLabel(self.verticalLayoutWidget)
        self.Nombre.setObjectName("Nombre")
        self.Layout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.Nombre)
        self.set_nombre1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_nombre1.setText("")
        self.set_nombre1.setObjectName("set_nombre1")
        self.Layout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.set_nombre1)
        self.Edad = QtGui.QLabel(self.verticalLayoutWidget)
        self.Edad.setObjectName("Edad")
        self.Layout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.Edad)
        self.set_edad1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_edad1.setText("")
        self.set_edad1.setObjectName("set_edad1")
        self.Layout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.set_edad1)
        self.Cumpleanos = QtGui.QLabel(self.verticalLayoutWidget)
        self.Cumpleanos.setObjectName("Cumpleanos")
        self.Layout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.Cumpleanos)
        self.set_cumpleanos1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_cumpleanos1.setText("")
        self.set_cumpleanos1.setObjectName("set_cumpleanos1")
        self.Layout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.set_cumpleanos1)
        self.Layout.addLayout(self.Layout_3)
        self.tabla_actores1 = QtGui.QTableView(self.centralwidget)
        self.tabla_actores1.setGeometry(QtCore.QRect(10, 10, 351, 321))
        self.tabla_actores1.setObjectName("tabla_actores1")
        actores_m.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(actores_m)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 25))
        self.menubar.setObjectName("menubar")
        self.menu_ver = QtGui.QMenu(self.menubar)
        self.menu_ver.setObjectName("menu_ver")
        actores_m.setMenuBar(self.menubar)
        self.menu_actores = QtGui.QAction(actores_m)
        self.menu_actores.setObjectName("menu_actores")
        self.menu_peliculas = QtGui.QAction(actores_m)
        self.menu_peliculas.setObjectName("menu_peliculas")
        self.menu_ver.addAction(self.menu_actores)
        self.menubar.addAction(self.menu_ver.menuAction())

        self.retranslateUi(actores_m)
        QtCore.QMetaObject.connectSlotsByName(actores_m)

    def retranslateUi(self, actores_m):
        actores_m.setWindowTitle(QtGui.QApplication.translate("actores_m", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_agregar1.setText(QtGui.QApplication.translate("actores_m", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_eliminar1.setText(QtGui.QApplication.translate("actores_m", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar1.setText(QtGui.QApplication.translate("actores_m", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.Nombre.setText(QtGui.QApplication.translate("actores_m", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.Edad.setText(QtGui.QApplication.translate("actores_m", "Edad:", None, QtGui.QApplication.UnicodeUTF8))
        self.Cumpleanos.setText(QtGui.QApplication.translate("actores_m", "Cumpleaños:", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ver.setTitle(QtGui.QApplication.translate("actores_m", "Ver...", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_actores.setText(QtGui.QApplication.translate("actores_m", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_peliculas.setText(QtGui.QApplication.translate("actores_m", "Actores", None, QtGui.QApplication.UnicodeUTF8))

