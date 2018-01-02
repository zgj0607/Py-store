# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_supplier_payment_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_supplierpaymentDialog(object):
    def setupUi(self, supplierpaymentDialog):
        supplierpaymentDialog.setObjectName("supplierpaymentDialog")
        supplierpaymentDialog.resize(455, 298)
        supplierpaymentDialog.setModal(True)
        self.formLayoutWidget = QtWidgets.QWidget(supplierpaymentDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 10, 251, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.payButton = QtWidgets.QPushButton(supplierpaymentDialog)
        self.payButton.setGeometry(QtCore.QRect(90, 220, 113, 32))
        self.payButton.setObjectName("payButton")
        self.closeButton = QtWidgets.QPushButton(supplierpaymentDialog)
        self.closeButton.setGeometry(QtCore.QRect(220, 220, 113, 32))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(supplierpaymentDialog)
        QtCore.QMetaObject.connectSlotsByName(supplierpaymentDialog)

    def retranslateUi(self, supplierpaymentDialog):
        _translate = QtCore.QCoreApplication.translate
        supplierpaymentDialog.setWindowTitle(_translate("supplierpaymentDialog", "Dialog"))
        self.label_2.setText(_translate("supplierpaymentDialog", "付款至"))
        self.label_9.setText(_translate("supplierpaymentDialog", "付款金额"))
        self.label_3.setText(_translate("supplierpaymentDialog", "付款方式"))
        self.label_4.setText(_translate("supplierpaymentDialog", "备注"))
        self.payButton.setText(_translate("supplierpaymentDialog", "确定付款"))
        self.closeButton.setText(_translate("supplierpaymentDialog", "取消"))

