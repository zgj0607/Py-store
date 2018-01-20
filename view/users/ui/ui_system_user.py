# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_system_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SystemUserForm(object):
    def setupUi(self, SystemUserForm):
        SystemUserForm.setObjectName("SystemUserForm")
        SystemUserForm.resize(942, 584)
        self.verticalLayout = QtWidgets.QVBoxLayout(SystemUserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sys_user_table = QtWidgets.QTableView(SystemUserForm)
        self.sys_user_table.setMinimumSize(QtCore.QSize(940, 520))
        self.sys_user_table.setMaximumSize(QtCore.QSize(940, 520))
        self.sys_user_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sys_user_table.setObjectName("sys_user_table")
        self.sys_user_table.horizontalHeader().setStretchLastSection(True)
        self.sys_user_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.sys_user_table)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.add_sys_user = QtWidgets.QPushButton(SystemUserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sys_user.sizePolicy().hasHeightForWidth())
        self.add_sys_user.setSizePolicy(sizePolicy)
        self.add_sys_user.setMinimumSize(QtCore.QSize(75, 29))
        self.add_sys_user.setMaximumSize(QtCore.QSize(75, 29))
        self.add_sys_user.setObjectName("add_sys_user")
        self.horizontalLayout_19.addWidget(self.add_sys_user)
        self.change_sys_user = QtWidgets.QPushButton(SystemUserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_sys_user.sizePolicy().hasHeightForWidth())
        self.change_sys_user.setSizePolicy(sizePolicy)
        self.change_sys_user.setMinimumSize(QtCore.QSize(75, 29))
        self.change_sys_user.setMaximumSize(QtCore.QSize(75, 29))
        self.change_sys_user.setObjectName("change_sys_user")
        self.horizontalLayout_19.addWidget(self.change_sys_user)
        self.remove_sys_user = QtWidgets.QPushButton(SystemUserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_sys_user.sizePolicy().hasHeightForWidth())
        self.remove_sys_user.setSizePolicy(sizePolicy)
        self.remove_sys_user.setMinimumSize(QtCore.QSize(75, 29))
        self.remove_sys_user.setMaximumSize(QtCore.QSize(75, 29))
        self.remove_sys_user.setObjectName("remove_sys_user")
        self.horizontalLayout_19.addWidget(self.remove_sys_user)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.retranslateUi(SystemUserForm)
        QtCore.QMetaObject.connectSlotsByName(SystemUserForm)

    def retranslateUi(self, SystemUserForm):
        _translate = QtCore.QCoreApplication.translate
        SystemUserForm.setWindowTitle(_translate("SystemUserForm", "Form"))
        self.add_sys_user.setText(_translate("SystemUserForm", "添加用户"))
        self.change_sys_user.setText(_translate("SystemUserForm", "修改用户"))
        self.remove_sys_user.setText(_translate("SystemUserForm", "删除用户"))

