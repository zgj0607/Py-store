# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inventory_money.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventorymoneyForm(object):
    def setupUi(self, inventorymoneyForm):
        inventorymoneyForm.setObjectName("inventorymoneyForm")
        inventorymoneyForm.resize(880, 720)
        self.tableWidget = QtWidgets.QTableWidget(inventorymoneyForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 851, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(inventorymoneyForm)
        QtCore.QMetaObject.connectSlotsByName(inventorymoneyForm)

    def retranslateUi(self, inventorymoneyForm):
        _translate = QtCore.QCoreApplication.translate
        inventorymoneyForm.setWindowTitle(_translate("inventorymoneyForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("inventorymoneyForm", "一级分类"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("inventorymoneyForm", "二级分类"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("inventorymoneyForm", "库存数量"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("inventorymoneyForm", "库存金额"))

