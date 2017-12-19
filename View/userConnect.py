# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userConnect.ui'
#
# Created: Wed Mar 29 11:51:06 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow_UserConnect(QtWidgets.QDialog):
    def __init__(self,word,key,today,deviceName,ip,func):
        QtWidgets.QDialog.__init__(self)
        self.word = word
        self.key = key
        self.func = func
        self.today = today
        self.deviceName = deviceName
        self.ip = ip
        myIcon = QIcon('img/logo.png')
        self.setWindowIcon(myIcon)

        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-image: url(img/button.png);background-color:transparent;background-repeat:no-repeat}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette=QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon)) #添加背景图片
        self.setPalette(palette)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(368, 170)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 311, 61))
        self.label.setObjectName("label")
        self.allow = QtWidgets.QPushButton(self.centralwidget)
        self.allow.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.allow.setObjectName("allow")
        self.refuse = QtWidgets.QPushButton(self.centralwidget)
        self.refuse.setGeometry(QtCore.QRect(210, 100, 81, 31))

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.WindowStaysOnTopHint )
        self.setFixedSize(self.width(), self.height())

        self.retranslateUi(self)
        self.allow.clicked.connect(self.AllowYuanGong)
        self.refuse.clicked.connect(self.RefuseYuanGong)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", self.word))
        self.allow.setText(_translate("MainWindow", "允许"))
        self.refuse.setText(_translate("MainWindow", "拒绝"))

    def AddYuanGong(self,state="0"):
        value = "'{}','{}','{}','{}'".format(self.ip,state,self.deviceName,self.today)
        self.func("Device",self.key,value)
        self.close()

    def AllowYuanGong(self):
        self.AddYuanGong("1")

    def RefuseYuanGong(self):
        self.AddYuanGong("0")
