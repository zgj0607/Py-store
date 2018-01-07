# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_normal_buy_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_stockQueryForm(object):
    def setupUi(self, stockQueryForm):
        stockQueryForm.setObjectName("stockQueryForm")
        stockQueryForm.resize(953, 602)
        self.add = QtWidgets.QPushButton(stockQueryForm)
        self.add.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.add.setObjectName("add")
        self.do_return = QtWidgets.QPushButton(stockQueryForm)
        self.do_return.setGeometry(QtCore.QRect(120, 10, 113, 32))
        self.do_return.setObjectName("do_return")
        self.buy_info_table = QtWidgets.QTableView(stockQueryForm)
        self.buy_info_table.setGeometry(QtCore.QRect(0, 50, 951, 550))
        self.buy_info_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.buy_info_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.buy_info_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.buy_info_table.setTextElideMode(QtCore.Qt.ElideNone)
        self.buy_info_table.setSortingEnabled(True)
        self.buy_info_table.setObjectName("buy_info_table")
        self.buy_info_table.horizontalHeader().setStretchLastSection(True)
        self.buy_info_table.verticalHeader().setVisible(False)

        self.retranslateUi(stockQueryForm)
        QtCore.QMetaObject.connectSlotsByName(stockQueryForm)

    def retranslateUi(self, stockQueryForm):
        _translate = QtCore.QCoreApplication.translate
        stockQueryForm.setWindowTitle(_translate("stockQueryForm", "进货信息"))
        self.add.setText(_translate("stockQueryForm", "录入"))
        self.do_return.setText(_translate("stockQueryForm", "退货"))

