# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.inventory.ui.ui_inventory_money import Ui_inventorymoneyForm



class inventory_moneyForm_stock(QtWidgets.QWidget, Ui_inventorymoneyForm):
    def __init__(self):
        super(inventory_moneyForm_stock, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库存金额')
    def _retranslateUi(self):
        print('123')






