# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_supplier_payment_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SupplierArrearPayOffDialog(object):
    def setupUi(self, SupplierArrearPayOffDialog):
        SupplierArrearPayOffDialog.setObjectName("SupplierArrearPayOffDialog")
        SupplierArrearPayOffDialog.resize(277, 302)
        SupplierArrearPayOffDialog.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SupplierArrearPayOffDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pay_to = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.pay_to.setMinimumSize(QtCore.QSize(150, 26))
        self.pay_to.setMaximumSize(QtCore.QSize(150, 26))
        self.pay_to.setReadOnly(True)
        self.pay_to.setObjectName("pay_to")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pay_to)
        self.label = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.paid = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.paid.setMinimumSize(QtCore.QSize(150, 26))
        self.paid.setMaximumSize(QtCore.QSize(150, 26))
        self.paid.setReadOnly(True)
        self.paid.setObjectName("paid")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.paid)
        self.label_9 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.pay = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.pay.setMinimumSize(QtCore.QSize(150, 26))
        self.pay.setMaximumSize(QtCore.QSize(150, 26))
        self.pay.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.pay.setObjectName("pay")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pay)
        self.label_3 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.payment_method = QtWidgets.QComboBox(SupplierArrearPayOffDialog)
        self.payment_method.setMinimumSize(QtCore.QSize(150, 26))
        self.payment_method.setMaximumSize(QtCore.QSize(160, 26))
        self.payment_method.setObjectName("payment_method")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.payment_method)
        self.label_4 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.notes = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.notes.setMinimumSize(QtCore.QSize(150, 26))
        self.notes.setMaximumSize(QtCore.QSize(150, 26))
        self.notes.setObjectName("notes")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.notes)
        self.payButton = QtWidgets.QPushButton(SupplierArrearPayOffDialog)
        self.payButton.setMinimumSize(QtCore.QSize(120, 0))
        self.payButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.payButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.payButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.payButton.setCheckable(False)
        self.payButton.setAutoDefault(True)
        self.payButton.setFlat(False)
        self.payButton.setObjectName("payButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.payButton)
        self.label_5 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.unpaid = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.unpaid.setMinimumSize(QtCore.QSize(150, 26))
        self.unpaid.setMaximumSize(QtCore.QSize(150, 26))
        self.unpaid.setReadOnly(True)
        self.unpaid.setObjectName("unpaid")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.unpaid)
        self.need_pay = QtWidgets.QLineEdit(SupplierArrearPayOffDialog)
        self.need_pay.setMinimumSize(QtCore.QSize(150, 26))
        self.need_pay.setMaximumSize(QtCore.QSize(150, 26))
        self.need_pay.setReadOnly(True)
        self.need_pay.setObjectName("need_pay")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.need_pay)
        self.label_6 = QtWidgets.QLabel(SupplierArrearPayOffDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(SupplierArrearPayOffDialog)
        QtCore.QMetaObject.connectSlotsByName(SupplierArrearPayOffDialog)
        SupplierArrearPayOffDialog.setTabOrder(self.pay_to, self.paid)
        SupplierArrearPayOffDialog.setTabOrder(self.paid, self.need_pay)
        SupplierArrearPayOffDialog.setTabOrder(self.need_pay, self.pay)
        SupplierArrearPayOffDialog.setTabOrder(self.pay, self.unpaid)
        SupplierArrearPayOffDialog.setTabOrder(self.unpaid, self.payment_method)
        SupplierArrearPayOffDialog.setTabOrder(self.payment_method, self.notes)
        SupplierArrearPayOffDialog.setTabOrder(self.notes, self.payButton)

    def retranslateUi(self, SupplierArrearPayOffDialog):
        _translate = QtCore.QCoreApplication.translate
        SupplierArrearPayOffDialog.setWindowTitle(_translate("SupplierArrearPayOffDialog", "Dialog"))
        self.label_2.setText(_translate("SupplierArrearPayOffDialog", "付款至"))
        self.label.setText(_translate("SupplierArrearPayOffDialog", "已付金额"))
        self.label_9.setText(_translate("SupplierArrearPayOffDialog", "本次支付"))
        self.label_3.setText(_translate("SupplierArrearPayOffDialog", "付款方式"))
        self.label_4.setText(_translate("SupplierArrearPayOffDialog", "备注"))
        self.payButton.setText(_translate("SupplierArrearPayOffDialog", "确定付款"))
        self.label_5.setText(_translate("SupplierArrearPayOffDialog", "剩余未付"))
        self.label_6.setText(_translate("SupplierArrearPayOffDialog", "未付金额"))
