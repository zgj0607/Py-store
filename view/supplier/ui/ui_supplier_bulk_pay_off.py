# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_supplier_bulk_pay_off.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BulkPayOff(object):
    def setupUi(self, BulkPayOff):
        BulkPayOff.setObjectName("BulkPayOff")
        BulkPayOff.resize(264, 216)
        BulkPayOff.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BulkPayOff)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(BulkPayOff)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pay = QtWidgets.QLineEdit(BulkPayOff)
        self.pay.setMinimumSize(QtCore.QSize(150, 26))
        self.pay.setMaximumSize(QtCore.QSize(150, 16))
        self.pay.setReadOnly(True)
        self.pay.setObjectName("pay")
        self.gridLayout.addWidget(self.pay, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(BulkPayOff)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pay_to = QtWidgets.QLineEdit(BulkPayOff)
        self.pay_to.setMinimumSize(QtCore.QSize(150, 26))
        self.pay_to.setMaximumSize(QtCore.QSize(150, 16))
        self.pay_to.setReadOnly(True)
        self.pay_to.setObjectName("pay_to")
        self.gridLayout.addWidget(self.pay_to, 0, 1, 1, 1)
        self.payment_method = QtWidgets.QComboBox(BulkPayOff)
        self.payment_method.setMinimumSize(QtCore.QSize(150, 26))
        self.payment_method.setMaximumSize(QtCore.QSize(160, 16))
        self.payment_method.setObjectName("payment_method")
        self.gridLayout.addWidget(self.payment_method, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(BulkPayOff)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.note = QtWidgets.QLineEdit(BulkPayOff)
        self.note.setMinimumSize(QtCore.QSize(150, 26))
        self.note.setMaximumSize(QtCore.QSize(150, 16))
        self.note.setObjectName("note")
        self.gridLayout.addWidget(self.note, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(BulkPayOff)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.payButton = QtWidgets.QPushButton(BulkPayOff)
        self.payButton.setMinimumSize(QtCore.QSize(120, 26))
        self.payButton.setMaximumSize(QtCore.QSize(120, 26))
        self.payButton.setObjectName("payButton")
        self.gridLayout.addWidget(self.payButton, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(BulkPayOff)
        QtCore.QMetaObject.connectSlotsByName(BulkPayOff)

    def retranslateUi(self, BulkPayOff):
        _translate = QtCore.QCoreApplication.translate
        BulkPayOff.setWindowTitle(_translate("BulkPayOff", "Dialog"))
        self.label_3.setText(_translate("BulkPayOff", "付款方式"))
        self.label_2.setText(_translate("BulkPayOff", "付款金额"))
        self.label.setText(_translate("BulkPayOff", "付款至"))
        self.label_4.setText(_translate("BulkPayOff", "备注"))
        self.payButton.setText(_translate("BulkPayOff", "确认付款"))

