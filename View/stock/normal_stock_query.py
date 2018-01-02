# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from View.stock.normal_stock_diglog import StockInputDialog
from View.stock.ui_normal_stock_query import Ui_stockQueryForm
from View.utils.table_utils import set_table_content
from database.dao.stock.stock_handler import get_all_stock


class StockQuery(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(StockQuery, self).__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addStock)
        self.editButton.clicked.connect(self.editStock)
        self.setWindowTitle('普通进货录入')
        self.stocktableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.table_title = (
            "ID", '进货日期', '商品型号', '商品品牌', '进货数量', '单位', '进货单价', '单品小计', '供应商', '所属项目', '付款金额', '未付金额')

        set_table_content(self.stocktableView, get_all_stock(), self.table_title)
        self.stocktableView.setColumnWidth(4, 60)
        self.stocktableView.setColumnWidth(5, 40)
        self.stocktableView.setColumnWidth(6, 80)
        self.stocktableView.setColumnWidth(7, 80)
        self.stocktableView.setColumnWidth(10, 80)
        self.stocktableView.setColumnWidth(11, 80)
        self.stocktableView.setColumnHidden(0, True)

    def _retranslateUi(self):
        print('123')

        # 新增进货录入信息

    def addStock(self):
        dialog = StockInputDialog()
        dialog.exec()
        # stockForm.

        # 修改进货录入信息

    def editStock(self):
        dialog = StockInputDialog()
        dialog.show()
        dialog.exec()
