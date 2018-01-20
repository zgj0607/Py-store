# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_staff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Staff(object):
    def setupUi(self, Staff):
        Staff.setObjectName("Staff")
        Staff.resize(951, 583)
        self.verticalLayout = QtWidgets.QVBoxLayout(Staff)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_staff = QtWidgets.QPushButton(Staff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_staff.sizePolicy().hasHeightForWidth())
        self.add_staff.setSizePolicy(sizePolicy)
        self.add_staff.setMinimumSize(QtCore.QSize(90, 29))
        self.add_staff.setMaximumSize(QtCore.QSize(90, 29))
        self.add_staff.setObjectName("add_staff")
        self.horizontalLayout_4.addWidget(self.add_staff)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.staff_table = QtWidgets.QTableView(Staff)
        self.staff_table.setMinimumSize(QtCore.QSize(951, 480))
        self.staff_table.setMaximumSize(QtCore.QSize(941, 480))
        self.staff_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.staff_table.setSortingEnabled(True)
        self.staff_table.setObjectName("staff_table")
        self.staff_table.horizontalHeader().setStretchLastSection(True)
        self.staff_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.staff_table)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.delete_staff = QtWidgets.QPushButton(Staff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_staff.sizePolicy().hasHeightForWidth())
        self.delete_staff.setSizePolicy(sizePolicy)
        self.delete_staff.setMinimumSize(QtCore.QSize(75, 29))
        self.delete_staff.setMaximumSize(QtCore.QSize(75, 29))
        self.delete_staff.setObjectName("delete_staff")
        self.horizontalLayout_13.addWidget(self.delete_staff)
        self.update_staff = QtWidgets.QPushButton(Staff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_staff.sizePolicy().hasHeightForWidth())
        self.update_staff.setSizePolicy(sizePolicy)
        self.update_staff.setMinimumSize(QtCore.QSize(75, 29))
        self.update_staff.setMaximumSize(QtCore.QSize(75, 29))
        self.update_staff.setObjectName("update_staff")
        self.horizontalLayout_13.addWidget(self.update_staff)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.retranslateUi(Staff)
        QtCore.QMetaObject.connectSlotsByName(Staff)

    def retranslateUi(self, Staff):
        _translate = QtCore.QCoreApplication.translate
        Staff.setWindowTitle(_translate("Staff", "Form"))
        self.add_staff.setText(_translate("Staff", "新增员工"))
        self.delete_staff.setText(_translate("Staff", "删除"))
        self.update_staff.setText(_translate("Staff", "修改"))

