# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_supplier_arrears.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_supplierarrearsForm(object):
    def setupUi(self, supplierarrearsForm):
        supplierarrearsForm.setObjectName("supplierarrearsForm")
        supplierarrearsForm.resize(880, 720)
        self.tableWidget = QtWidgets.QTableWidget(supplierarrearsForm)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 851, 601))
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
        self.singleButton = QtWidgets.QPushButton(supplierarrearsForm)
        self.singleButton.setGeometry(QtCore.QRect(230, 5, 113, 32))
        self.singleButton.setObjectName("singleButton")
        self.moreButton = QtWidgets.QPushButton(supplierarrearsForm)
        self.moreButton.setGeometry(QtCore.QRect(350, 5, 113, 32))
        self.moreButton.setObjectName("moreButton")
        self.detailButton = QtWidgets.QPushButton(supplierarrearsForm)
        self.detailButton.setGeometry(QtCore.QRect(580, 4, 113, 32))
        self.detailButton.setObjectName("detailButton")
        self.label = QtWidgets.QLabel(supplierarrearsForm)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(supplierarrearsForm)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 60, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(supplierarrearsForm)
        QtCore.QMetaObject.connectSlotsByName(supplierarrearsForm)

    def retranslateUi(self, supplierarrearsForm):
        _translate = QtCore.QCoreApplication.translate
        supplierarrearsForm.setWindowTitle(_translate("supplierarrearsForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("supplierarrearsForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("supplierarrearsForm", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("supplierarrearsForm", "欠款金额"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("supplierarrearsForm", "操作"))
        self.singleButton.setText(_translate("supplierarrearsForm", "单个付款"))
        self.moreButton.setText(_translate("supplierarrearsForm", "批量付款"))
        self.detailButton.setText(_translate("supplierarrearsForm", "详情"))
        self.label.setText(_translate("supplierarrearsForm", "已选合计金额："))
        self.label_2.setText(_translate("supplierarrearsForm", "2100000"))

