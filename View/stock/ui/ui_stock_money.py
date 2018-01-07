# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stock_money.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StockMoney(object):
    def setupUi(self, StockMoney):
        StockMoney.setObjectName("StockMoney")
        StockMoney.resize(953, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(StockMoney)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(StockMoney)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(StockMoney)
        QtCore.QMetaObject.connectSlotsByName(StockMoney)

    def retranslateUi(self, StockMoney):
        _translate = QtCore.QCoreApplication.translate
        StockMoney.setWindowTitle(_translate("StockMoney", "Form"))

