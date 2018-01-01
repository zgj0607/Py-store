# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_monitor_two_detail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_monitortwodetailDialog(object):
    def setupUi(self, monitortwodetailDialog):
        monitortwodetailDialog.setObjectName("monitortwodetailDialog")
        monitortwodetailDialog.resize(705, 499)
        self.tableWidget = QtWidgets.QTableWidget(monitortwodetailDialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 661, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(monitortwodetailDialog)
        QtCore.QMetaObject.connectSlotsByName(monitortwodetailDialog)

    def retranslateUi(self, monitortwodetailDialog):
        _translate = QtCore.QCoreApplication.translate
        monitortwodetailDialog.setWindowTitle(_translate("monitortwodetailDialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("monitortwodetailDialog", "属性"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("monitortwodetailDialog", "实例数据"))

