# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario_pelicula.ui'
#
# Created: Sun Jul 14 18:36:40 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Actor(object):
    def setupUi(self, Actor):
        Actor.setObjectName("Actor")
        Actor.resize(534, 509)
        self.verticalLayoutWidget = QtGui.QWidget(Actor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 191, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.a_photo = QtGui.QGraphicsView(self.verticalLayoutWidget)
        self.a_photo.setObjectName("a_photo")
        self.verticalLayout.addWidget(self.a_photo)
        self.change = QtGui.QPushButton(self.verticalLayoutWidget)
        self.change.setObjectName("change")
        self.verticalLayout.addWidget(self.change)
        self.horizontalLayoutWidget = QtGui.QWidget(Actor)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 460, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.accept = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.accept.setObjectName("accept")
        self.horizontalLayout.addWidget(self.accept)
        self.lb_nombre = QtGui.QLabel(Actor)
        self.lb_nombre.setGeometry(QtCore.QRect(30, 304, 91, 21))
        self.lb_nombre.setObjectName("lb_nombre")
        self.lb_birth = QtGui.QLabel(Actor)
        self.lb_birth.setGeometry(QtCore.QRect(30, 330, 91, 21))
        self.lb_birth.setObjectName("lb_birth")
        self.lb_genero = QtGui.QLabel(Actor)
        self.lb_genero.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.lb_genero.setObjectName("lb_genero")
        self.le_nombre = QtGui.QLineEdit(Actor)
        self.le_nombre.setGeometry(QtCore.QRect(110, 300, 181, 27))
        self.le_nombre.setObjectName("le_nombre")
        self.le_fecha = QtGui.QLineEdit(Actor)
        self.le_fecha.setGeometry(QtCore.QRect(110, 330, 181, 27))
        self.le_fecha.setObjectName("le_fecha")
        self.le_director = QtGui.QLineEdit(Actor)
        self.le_director.setGeometry(QtCore.QRect(110, 360, 181, 27))
        self.le_director.setObjectName("le_director")
        self.te_descripcion = QtGui.QPlainTextEdit(Actor)
        self.te_descripcion.setGeometry(QtCore.QRect(230, 50, 281, 211))
        self.te_descripcion.setObjectName("te_descripcion")
        self.lb_descripcion = QtGui.QLabel(Actor)
        self.lb_descripcion.setGeometry(QtCore.QRect(230, 20, 91, 21))
        self.lb_descripcion.setObjectName("lb_descripcion")
        self.lb_reparto = QtGui.QLabel(Actor)
        self.lb_reparto.setGeometry(QtCore.QRect(310, 270, 101, 17))
        self.lb_reparto.setObjectName("lb_reparto")
        self.le_descripcion = QtGui.QListView(Actor)
        self.le_descripcion.setGeometry(QtCore.QRect(310, 300, 201, 151))
        self.le_descripcion.setObjectName("le_descripcion")
        self.cb_actores = QtGui.QComboBox(Actor)
        self.cb_actores.setGeometry(QtCore.QRect(310, 460, 121, 27))
        self.cb_actores.setObjectName("cb_actores")
        self.btn_plus = QtGui.QPushButton(Actor)
        self.btn_plus.setGeometry(QtCore.QRect(440, 460, 31, 27))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtGui.QPushButton(Actor)
        self.btn_minus.setGeometry(QtCore.QRect(480, 460, 31, 27))
        self.btn_minus.setObjectName("btn_minus")

        self.retranslateUi(Actor)
        QtCore.QMetaObject.connectSlotsByName(Actor)

    def retranslateUi(self, Actor):
        Actor.setWindowTitle(QtGui.QApplication.translate("Actor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.change.setText(QtGui.QApplication.translate("Actor", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Actor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.accept.setText(QtGui.QApplication.translate("Actor", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("Actor", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_birth.setText(QtGui.QApplication.translate("Actor", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_genero.setText(QtGui.QApplication.translate("Actor", "Director:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_descripcion.setText(QtGui.QApplication.translate("Actor", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_reparto.setText(QtGui.QApplication.translate("Actor", "Reparto:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_plus.setText(QtGui.QApplication.translate("Actor", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_minus.setText(QtGui.QApplication.translate("Actor", "-", None, QtGui.QApplication.UnicodeUTF8))

