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
        sub_serviceoperationdataForm.resize(880, 720)
        self.horizontalLayoutWidget = QtWidgets.QWidget(sub_serviceoperationdataForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 731, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.startdateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.startdateTimeEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.startdateTimeEdit.setObjectName("startdateTimeEdit")
        self.horizontalLayout.addWidget(self.startdateTimeEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.enddateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.enddateTimeEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.enddateTimeEdit.setObjectName("enddateTimeEdit")
        self.horizontalLayout.addWidget(self.enddateTimeEdit)
        self.serchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.serchButton.setObjectName("serchButton")
        self.horizontalLayout.addWidget(self.serchButton)
        self.exportButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        self.sub_serviceoperationtableView = QtWidgets.QTableView(sub_serviceoperationdataForm)
        self.sub_serviceoperationtableView.setGeometry(QtCore.QRect(20, 100, 741, 551))
        self.sub_serviceoperationtableView.setObjectName("sub_serviceoperationtableView")

        self.retranslateUi(sub_serviceoperationdataForm)
        QtCore.QMetaObject.connectSlotsByName(sub_serviceoperationdataForm)

    def retranslateUi(self, sub_serviceoperationdataForm):
        _translate = QtCore.QCoreApplication.translate
        sub_serviceoperationdataForm.setWindowTitle(_translate("sub_serviceoperationdataForm", "Form"))
        self.label_3.setText(_translate("sub_serviceoperationdataForm", "选择门店"))
        self.label.setText(_translate("sub_serviceoperationdataForm", "起始时间"))
        self.startdateTimeEdit.setDisplayFormat(_translate("sub_serviceoperationdataForm", "yyyy-MM-dd"))
        self.label_2.setText(_translate("sub_serviceoperationdataForm", "结束时间"))
        self.enddateTimeEdit.setDisplayFormat(_translate("sub_serviceoperationdataForm", "yyyy-MM-dd"))
        self.serchButton.setText(_translate("sub_serviceoperationdataForm", "查询"))
        self.exportButton.setText(_translate("sub_serviceoperationdataForm", "导出"))

