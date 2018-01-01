# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.stock.ui_normal_stock_dialog import Ui_Dialog


class Diglog_stock(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Diglog_stock, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self._retranslateUi)

    def _retranslateUi(self):
        self.retranslateUi