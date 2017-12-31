# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(947, 611)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 942, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.AdminUser = QtWidgets.QTableView(self.layoutWidget)
        self.AdminUser.setMinimumSize(QtCore.QSize(940, 541))
        self.AdminUser.setObjectName("AdminUser")
        self.verticalLayout_20.addWidget(self.AdminUser)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.addUser = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addUser.sizePolicy().hasHeightForWidth())
        self.addUser.setSizePolicy(sizePolicy)
        self.addUser.setMinimumSize(QtCore.QSize(75, 58))
        self.addUser.setMaximumSize(QtCore.QSize(75, 58))
        self.addUser.setObjectName("addUser")
        self.horizontalLayout_19.addWidget(self.addUser)
        self.changeUser = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeUser.sizePolicy().hasHeightForWidth())
        self.changeUser.setSizePolicy(sizePolicy)
        self.changeUser.setMinimumSize(QtCore.QSize(75, 58))
        self.changeUser.setMaximumSize(QtCore.QSize(75, 58))
        self.changeUser.setObjectName("changeUser")
        self.horizontalLayout_19.addWidget(self.changeUser)
        self.removeUser = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeUser.sizePolicy().hasHeightForWidth())
        self.removeUser.setSizePolicy(sizePolicy)
        self.removeUser.setMinimumSize(QtCore.QSize(75, 58))
        self.removeUser.setMaximumSize(QtCore.QSize(75, 58))
        self.removeUser.setObjectName("removeUser")
        self.horizontalLayout_19.addWidget(self.removeUser)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addUser.setText(_translate("Form", "添加用户"))
        self.changeUser.setText(_translate("Form", "修改用户"))
        self.removeUser.setText(_translate("Form", "删除用户"))

