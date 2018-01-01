# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.stock.ui_history_stock import Ui_historySockForm
from View.stock.history_compare_dialog import Diglog_historystock


class historystockQueryForm_stock(QtWidgets.QWidget, Ui_historySockForm):
    def __init__(self):
        super(historystockQueryForm_stock, self).__init__()
        self.setupUi(self)
        self.serchButton.clicked.connect(self.serch)
        self.moniButton.clicked.connect(self.moni)
        self.setWindowTitle('历史进货信息')
    def _retranslateUi(self):
        print('123')

    # 历史进货信息查询
    def serch(self):
        dialog=Diglog_historystock()
        dialog.show()
        dialog.exec()

    def moni(self):
        dialog = Diglog_historystock()
        dialog.show()
        dialog.exec()
        # stockForm.




