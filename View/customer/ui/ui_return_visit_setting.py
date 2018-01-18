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
        MainWindow.resize(333, 258)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setMinimumSize(QtCore.QSize(160, 0))
        self.info_label.setMaximumSize(QtCore.QSize(240, 16777215))
        self.info_label.setText("")
        self.info_label.setIndent(-1)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget1 = QtWidgets.QWidget(self.layoutWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 4, 258, 31))
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
        self.verticalLayout.addWidget(self.layoutWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
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
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.submit_set = QtWidgets.QPushButton(self.centralwidget)
        self.submit_set.setObjectName("submit_set")
        self.horizontalLayout_4.addWidget(self.submit_set)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "回访设置"))
        self.label_2.setText(_translate("MainWindow", "回访备注："))
        self.do_set_next_date.setText(_translate("MainWindow", "设置二次回访时间："))
        self.next_date.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.submit_set.setText(_translate("MainWindow", "确认"))

