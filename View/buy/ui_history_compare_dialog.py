# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_history_compare_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_historystockDialog(object):
    def setupUi(self, historystockDialog):
        historystockDialog.setObjectName("historystockDialog")
        historystockDialog.resize(705, 499)
        self.tableWidget = QtWidgets.QTableWidget(historystockDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 661, 291))
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
        self.label = QtWidgets.QLabel(historystockDialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(historystockDialog)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 60, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(historystockDialog)
        QtCore.QMetaObject.connectSlotsByName(historystockDialog)

    def retranslateUi(self, historystockDialog):
        _translate = QtCore.QCoreApplication.translate
        historystockDialog.setWindowTitle(_translate("historystockDialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("historystockDialog", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("historystockDialog", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("historystockDialog", "进货平均价"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("historystockDialog", "进货次数"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("historystockDialog", "进货数量"))
        self.label.setText(_translate("historystockDialog", "商品品牌："))
        self.label_2.setText(_translate("historystockDialog", "马牌"))

