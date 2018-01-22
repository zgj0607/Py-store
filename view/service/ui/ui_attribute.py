# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_attribute.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AttributeQWidget(object):
    def setupUi(self, AttributeQWidget):
        AttributeQWidget.setObjectName("AttributeQWidget")
        AttributeQWidget.setProperty("modal", False)
        AttributeQWidget.resize(953, 601)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AttributeQWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(AttributeQWidget)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(AttributeQWidget)
        self.edit.setObjectName("edit")
        self.horizontalLayout.addWidget(self.edit)
        self.remove = QtWidgets.QPushButton(AttributeQWidget)
        self.remove.setObjectName("remove")
        self.horizontalLayout.addWidget(self.remove)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(AttributeQWidget)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AttributeQWidget)
        QtCore.QMetaObject.connectSlotsByName(AttributeQWidget)

    def retranslateUi(self, AttributeQWidget):
        _translate = QtCore.QCoreApplication.translate
        AttributeQWidget.setWindowTitle(_translate("AttributeQWidget", "QWidget"))
        self.add.setText(_translate("AttributeQWidget", "新增"))
        self.edit.setText(_translate("AttributeQWidget", "修改"))
        self.remove.setText(_translate("AttributeQWidget", "删除"))

