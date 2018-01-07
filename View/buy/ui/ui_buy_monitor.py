# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_buy_monitor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_historymonitorForm(object):
    def setupUi(self, historymonitorForm):
        historymonitorForm.setObjectName("historymonitorForm")
        historymonitorForm.resize(880, 720)
        self.label = QtWidgets.QLabel(historymonitorForm)
        self.label.setGeometry(QtCore.QRect(25, 40, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(historymonitorForm)
        self.label_2.setGeometry(QtCore.QRect(245, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(historymonitorForm)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 851, 601))
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
        self.serchButton = QtWidgets.QPushButton(historymonitorForm)
        self.serchButton.setGeometry(QtCore.QRect(475, 36, 113, 32))
        self.serchButton.setObjectName("serchButton")
        self.moniButton = QtWidgets.QPushButton(historymonitorForm)
        self.moniButton.setGeometry(QtCore.QRect(610, 35, 113, 32))
        self.moniButton.setObjectName("moniButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(historymonitorForm)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 36, 141, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(historymonitorForm)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(310, 37, 141, 24))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(historymonitorForm)
        QtCore.QMetaObject.connectSlotsByName(historymonitorForm)

    def retranslateUi(self, historymonitorForm):
        _translate = QtCore.QCoreApplication.translate
        historymonitorForm.setWindowTitle(_translate("historymonitorForm", "Form"))
        self.label.setText(_translate("historymonitorForm", "起始时间"))
        self.label_2.setText(_translate("historymonitorForm", "结束时间"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("historymonitorForm", "一级分类"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("historymonitorForm", "二级分类"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("historymonitorForm", "进货数量"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("historymonitorForm", "进货金额"))
        self.serchButton.setText(_translate("historymonitorForm", "查询"))
        self.moniButton.setText(_translate("historymonitorForm", "模拟操作"))

