# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_change_password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangePwd(object):
    def setupUi(self, ChangePwd):
        ChangePwd.setObjectName("ChangePwd")
        ChangePwd.resize(361, 142)
        self.centralwidget = QtWidgets.QWidget(ChangePwd)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 361, 141))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 131, 41))
        self.label.setObjectName("label")
        self.password_one = QtWidgets.QLineEdit(self.centralwidget)
        self.password_one.setGeometry(QtCore.QRect(170, 20, 161, 20))
        self.password_one.setObjectName("password_one")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(160, 100, 75, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm.sizePolicy().hasHeightForWidth())
        self.confirm.setSizePolicy(sizePolicy)
        self.confirm.setObjectName("confirm")
        self.password_two = QtWidgets.QLineEdit(self.centralwidget)
        self.password_two.setGeometry(QtCore.QRect(170, 60, 161, 20))
        self.password_two.setObjectName("password_two")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 131, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ChangePwd)
        QtCore.QMetaObject.connectSlotsByName(ChangePwd)

    def retranslateUi(self, ChangePwd):
        _translate = QtCore.QCoreApplication.translate
        ChangePwd.setWindowTitle(_translate("ChangePwd", "修改密码"))
        self.label.setText(_translate("ChangePwd", "<html><head/><body><p><span style=\" font-weight:600;\">         请输入新密码</span></p></body></html>"))
        self.confirm.setText(_translate("ChangePwd", "确认修改"))
        self.label_2.setText(_translate("ChangePwd", "<html><head/><body><p><span style=\" font-weight:600;\">请再次输入密码</span></p></body></html>"))

