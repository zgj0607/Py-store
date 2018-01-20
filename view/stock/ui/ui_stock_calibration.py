# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stock_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_stock_calibration(object):
    def setupUi(self, stock_calibration):
        stock_calibration.setObjectName("stock_calibration")
        stock_calibration.resize(953, 603)
        self.verticalLayout = QtWidgets.QVBoxLayout(stock_calibration)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(stock_calibration)
        self.label_3.setMinimumSize(QtCore.QSize(60, 26))
        self.label_3.setMaximumSize(QtCore.QSize(60, 26))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.second_srv_combo = QtWidgets.QComboBox(stock_calibration)
        self.second_srv_combo.setMinimumSize(QtCore.QSize(135, 26))
        self.second_srv_combo.setMaximumSize(QtCore.QSize(135, 26))
        self.second_srv_combo.setObjectName("second_srv_combo")
        self.horizontalLayout_2.addWidget(self.second_srv_combo)
        self.seachButton = QtWidgets.QPushButton(stock_calibration)
        self.seachButton.setMinimumSize(QtCore.QSize(90, 26))
        self.seachButton.setMaximumSize(QtCore.QSize(90, 26))
        self.seachButton.setObjectName("seachButton")
        self.horizontalLayout_2.addWidget(self.seachButton)
        self.calibrationButton = QtWidgets.QPushButton(stock_calibration)
        self.calibrationButton.setMinimumSize(QtCore.QSize(90, 26))
        self.calibrationButton.setMaximumSize(QtCore.QSize(90, 26))
        self.calibrationButton.setObjectName("calibrationButton")
        self.horizontalLayout_2.addWidget(self.calibrationButton)
        self.pushButton = QtWidgets.QPushButton(stock_calibration)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 26))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 26))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.tableView = QtWidgets.QTableView(stock_calibration)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(stock_calibration)
        QtCore.QMetaObject.connectSlotsByName(stock_calibration)

    def retranslateUi(self, stock_calibration):
        _translate = QtCore.QCoreApplication.translate
        stock_calibration.setWindowTitle(_translate("stock_calibration", "Form"))
        self.label_3.setText(_translate("stock_calibration", "审核状态"))
        self.seachButton.setText(_translate("stock_calibration", "查询"))
        self.calibrationButton.setText(_translate("stock_calibration", "校准"))
        self.pushButton.setText(_translate("stock_calibration", "审核"))

