# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_change_password.ui'
#
# Created: Fri Mar 24 13:27:58 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from view.users.ui.ui_change_password import Ui_ChangePwd as UiChangePwd
from database.dao.users.user_handler import update_sys_user_pwd


class ChangePassword(QtWidgets.QDialog, UiChangePwd):
    def __init__(self, sys_user_id):
        super(ChangePassword, self).__init__()
        self.sys_user_id = sys_user_id
        self.setupUi(self)

        self.confirm.clicked.connect(self._update)

    def _update(self):
        pwd_one = self.password_one.text()
        pwd_two = self.password_two.text()
        if pwd_one == "":
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "请输入密码")
        elif pwd_one != pwd_two:
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "两次密码输入不一致")
        else:
            pwd_one += "udontknowwhy"
            update_sys_user_pwd(self.sys_user_id, pwd_one)
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "修改成功")
            self.close()
