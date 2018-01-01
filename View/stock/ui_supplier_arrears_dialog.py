# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_supplier_arrears_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_supplierarrearsDialog(object):
    def setupUi(self, supplierarrearsDialog):
        supplierarrearsDialog.setObjectName("supplierarrearsDialog")
        supplierarrearsDialog.resize(705, 499)
        supplierarrearsDialog.setModal(True)
        self.tableWidget = QtWidgets.QTableWidget(supplierarrearsDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 661, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(supplierarrearsDialog)
        QtCore.QMetaObject.connectSlotsByName(supplierarrearsDialog)

    def retranslateUi(self, supplierarrearsDialog):
        _translate = QtCore.QCoreApplication.translate
        supplierarrearsDialog.setWindowTitle(_translate("supplierarrearsDialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("supplierarrearsDialog", "属性"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("supplierarrearsDialog", "实例数据"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("supplierarrearsDialog", "说明"))

