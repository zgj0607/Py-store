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
        operationtotaldataForm.resize(953, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(operationtotaldataForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(operationtotaldataForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.start_date = QtWidgets.QDateEdit(operationtotaldataForm)
        self.start_date.setDate(QtCore.QDate(2018, 1, 1))
        self.start_date.setObjectName("start_date")
        self.horizontalLayout.addWidget(self.start_date)
        self.label_2 = QtWidgets.QLabel(operationtotaldataForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.end_date = QtWidgets.QDateEdit(operationtotaldataForm)
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 12, 1), QtCore.QTime(0, 0, 0)))
        self.end_date.setDate(QtCore.QDate(2018, 12, 1))
        self.end_date.setObjectName("end_date")
        self.horizontalLayout.addWidget(self.end_date)
        self.search = QtWidgets.QPushButton(operationtotaldataForm)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(operationtotaldataForm)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(operationtotaldataForm)
        QtCore.QMetaObject.connectSlotsByName(operationtotaldataForm)

    def retranslateUi(self, operationtotaldataForm):
        _translate = QtCore.QCoreApplication.translate
        operationtotaldataForm.setWindowTitle(_translate("operationtotaldataForm", "Form"))
        self.label.setText(_translate("operationtotaldataForm", "请选择时间"))
        self.label_2.setText(_translate("operationtotaldataForm", "---"))
        self.search.setText(_translate("operationtotaldataForm", "查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("operationtotaldataForm", "到店车辆"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("operationtotaldataForm", "总产值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("operationtotaldataForm", "总毛利"))

