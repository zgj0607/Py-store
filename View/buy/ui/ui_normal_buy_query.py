# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_normal_buy_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_stockQueryForm(object):
    def setupUi(self, stockQueryForm):
        stockQueryForm.setObjectName("stockQueryForm")
        stockQueryForm.resize(953, 602)
        self.addButton = QtWidgets.QPushButton(stockQueryForm)
        self.addButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(stockQueryForm)
        self.editButton.setGeometry(QtCore.QRect(120, 10, 113, 32))
        self.editButton.setObjectName("editButton")
        self.stocktableView = QtWidgets.QTableView(stockQueryForm)
        self.stocktableView.setGeometry(QtCore.QRect(0, 50, 951, 550))
        self.stocktableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.stocktableView.setObjectName("stocktableView")

        self.retranslateUi(stockQueryForm)
        QtCore.QMetaObject.connectSlotsByName(stockQueryForm)

    def retranslateUi(self, stockQueryForm):
        _translate = QtCore.QCoreApplication.translate
        stockQueryForm.setWindowTitle(_translate("stockQueryForm", "进货信息"))
        self.addButton.setText(_translate("stockQueryForm", "录入"))
        self.editButton.setText(_translate("stockQueryForm", "修改"))

