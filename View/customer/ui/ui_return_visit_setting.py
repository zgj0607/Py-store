# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_return_visit_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 243)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 401, 251))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 71))
        self.label.setObjectName("label")
        self.submit_set = QtWidgets.QPushButton(self.centralwidget)
        self.submit_set.setGeometry(QtCore.QRect(150, 180, 81, 31))
        self.submit_set.setObjectName("submit_set")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 100, 261, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget1 = QtWidgets.QWidget(self.layoutWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 4, 251, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.remark = QtWidgets.QLineEdit(self.layoutWidget1)
        self.remark.setObjectName("remark")
        self.horizontalLayout.addWidget(self.remark)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 261, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.do_set_next_date = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.do_set_next_date.setObjectName("do_set_next_date")
        self.horizontalLayout_3.addWidget(self.do_set_next_date)
        self.next_date = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.next_date.setDate(QtCore.QDate(2018, 2, 1))
        self.next_date.setObjectName("next_date")
        self.horizontalLayout_3.addWidget(self.next_date)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 21))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "回访设置"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.submit_set.setText(_translate("MainWindow", "确认"))
        self.label_2.setText(_translate("MainWindow", "回访备注："))
        self.do_set_next_date.setText(_translate("MainWindow", "设置二次回访时间："))
        self.next_date.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))

