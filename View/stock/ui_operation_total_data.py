# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_operation_total_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_operationtotaldataForm(object):
    def setupUi(self, operationtotaldataForm):
        operationtotaldataForm.setObjectName("operationtotaldataForm")
        operationtotaldataForm.resize(880, 720)
        self.tableWidget = QtWidgets.QTableWidget(operationtotaldataForm)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 851, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(operationtotaldataForm)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(operationtotaldataForm)
        self.lineEdit.setGeometry(QtCore.QRect(100, 27, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(operationtotaldataForm)
        QtCore.QMetaObject.connectSlotsByName(operationtotaldataForm)

    def retranslateUi(self, operationtotaldataForm):
        _translate = QtCore.QCoreApplication.translate
        operationtotaldataForm.setWindowTitle(_translate("operationtotaldataForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("operationtotaldataForm", "到店车辆"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("operationtotaldataForm", "总产值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("operationtotaldataForm", "总毛利"))
        self.label.setText(_translate("operationtotaldataForm", "选择门店"))

