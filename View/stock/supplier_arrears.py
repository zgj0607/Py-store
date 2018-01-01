# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.stock.ui_supplier_arrears import Ui_supplierarrearsForm
from View.stock.supplier_arrears_dialog import Diglog_supplier_arrears
from View.stock.supplier_payment_dialog import Diglog_supplier_payment

class supplierarrearsForm_stock(QtWidgets.QWidget, Ui_supplierarrearsForm):
    def __init__(self):
        super(supplierarrearsForm_stock, self).__init__()
        self.setupUi(self)
        self.singleButton.clicked.connect(self.single)
        self.moreButton.clicked.connect(self.more)
        self.detailButton.clicked.connect(self.detail)
        self.setWindowTitle('欠款信息')
    def _retranslateUi(self):
        print('123')

    # 单个付款
    def single(self):
        dialog = Diglog_supplier_payment()
        dialog.show()
        dialog.exec()

    # 批量付款
    def more(self):
        dialog = Diglog_supplier_payment()
        dialog.show()
        dialog.exec()

    # 欠款明细
    def detail(self):
        dialog = Diglog_supplier_arrears()
        dialog.show()
        dialog.exec()


