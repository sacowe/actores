# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario_actor.ui'
#
# Created: Sun Jul 14 18:36:26 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Actor(object):
    def setupUi(self, Actor):
        Actor.setObjectName("Actor")
        Actor.resize(333, 440)
        self.verticalLayoutWidget = QtGui.QWidget(Actor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 20, 191, 271))
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 390, 251, 31))
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
        self.lb_nombre.setGeometry(QtCore.QRect(30, 300, 91, 25))
        self.lb_nombre.setObjectName("lb_nombre")
        self.lb_birth = QtGui.QLabel(Actor)
        self.lb_birth.setGeometry(QtCore.QRect(30, 330, 91, 21))
        self.lb_birth.setObjectName("lb_birth")
        self.lb_genero = QtGui.QLabel(Actor)
        self.lb_genero.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.lb_genero.setObjectName("lb_genero")
        self.le_nombre = QtGui.QLineEdit(Actor)
        self.le_nombre.setGeometry(QtCore.QRect(130, 300, 181, 27))
        self.le_nombre.setObjectName("le_nombre")
        self.le_birth = QtGui.QLineEdit(Actor)
        self.le_birth.setGeometry(QtCore.QRect(130, 330, 181, 27))
        self.le_birth.setObjectName("le_birth")
        self.cb_genero = QtGui.QComboBox(Actor)
        self.cb_genero.setGeometry(QtCore.QRect(130, 360, 181, 27))
        self.cb_genero.setObjectName("cb_genero")

        self.retranslateUi(Actor)
        QtCore.QMetaObject.connectSlotsByName(Actor)

    def retranslateUi(self, Actor):
        Actor.setWindowTitle(QtGui.QApplication.translate("Actor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.change.setText(QtGui.QApplication.translate("Actor", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Actor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.accept.setText(QtGui.QApplication.translate("Actor", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("Actor", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_birth.setText(QtGui.QApplication.translate("Actor", "Cumpleaños:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_genero.setText(QtGui.QApplication.translate("Actor", "Genero:", None, QtGui.QApplication.UnicodeUTF8))

