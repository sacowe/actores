# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actores_h.ui'
#
# Created: Thu Jun 27 12:21:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_actores_h(object):
    def setupUi(self, actores_h):
        actores_h.setObjectName("actores_h")
        actores_h.resize(710, 463)
        self.centralwidget = QtGui.QWidget(actores_h)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 380, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Layout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.Layout_2.setContentsMargins(0, 0, 0, 0)
        self.Layout_2.setObjectName("Layout_2")
        self.boton_agregar2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_agregar2.setObjectName("boton_agregar2")
        self.Layout_2.addWidget(self.boton_agregar2)
        self.boton_eliminar2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_eliminar2.setObjectName("boton_eliminar2")
        self.Layout_2.addWidget(self.boton_eliminar2)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(440, 30, 221, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setObjectName("Layout")
        self.foto2 = QtGui.QGraphicsView(self.verticalLayoutWidget)
        self.foto2.setObjectName("foto2")
        self.Layout.addWidget(self.foto2)
        self.boton_editar2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.boton_editar2.setObjectName("boton_editar2")
        self.Layout.addWidget(self.boton_editar2)
        self.Layout_3 = QtGui.QFormLayout()
        self.Layout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.Layout_3.setObjectName("Layout_3")
        self.Nombre = QtGui.QLabel(self.verticalLayoutWidget)
        self.Nombre.setObjectName("Nombre")
        self.Layout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.Nombre)
        self.set_nombre2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_nombre2.setText("")
        self.set_nombre2.setObjectName("set_nombre2")
        self.Layout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.set_nombre2)
        self.Edad = QtGui.QLabel(self.verticalLayoutWidget)
        self.Edad.setObjectName("Edad")
        self.Layout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.Edad)
        self.set_edad2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_edad2.setText("")
        self.set_edad2.setObjectName("set_edad2")
        self.Layout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.set_edad2)
        self.Cumpleanos = QtGui.QLabel(self.verticalLayoutWidget)
        self.Cumpleanos.setObjectName("Cumpleanos")
        self.Layout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.Cumpleanos)
        self.set_cumpleanos2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.set_cumpleanos2.setText("")
        self.set_cumpleanos2.setObjectName("set_cumpleanos2")
        self.Layout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.set_cumpleanos2)
        self.Layout.addLayout(self.Layout_3)
        self.tabla_actores2 = QtGui.QTableView(self.centralwidget)
        self.tabla_actores2.setGeometry(QtCore.QRect(50, 30, 351, 311))
        self.tabla_actores2.setObjectName("tabla_actores2")
        actores_h.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(actores_h)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 20))
        self.menubar.setObjectName("menubar")
        self.menu_ver = QtGui.QMenu(self.menubar)
        self.menu_ver.setObjectName("menu_ver")
        actores_h.setMenuBar(self.menubar)
        self.menu_actores = QtGui.QAction(actores_h)
        self.menu_actores.setObjectName("menu_actores")
        self.menu_peliculas = QtGui.QAction(actores_h)
        self.menu_peliculas.setObjectName("menu_peliculas")
        self.menubar.addAction(self.menu_ver.menuAction())

        self.retranslateUi(actores_h)
        QtCore.QMetaObject.connectSlotsByName(actores_h)

    def retranslateUi(self, actores_h):
        actores_h.setWindowTitle(QtGui.QApplication.translate("actores_h", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_agregar2.setText(QtGui.QApplication.translate("actores_h", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_eliminar2.setText(QtGui.QApplication.translate("actores_h", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_editar2.setText(QtGui.QApplication.translate("actores_h", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.Nombre.setText(QtGui.QApplication.translate("actores_h", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.Edad.setText(QtGui.QApplication.translate("actores_h", "Edad", None, QtGui.QApplication.UnicodeUTF8))
        self.Cumpleanos.setText(QtGui.QApplication.translate("actores_h", "Cumpleaños", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ver.setTitle(QtGui.QApplication.translate("actores_h", "Ver...", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_actores.setText(QtGui.QApplication.translate("actores_h", "Peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_peliculas.setText(QtGui.QApplication.translate("actores_h", "Actores", None, QtGui.QApplication.UnicodeUTF8))
