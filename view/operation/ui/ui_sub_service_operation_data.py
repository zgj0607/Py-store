# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sub_service_operation_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sub_serviceoperationdataForm(object):
    def setupUi(self, sub_serviceoperationdataForm):
        sub_serviceoperationdataForm.setObjectName("sub_serviceoperationdataForm")
        sub_serviceoperationdataForm.resize(953, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(sub_serviceoperationdataForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(sub_serviceoperationdataForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.start_date = QtWidgets.QDateTimeEdit(sub_serviceoperationdataForm)
        self.start_date.setDate(QtCore.QDate(2018, 1, 1))
        self.start_date.setObjectName("start_date")
        self.horizontalLayout.addWidget(self.start_date)
        self.label_2 = QtWidgets.QLabel(sub_serviceoperationdataForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.end_date = QtWidgets.QDateTimeEdit(sub_serviceoperationdataForm)
        self.end_date.setDate(QtCore.QDate(2018, 12, 1))
        self.end_date.setObjectName("end_date")
        self.horizontalLayout.addWidget(self.end_date)
        self.search = QtWidgets.QPushButton(sub_serviceoperationdataForm)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.export = QtWidgets.QPushButton(sub_serviceoperationdataForm)
        self.export.setObjectName("export")
        self.horizontalLayout.addWidget(self.export)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sub_serviceoperationtableView = QtWidgets.QTableView(sub_serviceoperationdataForm)
        self.sub_serviceoperationtableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sub_serviceoperationtableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sub_serviceoperationtableView.setObjectName("sub_serviceoperationtableView")
        self.verticalLayout.addWidget(self.sub_serviceoperationtableView)

        self.retranslateUi(sub_serviceoperationdataForm)
        QtCore.QMetaObject.connectSlotsByName(sub_serviceoperationdataForm)

    def retranslateUi(self, sub_serviceoperationdataForm):
        _translate = QtCore.QCoreApplication.translate
        sub_serviceoperationdataForm.setWindowTitle(_translate("sub_serviceoperationdataForm", "Form"))
        self.label.setText(_translate("sub_serviceoperationdataForm", "请选择时间"))
        self.start_date.setDisplayFormat(_translate("sub_serviceoperationdataForm", "yyyy-MM-dd"))
        self.label_2.setText(_translate("sub_serviceoperationdataForm", "---"))
        self.end_date.setDisplayFormat(_translate("sub_serviceoperationdataForm", "yyyy-MM-dd"))
        self.search.setText(_translate("sub_serviceoperationdataForm", "查询"))
        self.export.setText(_translate("sub_serviceoperationdataForm", "导出"))

