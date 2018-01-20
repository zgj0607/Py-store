# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pad_connect.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PadConnect(object):
    def setupUi(self, PadConnect):
        PadConnect.setObjectName("PadConnect")
        PadConnect.resize(368, 170)
        PadConnect.setModal(True)
        self.centralwidget = QtWidgets.QWidget(PadConnect)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 371, 151))
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(30, 20, 311, 61))
        self.info.setText("")
        self.info.setObjectName("info")
        self.allow = QtWidgets.QPushButton(self.centralwidget)
        self.allow.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.allow.setObjectName("allow")
        self.refuse = QtWidgets.QPushButton(self.centralwidget)
        self.refuse.setGeometry(QtCore.QRect(210, 100, 81, 31))
        self.refuse.setObjectName("refuse")

        self.retranslateUi(PadConnect)
        QtCore.QMetaObject.connectSlotsByName(PadConnect)

    def retranslateUi(self, PadConnect):
        _translate = QtCore.QCoreApplication.translate
        PadConnect.setWindowTitle(_translate("PadConnect", "Pad连接请求确认"))
        self.allow.setText(_translate("PadConnect", "允许"))
        self.refuse.setText(_translate("PadConnect", "拒绝"))

