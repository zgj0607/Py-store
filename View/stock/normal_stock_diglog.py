# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from View.stock.ui_normal_stock_dialog import Ui_Dialog
from View.utils.table_utils import set_table_content


class Diglog_stock(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(Diglog_stock, self).__init__()
        self.setupUi(self)
        self.commitButton.clicked().connect(self.commit)
    def _retranslateUi(self):
        print('123')

    # 进货信息录入
    def commit(self):
        buydate = self.staff_name.text()
        goodModel = self.gender.text()
        goodBrand = self.gender.text()
        number = self.gender.text()
        goodUnit = self.gender.text()
        price = self.gender.text()
        supplierName = self.gender.text()
        payAmount= self.gender.text()
        # id_card_no = self.id_card_no.text()
        # submit_staff_info(name, sex, id_card_no, self.staff_id)
        # QMessageBox.information(self.submit, "提示", "提交成功")
        # self.close()
        # set_table_content(self.staff_table, get_all_staff(), self.table_title)