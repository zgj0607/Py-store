# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.buy.ui.ui_write_off_dialog import Ui_writeOffDialog


class DiglogWriteOff(QtWidgets.QDialog, Ui_writeOffDialog):
    def __init__(self):
        super(DiglogWriteOff, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self._retranslateUi)

    def _retranslateUi(self):
        self.retranslateUi