# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from View.buy.normal_buy_dialog import StockInputDialog
from View.buy.ui.ui_normal_buy_query import Ui_stockQueryForm
from View.utils.table_utils import set_table_content
from database.dao.buy.buy_handler import get_all_stock


class StockQuery(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(StockQuery, self).__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_buy_info)
        self.editButton.clicked.connect(self.edit_buy_info)
        self.setWindowTitle('普通进货录入')
        self.stocktableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.table_title = (
            "ID", '进货日期', '商品型号', '商品品牌', '进货数量', '单位', '进货单价', '单品小计',
            '供应商', '所属项目', '付款金额', '未付金额')

        self._init_buy_info_table()
        self.stocktableView.setColumnWidth(1, 60)
        self.stocktableView.setColumnWidth(4, 50)
        self.stocktableView.setColumnWidth(5, 40)
        self.stocktableView.setColumnWidth(6, 80)
        self.stocktableView.setColumnWidth(7, 80)
        self.stocktableView.setColumnWidth(10, 80)
        self.stocktableView.setColumnWidth(11, 80)
        self.stocktableView.setColumnHidden(0, True)

    # 新增进货录入信息
    def add_buy_info(self):
        dialog = StockInputDialog()
        dialog.exec()

    # 修改进货录入信息
    def edit_buy_info(self):
        dialog = StockInputDialog()
        dialog.exec()

    def _init_buy_info_table(self):
        set_table_content(self.stocktableView, get_all_stock(), self.table_title)
