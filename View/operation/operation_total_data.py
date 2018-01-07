# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.operation.ui.ui_operation_total_data import Ui_operationtotaldataForm



class operationtotaldataForm(QtWidgets.QWidget, Ui_operationtotaldataForm):
    def __init__(self):
        super(operationtotaldataForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('总体经营数据')
    def _retranslateUi(self):
        print('123')

    # 历史进货信息查询
    def serch(self):
        print('123')





