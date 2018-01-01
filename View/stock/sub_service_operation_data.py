# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.stock.ui_sub_service_operation_data import Ui_sub_serviceoperationdataForm


class sub_serviceoperationdataForm(QtWidgets.QWidget, Ui_sub_serviceoperationdataForm):
    def __init__(self):
        super(sub_serviceoperationdataForm, self).__init__()
        self.setupUi(self)
        self.serchButton.clicked.connect(self.serch)
        self.exportButton.clicked.connect(self.export)
        self.setWindowTitle('二级分类经营数据')
    def _retranslateUi(self):
        print('123')

    # 按照时间查询
    def serch(self):
        print('123')
        # stockForm.

    # 导出
    def export(self):
        print('123')




