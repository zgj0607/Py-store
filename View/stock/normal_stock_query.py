# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.stock.ui_normal_stock_query import Ui_stockQueryForm
from View.stock.normal_stock_diglog import Diglog_stock


class stockQueryForm_stock(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(stockQueryForm_stock, self).__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addStock)
        self.editButton.clicked.connect(self.editStock)
        self.setWindowTitle('进货监控')

    def _retranslateUi(self):
        print('123')

        # 新增进货录入信息

    def addStock(self):
        dialog = Diglog_stock()
        dialog.show()
        dialog.exec()
        # stockForm.

        # 修改进货录入信息

    def editStock(self):
        dialog = Diglog_stock()
        dialog.show()
        dialog.exec()




