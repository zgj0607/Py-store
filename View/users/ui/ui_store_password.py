# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_store_password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 630)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.store_pc_info_table = QtWidgets.QTableView(Form)
        self.store_pc_info_table.setObjectName("store_pc_info_table")
        self.store_pc_info_table.horizontalHeader().setVisible(False)
        self.store_pc_info_table.horizontalHeader().setStretchLastSection(True)
        self.store_pc_info_table.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.store_pc_info_table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.store_pc_info_save = QtWidgets.QPushButton(Form)
        self.store_pc_info_save.setObjectName("store_pc_info_save")
        self.horizontalLayout_3.addWidget(self.store_pc_info_save)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.super_user_pwd_table = QtWidgets.QTableView(Form)
        self.super_user_pwd_table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.super_user_pwd_table.setAlternatingRowColors(False)
        self.super_user_pwd_table.setObjectName("super_user_pwd_table")
        self.super_user_pwd_table.horizontalHeader().setVisible(False)
        self.super_user_pwd_table.horizontalHeader().setStretchLastSection(True)
        self.super_user_pwd_table.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.super_user_pwd_table)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.update_super_user_pwd = QtWidgets.QPushButton(Form)
        self.update_super_user_pwd.setObjectName("update_super_user_pwd")
        self.horizontalLayout_4.addWidget(self.update_super_user_pwd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.store_info_table = QtWidgets.QTableView(Form)
        self.store_info_table.setObjectName("store_info_table")
        self.store_info_table.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.store_info_table)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "门店所有者信息"))
        self.store_pc_info_save.setText(_translate("Form", "保存"))
        self.label_2.setText(_translate("Form", "修改最高权限密码"))
        self.update_super_user_pwd.setText(_translate("Form", "保存"))
        self.label_3.setText(_translate("Form", "所有门店信息"))

