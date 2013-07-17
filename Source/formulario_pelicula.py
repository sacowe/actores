# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario_pelicula.ui'
#
# Created: Mon Jul 15 22:35:49 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Actor(object):
    def setupUi(self, Actor):
        Actor.setObjectName("Actor")
        Actor.resize(327, 501)
        self.lb_nombre = QtGui.QLabel(Actor)
        self.lb_nombre.setGeometry(QtCore.QRect(30, 20, 59, 17))
        self.lb_nombre.setObjectName("lb_nombre")
        self.lb_birth = QtGui.QLabel(Actor)
        self.lb_birth.setGeometry(QtCore.QRect(30, 50, 43, 17))
        self.lb_birth.setObjectName("lb_birth")
        self.lb_genero = QtGui.QLabel(Actor)
        self.lb_genero.setGeometry(QtCore.QRect(30, 80, 59, 17))
        self.lb_genero.setObjectName("lb_genero")
        self.le_nombre = QtGui.QLineEdit(Actor)
        self.le_nombre.setGeometry(QtCore.QRect(110, 20, 181, 27))
        self.le_nombre.setObjectName("le_nombre")
        self.le_fecha = QtGui.QLineEdit(Actor)
        self.le_fecha.setGeometry(QtCore.QRect(110, 50, 181, 27))
        self.le_fecha.setObjectName("le_fecha")
        self.le_director = QtGui.QLineEdit(Actor)
        self.le_director.setGeometry(QtCore.QRect(110, 80, 181, 27))
        self.le_director.setObjectName("le_director")
        self.te_descripcion = QtGui.QPlainTextEdit(Actor)
        self.te_descripcion.setGeometry(QtCore.QRect(20, 140, 281, 121))
        self.te_descripcion.setObjectName("te_descripcion")
        self.lb_descripcion = QtGui.QLabel(Actor)
        self.lb_descripcion.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.lb_descripcion.setObjectName("lb_descripcion")
        self.lb_reparto = QtGui.QLabel(Actor)
        self.lb_reparto.setGeometry(QtCore.QRect(30, 270, 58, 17))
        self.lb_reparto.setObjectName("lb_reparto")
        self.le_descripcion = QtGui.QListWidget(Actor)
        self.le_descripcion.setGeometry(QtCore.QRect(20, 290, 281, 111))
        self.le_descripcion.setObjectName("le_descripcion")
        self.cb_actores = QtGui.QComboBox(Actor)
        self.cb_actores.setGeometry(QtCore.QRect(20, 410, 201, 27))
        self.cb_actores.setObjectName("cb_actores")
        self.btn_plus = QtGui.QPushButton(Actor)
        self.btn_plus.setGeometry(QtCore.QRect(230, 410, 31, 27))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtGui.QPushButton(Actor)
        self.btn_minus.setGeometry(QtCore.QRect(270, 410, 31, 27))
        self.btn_minus.setObjectName("btn_minus")
        self.cancel = QtGui.QPushButton(Actor)
        self.cancel.setGeometry(QtCore.QRect(166, 450, 141, 27))
        self.cancel.setObjectName("cancel")
        self.accept = QtGui.QPushButton(Actor)
        self.accept.setGeometry(QtCore.QRect(20, 450, 131, 27))
        self.accept.setObjectName("accept")

        self.retranslateUi(Actor)
        QtCore.QMetaObject.connectSlotsByName(Actor)

    def retranslateUi(self, Actor):
        Actor.setWindowTitle(QtGui.QApplication.translate("Actor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("Actor", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_birth.setText(QtGui.QApplication.translate("Actor", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_genero.setText(QtGui.QApplication.translate("Actor", "Director:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_descripcion.setText(QtGui.QApplication.translate("Actor", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_reparto.setText(QtGui.QApplication.translate("Actor", "Reparto:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_plus.setText(QtGui.QApplication.translate("Actor", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_minus.setText(QtGui.QApplication.translate("Actor", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Actor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.accept.setText(QtGui.QApplication.translate("Actor", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

