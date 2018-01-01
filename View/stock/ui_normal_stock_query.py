# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_normal_stock_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_stockQueryForm(object):
    def setupUi(self, stockQueryForm):
        stockQueryForm.setObjectName("stockQueryForm")
        stockQueryForm.resize(983, 708)
        self.tableWidget = QtWidgets.QTableWidget(stockQueryForm)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 971, 661))
        self.tableWidget.setMinimumSize(QtCore.QSize(971, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(971, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.addButton = QtWidgets.QPushButton(stockQueryForm)
        self.addButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(stockQueryForm)
        self.editButton.setGeometry(QtCore.QRect(120, 10, 113, 32))
        self.editButton.setObjectName("editButton")

        self.retranslateUi(stockQueryForm)
        QtCore.QMetaObject.connectSlotsByName(stockQueryForm)

    def retranslateUi(self, stockQueryForm):
        _translate = QtCore.QCoreApplication.translate
        stockQueryForm.setWindowTitle(_translate("stockQueryForm", "进货信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("stockQueryForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("stockQueryForm", "进货日期"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("stockQueryForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("stockQueryForm", "商品品牌"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("stockQueryForm", "进货数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("stockQueryForm", "单位"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("stockQueryForm", "进货单价"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("stockQueryForm", "单品小计"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("stockQueryForm", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("stockQueryForm", "所属项目"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("stockQueryForm", "付款金额"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("stockQueryForm", "未付金额"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("stockQueryForm", "备注"))
        self.addButton.setText(_translate("stockQueryForm", "录入"))
        self.editButton.setText(_translate("stockQueryForm", "修改"))

