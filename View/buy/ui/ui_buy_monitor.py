# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_buy_monitor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BuyInfoMonitor(object):
    def setupUi(self, BuyInfoMonitor):
        BuyInfoMonitor.setObjectName("BuyInfoMonitor")
        BuyInfoMonitor.resize(953, 602)
        self.verticalLayout = QtWidgets.QVBoxLayout(BuyInfoMonitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(BuyInfoMonitor)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.start_date = QtWidgets.QDateEdit(BuyInfoMonitor)
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setObjectName("start_date")
        self.horizontalLayout.addWidget(self.start_date)
        self.label_2 = QtWidgets.QLabel(BuyInfoMonitor)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.end_date = QtWidgets.QDateEdit(BuyInfoMonitor)
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date.setObjectName("end_date")
        self.horizontalLayout.addWidget(self.end_date)
        self.pushButton = QtWidgets.QPushButton(BuyInfoMonitor)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.summary_table = QtWidgets.QTableView(BuyInfoMonitor)
        self.summary_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.summary_table.setObjectName("summary_table")
        self.summary_table.verticalHeader().setVisible(False)
        self.summary_table.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.summary_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(BuyInfoMonitor)
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
        self.detail_table = QtWidgets.QTableView(BuyInfoMonitor)
        self.detail_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detail_table.setObjectName("detail_table")
        self.detail_table.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.detail_table)

        self.retranslateUi(BuyInfoMonitor)
        QtCore.QMetaObject.connectSlotsByName(BuyInfoMonitor)

    def retranslateUi(self, BuyInfoMonitor):
        _translate = QtCore.QCoreApplication.translate
        BuyInfoMonitor.setWindowTitle(_translate("BuyInfoMonitor", "Form"))
        self.label.setText(_translate("BuyInfoMonitor", "起始时间"))
        self.start_date.setDisplayFormat(_translate("BuyInfoMonitor", "yyyyMMdd"))
        self.label_2.setText(_translate("BuyInfoMonitor", "结束时间"))
        self.end_date.setDisplayFormat(_translate("BuyInfoMonitor", "yyyyMMdd"))
        self.pushButton.setText(_translate("BuyInfoMonitor", "查询"))
        self.label_3.setText(_translate("BuyInfoMonitor", "进货明细"))

