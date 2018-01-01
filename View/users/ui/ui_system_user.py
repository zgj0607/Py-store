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
        SystemUserForm.resize(947, 611)
        self.layoutWidget = QtWidgets.QWidget(SystemUserForm)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 942, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.sys_user_table = QtWidgets.QTableView(self.layoutWidget)
        self.sys_user_table.setMinimumSize(QtCore.QSize(940, 541))
        self.sys_user_table.setObjectName("sys_user_table")
        self.verticalLayout_20.addWidget(self.sys_user_table)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.add_sys_user = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sys_user.sizePolicy().hasHeightForWidth())
        self.add_sys_user.setSizePolicy(sizePolicy)
        self.add_sys_user.setMinimumSize(QtCore.QSize(75, 58))
        self.add_sys_user.setMaximumSize(QtCore.QSize(75, 58))
        self.add_sys_user.setObjectName("add_sys_user")
        self.horizontalLayout_19.addWidget(self.add_sys_user)
        self.change_sys_user = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_sys_user.sizePolicy().hasHeightForWidth())
        self.change_sys_user.setSizePolicy(sizePolicy)
        self.change_sys_user.setMinimumSize(QtCore.QSize(75, 58))
        self.change_sys_user.setMaximumSize(QtCore.QSize(75, 58))
        self.change_sys_user.setObjectName("change_sys_user")
        self.horizontalLayout_19.addWidget(self.change_sys_user)
        self.remove_sys_user = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_sys_user.sizePolicy().hasHeightForWidth())
        self.remove_sys_user.setSizePolicy(sizePolicy)
        self.remove_sys_user.setMinimumSize(QtCore.QSize(75, 58))
        self.remove_sys_user.setMaximumSize(QtCore.QSize(75, 58))
        self.remove_sys_user.setObjectName("remove_sys_user")
        self.horizontalLayout_19.addWidget(self.remove_sys_user)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.retranslateUi(SystemUserForm)
        QtCore.QMetaObject.connectSlotsByName(SystemUserForm)

    def retranslateUi(self, SystemUserForm):
        _translate = QtCore.QCoreApplication.translate
        SystemUserForm.setWindowTitle(_translate("SystemUserForm", "Form"))
        self.add_sys_user.setText(_translate("SystemUserForm", "添加用户"))
        self.change_sys_user.setText(_translate("SystemUserForm", "修改用户"))
        self.remove_sys_user.setText(_translate("SystemUserForm", "删除用户"))

