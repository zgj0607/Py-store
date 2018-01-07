# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stock_unsalable_warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inventoryunsalablewarningForm(object):
    def setupUi(self, inventoryunsalablewarningForm):
        inventoryunsalablewarningForm.setObjectName("inventoryunsalablewarningForm")
        inventoryunsalablewarningForm.resize(880, 720)
        self.exportButton = QtWidgets.QPushButton(inventoryunsalablewarningForm)
        self.exportButton.setGeometry(QtCore.QRect(10, 20, 113, 32))
        self.exportButton.setObjectName("exportButton")
        self.inventorywaringtableView = QtWidgets.QTableView(inventoryunsalablewarningForm)
        self.inventorywaringtableView.setGeometry(QtCore.QRect(10, 60, 871, 621))
        self.inventorywaringtableView.setObjectName("inventorywaringtableView")

        self.retranslateUi(inventoryunsalablewarningForm)
        QtCore.QMetaObject.connectSlotsByName(inventoryunsalablewarningForm)

    def retranslateUi(self, inventoryunsalablewarningForm):
        _translate = QtCore.QCoreApplication.translate
        inventoryunsalablewarningForm.setWindowTitle(_translate("inventoryunsalablewarningForm", "Form"))
        self.exportButton.setText(_translate("inventoryunsalablewarningForm", "导出"))

