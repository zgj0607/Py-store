# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_return_visit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReturnVisit(object):
    def setupUi(self, ReturnVisit):
        ReturnVisit.setObjectName("ReturnVisit")
        ReturnVisit.resize(943, 594)
        self.layoutWidget = QtWidgets.QWidget(ReturnVisit)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 943, 595))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.return_visit_table = QtWidgets.QTableView(self.layoutWidget)
        self.return_visit_table.setMinimumSize(QtCore.QSize(941, 551))
        self.return_visit_table.setObjectName("return_visit_table")
        self.verticalLayout_11.addWidget(self.return_visit_table)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.return_visit_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_visit_button.sizePolicy().hasHeightForWidth())
        self.return_visit_button.setSizePolicy(sizePolicy)
        self.return_visit_button.setMinimumSize(QtCore.QSize(75, 29))
        self.return_visit_button.setMaximumSize(QtCore.QSize(75, 29))
        self.return_visit_button.setObjectName("return_visit_button")
        self.horizontalLayout_17.addWidget(self.return_visit_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.retranslateUi(ReturnVisit)
        QtCore.QMetaObject.connectSlotsByName(ReturnVisit)

    def retranslateUi(self, ReturnVisit):
        _translate = QtCore.QCoreApplication.translate
        ReturnVisit.setWindowTitle(_translate("ReturnVisit", "Form"))
        self.return_visit_button.setText(_translate("ReturnVisit", "回访"))

