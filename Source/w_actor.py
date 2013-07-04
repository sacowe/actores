# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_actor.ui'
#
# Created: Thu Jul  4 12:12:09 2013
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
        self.a_name = QtGui.QLabel(Actor)
        self.a_name.setGeometry(QtCore.QRect(30, 300, 249, 25))
        self.a_name.setObjectName("a_name")
        self.a_birth = QtGui.QLabel(Actor)
        self.a_birth.setGeometry(QtCore.QRect(30, 319, 241, 41))
        self.a_birth.setObjectName("a_birth")
        self.a_age = QtGui.QLabel(Actor)
        self.a_age.setGeometry(QtCore.QRect(30, 350, 249, 31))
        self.a_age.setObjectName("a_age")
        self.nombre_edit = QtGui.QLineEdit(Actor)
        self.nombre_edit.setGeometry(QtCore.QRect(130, 300, 181, 27))
        self.nombre_edit.setObjectName("nombre_edit")
        self.cumple_edit = QtGui.QLineEdit(Actor)
        self.cumple_edit.setGeometry(QtCore.QRect(130, 330, 181, 27))
        self.cumple_edit.setObjectName("cumple_edit")
        self.lineEdit_3 = QtGui.QLineEdit(Actor)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 360, 181, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Actor)
        QtCore.QMetaObject.connectSlotsByName(Actor)

    def retranslateUi(self, Actor):
        Actor.setWindowTitle(QtGui.QApplication.translate("Actor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.change.setText(QtGui.QApplication.translate("Actor", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Actor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.accept.setText(QtGui.QApplication.translate("Actor", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.a_name.setText(QtGui.QApplication.translate("Actor", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.a_birth.setText(QtGui.QApplication.translate("Actor", "Cumpleaños:", None, QtGui.QApplication.UnicodeUTF8))
        self.a_age.setText(QtGui.QApplication.translate("Actor", "Edad:", None, QtGui.QApplication.UnicodeUTF8))

