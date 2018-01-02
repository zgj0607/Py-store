# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from View.stock.history_compare_dialog import Diglog_historystock
from View.stock.ui_history_stock import Ui_historySockForm


class HistoryStock(QtWidgets.QWidget, Ui_historySockForm):
    def __init__(self):
        super(HistoryStock, self).__init__()
        self.setupUi(self)
        self.serchButton.clicked.connect(self.serch)
        self.moniButton.clicked.connect(self.monitor)
        self.setWindowTitle('历史进货信息')

    # 历史进货信息查询
    def serch(self):
        dialog = Diglog_historystock()
        dialog.show()
        dialog.exec()

    def monitor(self):
        dialog = Diglog_historystock()
        dialog.show()
        dialog.exec()
        # stockForm.
