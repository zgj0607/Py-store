# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userConnect.ui'
#
# Created: Wed Mar 29 20:44:04 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 311, 61))
        self.label.setObjectName("label")
        self.allow = QtWidgets.QPushButton(self.centralwidget)
        self.allow.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.allow.setObjectName("allow")
        self.refuse = QtWidgets.QPushButton(self.centralwidget)
        self.refuse.setGeometry(QtCore.QRect(210, 100, 81, 31))
        self.refuse.setObjectName("refuse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.allow.setText(_translate("MainWindow", "允许"))
        self.refuse.setText(_translate("MainWindow", "拒绝"))

