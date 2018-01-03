# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.buy.ui.ui_write_off_query import Ui_writeOffForm
from View.buy.write_off_dialog import DiglogWriteOff


class write_offForm_stock(QtWidgets.QWidget, Ui_writeOffForm):
    def __init__(self):
        super(write_offForm_stock, self).__init__()
        self.setupUi(self)
        self.writeOffButton.clicked.connect(self.writeOff)
        self.setWindowTitle('销负进货信息')
    def _retranslateUi(self):
        print('123')

    # 新增进货录入信息
    def writeOff(self):
        dialog=DiglogWriteOff()
        #dialog.show()
        dialog.exec()
        # stockForm.





