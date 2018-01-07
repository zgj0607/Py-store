# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.buy.ui.ui_buy_monitor import Ui_historymonitorForm
from View.buy.buy_monitor_two_detail import Diglog_monitor_two_detail


class stockmonitorQueryForm_stock(QtWidgets.QWidget, Ui_historymonitorForm):
    def __init__(self):
        super(stockmonitorQueryForm_stock, self).__init__()
        self.setupUi(self)
        self.serchButton.clicked.connect(self.addStock)
        self.moniButton.clicked.connect(self.editStock)
        self.setWindowTitle('进货监控')
    def _retranslateUi(self):
        print('123')

    # 新增进货录入信息
    def addStock(self):
        dialog=Diglog_monitor_two_detail()
        dialog.show()
        dialog.exec()
        # stockForm.

    # 修改进货录入信息
    def editStock(self):
        dialog = Diglog_monitor_two_detail()
        dialog.show()
        dialog.exec()



