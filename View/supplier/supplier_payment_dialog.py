# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.supplier.ui.ui_supplier_payment_dialog import Ui_supplierpaymentDialog


class Diglog_supplier_payment(QtWidgets.QDialog, Ui_supplierpaymentDialog):
    def __init__(self):
        super(Diglog_supplier_payment, self).__init__()
        self.setupUi(self)
        self.payButton.clicked.connect(self.pay)

    def _retranslateUi(self):
        self.retranslateUi

    def pay(self):
        self.retranslateUi