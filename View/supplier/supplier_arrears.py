# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from View.supplier.supplier_arrears_dialog import Diglog_supplier_arrears
from View.supplier.supplier_payment_dialog import Diglog_supplier_payment
from View.supplier.ui.ui_supplier_arrears import Ui_SupplierArrears
from View.utils import table_utils
from database.dao.buy import payment_handler


class SupplierArrears(QtWidgets.QWidget, Ui_SupplierArrears):
    def __init__(self):
        super(SupplierArrears, self).__init__()
        self.setupUi(self)
        self.single_button.clicked.connect(self.single_pay)
        self.bulk_button.clicked.connect(self.bulk_pay)
        self.setWindowTitle('欠款信息')
        self.summary_table_title = ('','','','')

        self._init_table()

    def _init_table(self):
        self._init_summary_table()

    def _init_summary_table(self):
        record = payment_handler.get_all_arrears_info()
        table_utils.set_table_content(self.summary_table, record, self.summary_table_title)

    # 单个付款
    def single_pay(self):
        dialog = Diglog_supplier_payment()
        dialog.show()
        dialog.exec()

    # 批量付款
    def bulk_pay(self):
        dialog = Diglog_supplier_payment()
        dialog.show()
        dialog.exec()

    # 欠款明细
    def arrears_detail(self):
        dialog = Diglog_supplier_arrears()
        dialog.show()
        dialog.exec()
