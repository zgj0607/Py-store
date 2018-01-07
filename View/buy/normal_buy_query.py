# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from Common import time_utils, Common
from View.buy.normal_buy_dialog import StockInputDialog
from View.buy.ui.ui_normal_buy_query import Ui_stockQueryForm
from View.utils import table_utils, db_transaction_util
from View.utils.table_utils import set_table_content
from database.dao.buy import buy_handler, payment_handler
from database.dao.stock import stock_detail_handler, stock_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock_detail import StockDetail


class StockQuery(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(StockQuery, self).__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.add_buy_info)
        self.do_return.clicked.connect(self._do_return)
        self.setWindowTitle('普通进货录入')
        self.buy_info_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.table_title = (
            "ID", '进货日期', '商品型号', '商品品牌', '进货数量', '单位', '进货单价', '单品小计', '供应商ID',
            '供应商', '所属项目', '付款金额', '未付金额', '进货类型', '关联进货ID', '库存ID')

        self._init_buy_info_table()

    def _init_buy_info_table(self):
        buy_info_table = self.buy_info_table

        # 填充数据
        set_table_content(buy_info_table, buy_handler.get_all_buy_info(), self.table_title)

        # 隐藏ID列
        buy_info_table.setColumnHidden(0, True)
        buy_info_table.setColumnHidden(8, True)
        buy_info_table.setColumnHidden(15, True)

    # 新增进货录入信息
    def add_buy_info(self):
        dialog = StockInputDialog()
        dialog.exec()
        self._init_buy_info_table()

    # 退货录入
    def _do_return(self):
        buy_id = table_utils.get_table_current_index_info(self.buy_info_table, 0)

        if not buy_id:
            QMessageBox.information(self.do_return, "提示", '请先选择一条进货记录！')
            return

        balance = stock_detail_handler.get_in_store_count_by_buy_id(buy_id)
        if not balance or balance[0][0] <= 0:
            QMessageBox.information(self.do_return, "提示", '该进货批次的库量为零，请重新选择！')
            return
        balance = balance[0][0]

        return_number, ok = QInputDialog.getInt(self.do_return, '输入退货数量', '该批次现有库存 {} ，请输入退货量:'.format(balance),
                                                1, 1, balance, 1)

        while ok and not return_number:
            QMessageBox.information(self.do_return, "提示", '退货量不能为0')
            return_number, ok = QInputDialog.getInt(self.do_return, '输入退货数量', '该批次现有库存{}，请输入退货量:'.format(balance),
                                                    1, 1, balance, 1)
        if not ok:
            return

        self._add_return_info(buy_id, return_number)
        QMessageBox.information(self.do_return, "提示", '退货录入成功！')
        self._init_buy_info_table()

    def _add_return_info(self, rela_buy_id, return_number):
        try:

            db_transaction_util.begin()

            # 新增退货的进货信息
            return_id = self._add_buy_info(rela_buy_id, return_number)

            stock_id = int(table_utils.get_table_current_index_info(self.buy_info_table, 15))

            # 减少库存量
            unit_price = Decimal(table_utils.get_table_current_index_info(self.buy_info_table, 6))
            total = Decimal(return_number) * unit_price
            balance = 0 - return_number
            total_cost = Decimal(0.0) - total
            stock_handler.update_stock_balance(stock_id, balance, total_cost)

            # 更新原进货库存明细
            self._update_stock_detail(rela_buy_id, return_number)

            # 增加退货库存明细
            self._add_return_detail(return_id, stock_id, unit_price, return_number)

            # 增加原进货付款明细
            paid = Decimal(table_utils.get_table_current_index_info(self.buy_info_table, 11))
            unpaid = Decimal(table_utils.get_table_current_index_info(self.buy_info_table, 12))
            self._add_original_buy_payment_detail(rela_buy_id, total, paid, unpaid)

            # 增加退货付款明细
            self._add_return_payment_detail(return_id, total)
            db_transaction_util.commit()
        except Exception as e:
            print(e)
            db_transaction_util.rollback()

    def _add_buy_info(self, rela_buy_id, return_number) -> int:
        unit_price = Decimal(table_utils.get_table_current_index_info(self.buy_info_table, 6))
        unit = table_utils.get_table_current_index_info(self.buy_info_table, 5)
        supplier_id = int(table_utils.get_table_current_index_info(self.buy_info_table, 8))
        stock_id = int(table_utils.get_table_current_index_info(self.buy_info_table, 15))
        total = Decimal(return_number) * unit_price
        paid = total

        buy_date = time_utils.get_date_number()
        create_time = time_utils.get_now()
        create_op = Common.config.login_user_info[0]

        buy = BuyInfo()
        buy.stock_id(stock_id).supplier_id(supplier_id).unit_price(unit_price).number(return_number)
        buy.buy_date(buy_date)
        buy.create_time(create_time).create_op(create_op)
        buy.paid(paid)
        buy.total(total)
        buy.rela_buy_id(rela_buy_id)
        buy.buy_type(BuyInfo.returned())

        return_id = buy_handler.add_buy_info(buy)

        return return_id

    def _update_stock_detail(self, rela_buy_id, return_number):
        details = stock_detail_handler.get_detail_by_buy_id(rela_buy_id)
        num = 0
        for detail in details:
            stock_detail_handler.update_detail_state(detail[0], StockDetail.returned())
            num += 1
            if num >= return_number:
                break

    def _add_return_detail(self, return_id, stock_id, unit_price, return_number):
        detail = StockDetail()
        detail.stock_id(stock_id).buy_id(return_id)
        detail.buy_price(unit_price)
        detail.state(StockDetail.returned())
        detail.type(StockDetail.by_returned())
        detail.update_time(time_utils.get_now())
        detail.update_op(Common.config.login_user_info[0])

        # 循环写入退货明细
        for i in range(return_number):
            stock_detail_handler.add_stock_detail(detail)

    def _add_original_buy_payment_detail(self, buy_id, total, paid, unpaid):
        now_paid = paid
        now_unpaid = unpaid
        if unpaid:
            if total >= unpaid:
                now_paid += Decimal(unpaid)
                now_unpaid = 0.0
            else:
                now_paid = now_paid + total
                now_unpaid = now_unpaid - total
            payment = Payment()
            payment.buy_id(buy_id)
            payment.payment_method(Payment.cash())
            payment.paid(now_paid)
            payment.unpaid(now_unpaid)
            payment.create_op(Common.config.login_user_info[0])
            payment.create_time(time_utils.get_now())
            payment.refund_type(Payment.returned())

            payment_handler.add_payment_detail(payment)

    def _add_return_payment_detail(self, return_id, total):
        payment = Payment()
        payment.buy_id(return_id)
        payment.payment_method(Payment.cash())
        payment.paid(total)
        payment.create_op(Common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())
        payment.refund_type(Payment.returned())

        payment_handler.add_payment_detail(payment)
