# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_attribute_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AttributeDialog(object):
    def setupUi(self, AttributeDialog):
        AttributeDialog.setObjectName("AttributeDialog")
        AttributeDialog.resize(953, 601)
        AttributeDialog.setModal(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AttributeDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(AttributeDialog)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(AttributeDialog)
        self.edit.setObjectName("edit")
        self.horizontalLayout.addWidget(self.edit)
        self.remove = QtWidgets.QPushButton(AttributeDialog)
        self.remove.setObjectName("remove")
        self.horizontalLayout.addWidget(self.remove)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(AttributeDialog)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AttributeDialog)
        QtCore.QMetaObject.connectSlotsByName(AttributeDialog)

    def retranslateUi(self, AttributeDialog):
        _translate = QtCore.QCoreApplication.translate
        AttributeDialog.setWindowTitle(_translate("AttributeDialog", "Dialog"))
        self.add.setText(_translate("AttributeDialog", "新增"))
        self.edit.setText(_translate("AttributeDialog", "修改"))
        self.remove.setText(_translate("AttributeDialog", "删除"))

