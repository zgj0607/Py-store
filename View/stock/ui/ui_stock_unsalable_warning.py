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
        inventoryunsalablewarningForm.resize(953, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(inventoryunsalablewarningForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exportButton = QtWidgets.QPushButton(inventoryunsalablewarningForm)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.inventorywaringtableView = QtWidgets.QTableView(inventoryunsalablewarningForm)
        self.inventorywaringtableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.inventorywaringtableView.setObjectName("inventorywaringtableView")
        self.verticalLayout.addWidget(self.inventorywaringtableView)

        self.retranslateUi(inventoryunsalablewarningForm)
        QtCore.QMetaObject.connectSlotsByName(inventoryunsalablewarningForm)

    def retranslateUi(self, inventoryunsalablewarningForm):
        _translate = QtCore.QCoreApplication.translate
        inventoryunsalablewarningForm.setWindowTitle(_translate("inventoryunsalablewarningForm", "Form"))
        self.exportButton.setText(_translate("inventoryunsalablewarningForm", "导出"))

