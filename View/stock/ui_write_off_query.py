# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_write_off_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_writeOffForm(object):
    def setupUi(self, writeOffForm):
        writeOffForm.setObjectName("writeOffForm")
        writeOffForm.resize(983, 708)
        self.tableWidget = QtWidgets.QTableWidget(writeOffForm)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 971, 661))
        self.tableWidget.setMinimumSize(QtCore.QSize(971, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(971, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.writeOffButton = QtWidgets.QPushButton(writeOffForm)
        self.writeOffButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.writeOffButton.setObjectName("writeOffButton")

        self.retranslateUi(writeOffForm)
        QtCore.QMetaObject.connectSlotsByName(writeOffForm)

    def retranslateUi(self, writeOffForm):
        _translate = QtCore.QCoreApplication.translate
        writeOffForm.setWindowTitle(_translate("writeOffForm", "销负信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("writeOffForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("writeOffForm", "销售日期"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("writeOffForm", "商品品牌"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("writeOffForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("writeOffForm", "销售数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("writeOffForm", "单位"))
        self.writeOffButton.setText(_translate("writeOffForm", "销负"))

