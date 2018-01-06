# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stock_unsalable_warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventoryunsalablewarningForm(object):
    def setupUi(self, inventoryunsalablewarningForm):
        inventoryunsalablewarningForm.setObjectName("inventoryunsalablewarningForm")
        inventoryunsalablewarningForm.resize(880, 720)
        self.tableWidget = QtWidgets.QTableWidget(inventoryunsalablewarningForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 851, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.exportButton = QtWidgets.QPushButton(inventoryunsalablewarningForm)
        self.exportButton.setGeometry(QtCore.QRect(10, 20, 113, 32))
        self.exportButton.setObjectName("exportButton")

        self.retranslateUi(inventoryunsalablewarningForm)
        QtCore.QMetaObject.connectSlotsByName(inventoryunsalablewarningForm)

    def retranslateUi(self, inventoryunsalablewarningForm):
        _translate = QtCore.QCoreApplication.translate
        inventoryunsalablewarningForm.setWindowTitle(_translate("inventoryunsalablewarningForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("inventoryunsalablewarningForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("inventoryunsalablewarningForm", "商品品牌"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("inventoryunsalablewarningForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("inventoryunsalablewarningForm", "库存数量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("inventoryunsalablewarningForm", "最长库龄"))
        self.exportButton.setText(_translate("inventoryunsalablewarningForm", "导出"))

