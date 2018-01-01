# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 138)
        Dialog.setStyleSheet("background: #ECECEC;")
        self.pc_code_label = QtWidgets.QLabel(Dialog)
        self.pc_code_label.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.pc_code_label.setStyleSheet("color:#A1A1A1;")
        self.pc_code_label.setObjectName("pc_code_label")
        self.reg_code_label = QtWidgets.QLabel(Dialog)
        self.reg_code_label.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.reg_code_label.setStyleSheet("color:#A1A1A1;")
        self.reg_code_label.setObjectName("reg_code_label")
        self.copy_pc_code = QtWidgets.QPushButton(Dialog)
        self.copy_pc_code.setGeometry(QtCore.QRect(240, 20, 50, 24))
        self.copy_pc_code.setStyleSheet("background-color: #B2B2B2;\n"
"color: #606060;\n"
"border: 1px solid #C5C5C5;\n"
"border-radius: 5px;")
        self.copy_pc_code.setObjectName("copy_pc_code")
        self.verify_reg_code = QtWidgets.QPushButton(Dialog)
        self.verify_reg_code.setGeometry(QtCore.QRect(130, 100, 50, 24))
        self.verify_reg_code.setStyleSheet("background-color: #4FA2F8;\n"
"color: #FFFFFF;\n"
"border: 1px solid #55A2F5;\n"
"border-radius: 5px;")
        self.verify_reg_code.setObjectName("verify_reg_code")
        self.pc_code = QtWidgets.QPlainTextEdit(Dialog)
        self.pc_code.setGeometry(QtCore.QRect(80, 20, 150, 24))
        self.pc_code.setStyleSheet("border: 1px solid #BCBCBC;\n"
"border-radius: 5px;\n"
"color: #000000;\n"
"background-color: #E8E8E8;")
        self.pc_code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pc_code.setObjectName("pc_code")
        self.serial_number = QtWidgets.QLineEdit(Dialog)
        self.serial_number.setGeometry(QtCore.QRect(80, 60, 150, 24))
        self.serial_number.setStyleSheet("border:2px solid #8EACCC;\n"
"color:#000000;\n"
"background-color: #FFFFFF;\n"
"border-radius: 5px;")
        self.serial_number.setObjectName("serial_number")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "验证"))
        self.pc_code_label.setText(_translate("Dialog", "序列号："))
        self.reg_code_label.setText(_translate("Dialog", "注册码："))
        self.copy_pc_code.setText(_translate("Dialog", "复制"))
        self.verify_reg_code.setText(_translate("Dialog", "验证"))
        self.serial_number.setPlaceholderText(_translate("Dialog", "请输入16位注册码"))

