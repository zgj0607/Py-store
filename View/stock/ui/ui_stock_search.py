# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stock_search.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventoryForm(object):
    def setupUi(self, inventoryForm):
        inventoryForm.setObjectName("inventoryForm")
        inventoryForm.resize(880, 720)
        self.label = QtWidgets.QLabel(inventoryForm)
        self.label.setGeometry(QtCore.QRect(25, 40, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(inventoryForm)
        self.label_2.setGeometry(QtCore.QRect(245, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(inventoryForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 851, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.serchButton = QtWidgets.QPushButton(inventoryForm)
        self.serchButton.setGeometry(QtCore.QRect(475, 36, 113, 32))
        self.serchButton.setObjectName("serchButton")
        self.lineEdit = QtWidgets.QLineEdit(inventoryForm)
        self.lineEdit.setGeometry(QtCore.QRect(93, 39, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(inventoryForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(316, 38, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.exportButton = QtWidgets.QPushButton(inventoryForm)
        self.exportButton.setGeometry(QtCore.QRect(620, 34, 113, 32))
        self.exportButton.setObjectName("exportButton")

        self.retranslateUi(inventoryForm)
        QtCore.QMetaObject.connectSlotsByName(inventoryForm)

    def retranslateUi(self, inventoryForm):
        _translate = QtCore.QCoreApplication.translate
        inventoryForm.setWindowTitle(_translate("inventoryForm", "Form"))
        self.label.setText(_translate("inventoryForm", "商品品牌"))
        self.label_2.setText(_translate("inventoryForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("inventoryForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("inventoryForm", "商品品牌"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("inventoryForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("inventoryForm", "库存数量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("inventoryForm", "库存金额"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("inventoryForm", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("inventoryForm", "单位"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("inventoryForm", "备注"))
        self.serchButton.setText(_translate("inventoryForm", "查询"))
        self.exportButton.setText(_translate("inventoryForm", "导出"))

