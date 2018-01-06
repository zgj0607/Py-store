# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_write_off_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_writeOffForm(object):
    def setupUi(self, writeOffForm):
        writeOffForm.setObjectName("writeOffForm")
        writeOffForm.resize(953, 602)
        self.writeOffButton = QtWidgets.QPushButton(writeOffForm)
        self.writeOffButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.writeOffButton.setObjectName("writeOffButton")
        self.write_off_table = QtWidgets.QTableView(writeOffForm)
        self.write_off_table.setGeometry(QtCore.QRect(0, 50, 951, 550))
        self.write_off_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.write_off_table.setSortingEnabled(True)
        self.write_off_table.setObjectName("write_off_table")
        self.write_off_table.verticalHeader().setVisible(False)

        self.retranslateUi(writeOffForm)
        QtCore.QMetaObject.connectSlotsByName(writeOffForm)

    def retranslateUi(self, writeOffForm):
        _translate = QtCore.QCoreApplication.translate
        writeOffForm.setWindowTitle(_translate("writeOffForm", "销负信息"))
        self.writeOffButton.setText(_translate("writeOffForm", "销负"))

