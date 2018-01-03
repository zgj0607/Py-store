# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_history_buy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_historySockForm(object):
    def setupUi(self, historySockForm):
        historySockForm.setObjectName("historySockForm")
        historySockForm.resize(880, 720)
        self.lineEdit = QtWidgets.QLineEdit(historySockForm)
        self.lineEdit.setGeometry(QtCore.QRect(105, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(historySockForm)
        self.label.setGeometry(QtCore.QRect(25, 40, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(historySockForm)
        self.label_2.setGeometry(QtCore.QRect(245, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(historySockForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(315, 40, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(historySockForm)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 851, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.serchButton = QtWidgets.QPushButton(historySockForm)
        self.serchButton.setGeometry(QtCore.QRect(475, 36, 113, 32))
        self.serchButton.setObjectName("serchButton")
        self.moniButton = QtWidgets.QPushButton(historySockForm)
        self.moniButton.setGeometry(QtCore.QRect(610, 35, 113, 32))
        self.moniButton.setObjectName("moniButton")

        self.retranslateUi(historySockForm)
        QtCore.QMetaObject.connectSlotsByName(historySockForm)

    def retranslateUi(self, historySockForm):
        _translate = QtCore.QCoreApplication.translate
        historySockForm.setWindowTitle(_translate("historySockForm", "Form"))
        self.label.setText(_translate("historySockForm", "商品品牌"))
        self.label_2.setText(_translate("historySockForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("historySockForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("historySockForm", "商品品牌"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("historySockForm", "商品型号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("historySockForm", "最低进货价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("historySockForm", "进货平均价"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("historySockForm", "最后一次进货价"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("historySockForm", "操作"))
        self.serchButton.setText(_translate("historySockForm", "查询"))
        self.moniButton.setText(_translate("historySockForm", "模拟操作"))

