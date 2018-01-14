# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_history_buy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistorySock(object):
    def setupUi(self, HistorySock):
        HistorySock.setObjectName("HistorySock")
        HistorySock.resize(953, 602)
        self.verticalLayout = QtWidgets.QVBoxLayout(HistorySock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(HistorySock)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.brand_combo = QtWidgets.QComboBox(HistorySock)
        self.brand_combo.setMinimumSize(QtCore.QSize(150, 26))
        self.brand_combo.setMaximumSize(QtCore.QSize(150, 26))
        self.brand_combo.setEditable(True)
        self.brand_combo.setMaxVisibleItems(100)
        self.brand_combo.setObjectName("brand_combo")
        self.horizontalLayout.addWidget(self.brand_combo)
        self.label_2 = QtWidgets.QLabel(HistorySock)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.model_combo = QtWidgets.QComboBox(HistorySock)
        self.model_combo.setMinimumSize(QtCore.QSize(150, 26))
        self.model_combo.setMaximumSize(QtCore.QSize(150, 26))
        self.model_combo.setEditable(True)
        self.model_combo.setMaxVisibleItems(100)
        self.model_combo.setObjectName("model_combo")
        self.horizontalLayout.addWidget(self.model_combo)
        self.pushButton = QtWidgets.QPushButton(HistorySock)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.history_table = QtWidgets.QTableView(HistorySock)
        self.history_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.history_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.history_table.setObjectName("history_table")
        self.history_table.horizontalHeader().setStretchLastSection(True)
        self.history_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.history_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(HistorySock)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.compare_table = QtWidgets.QTableView(HistorySock)
        self.compare_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.compare_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.compare_table.setObjectName("compare_table")
        self.compare_table.horizontalHeader().setStretchLastSection(True)
        self.compare_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.compare_table)

        self.retranslateUi(HistorySock)
        QtCore.QMetaObject.connectSlotsByName(HistorySock)

    def retranslateUi(self, HistorySock):
        _translate = QtCore.QCoreApplication.translate
        HistorySock.setWindowTitle(_translate("HistorySock", "Form"))
        self.label.setText(_translate("HistorySock", "商品品牌"))
        self.label_2.setText(_translate("HistorySock", "商品型号"))
        self.pushButton.setText(_translate("HistorySock", "查询"))
        self.label_3.setText(_translate("HistorySock", "单品供应商对比"))

