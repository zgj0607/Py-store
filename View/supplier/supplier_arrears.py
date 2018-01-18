# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from View.supplier.supplier_bulk_pay_off import SupplierBulkPayOff
from View.supplier.supplier_payment_dialog import PayOffArrearsDialog
from View.supplier.ui.ui_supplier_arrears import Ui_SupplierArrears
from View.utils import table_utils
from database.dao.buy import payment_handler
from domain.buy import BuyInfo


class SupplierArrears(QtWidgets.QWidget, Ui_SupplierArrears):
    def __init__(self):
        super(SupplierArrears, self).__init__()
        self.setupUi(self)
        self.single_button.clicked.connect(self.single_pay)
        self.bulk_button.clicked.connect(self.bulk_pay)
        self.setWindowTitle('欠款信息')
        self.summary_table_title = ('供应商ID', '供应商名称', '欠款金额')
        self.detail_table_title = ('选择', '进货日期', '商品品牌', '商品型号', '进货数量', '单位', '进货单价', '单品小计', '付款金额', '未付金额', '进货ID')
        self.detail_table_cell_check_state = []

        self.supplier_name = ''

        self._init_table()
        self._init_signal_and_slot()

    def _init_table(self):
        self._init_summary_table()
        current_index = self.summary_table.model().index(0, 0)
        self._refresh_detail_table(current_index)

    def _init_summary_table(self):
        record = payment_handler.get_all_arrears_info()
        table_utils.set_table_content(self.summary_table, record, self.summary_table_title)
        self.summary_table.setColumnHidden(0, True)
        self.summary_table.resizeColumnsToContents()

    def _refresh_detail_table(self, summary_table_index):
        if not summary_table_index:
            record = ()
        else:
            supplier_id = table_utils.get_table_cell(self.summary_table, summary_table_index.row(), 0)
            if supplier_id:
                record = payment_handler.get_arrears_info_buy(supplier_id)
                self.supplier_name = table_utils.get_table_cell(self.summary_table, summary_table_index.row(), 1)
            else:
                record = ()
        table_utils.set_table_widget_content(self.detail_table, record, self.detail_table_title, True)
        self.detail_table.setColumnHidden(10, True)

        if record:
            self.detail_table.resizeColumnsToContents()
        self.detail_table_cell_check_state.clear()
        self.detail_table_cell_check_state = [False] * len(record)
        self.summary_need_pay.setText('0.0')

    def _init_signal_and_slot(self):
        self.summary_table.clicked['QModelIndex'].connect(self._refresh_detail_table)
        self.detail_table.cellClicked.connect(self._check_cell)

    # 单个付款
    def single_pay(self):

        buy_id = table_utils.get_table_current_index_info(self.detail_table, 10)
        if not buy_id:
            QMessageBox.information(self.single_button, '提示', '请选择一条明细！')
            return
        buy_info = BuyInfo()

        buy_info.buy_id(int(buy_id))

        unpaid = Decimal(table_utils.get_table_current_index_info(self.detail_table, 9))
        paid = Decimal(table_utils.get_table_current_index_info(self.detail_table, 8))
        supplier_id = self._get_supplier_id()

        buy_info.paid(paid)
        buy_info.unpaid(unpaid)
        buy_info.note(self.supplier_name)
        buy_info.supplier_id(supplier_id)
        dialog = PayOffArrearsDialog(buy_info)
        dialog.exec()

        self._init_table()

    # 批量付款
    def bulk_pay(self):
        total = self.summary_need_pay.text()

        if not total or not Decimal(total):
            QMessageBox.information(self.bulk_button, '提示', '请勾选需要付款的进货信息！')
            return
        buys = []
        for index, state in enumerate(self.detail_table_cell_check_state):
            if state:
                unpaid = Decimal(table_utils.get_table_cell(self.detail_table, index, 9))
                paid = Decimal(table_utils.get_table_cell(self.detail_table, index, 8))
                buy_id = int(table_utils.get_table_cell(self.detail_table, index, 10))
                buys.append((buy_id, unpaid + paid, 0.0))
        supplier_id = self._get_supplier_id()
        dialog = SupplierBulkPayOff(buys, total, self.supplier_name, supplier_id)
        dialog.exec()

        self._init_table()

    # 欠款明细
    def _check_cell(self, row, col):
        if not col:
            item = self.detail_table.item(row, 0)
            check_state = item.checkState()

            if (check_state == Qt.Checked) == self.detail_table_cell_check_state[row]:
                return

            unpaid = Decimal(self.detail_table.item(row, 9).text())
            total = Decimal(self.summary_need_pay.text())
            if check_state:
                total += unpaid
            else:
                total -= unpaid
            self.summary_need_pay.setText(str(total))
            self.detail_table_cell_check_state[row] = (check_state == Qt.Checked)

    def _get_supplier_id(self):
        supplier_id = table_utils.get_table_current_index_info(self.summary_table, 0)
        if not supplier_id:
            supplier_id = int(table_utils.get_table_cell(self.summary_table, 0, 0))
        else:
            supplier_id = int(supplier_id)
        return supplier_id
