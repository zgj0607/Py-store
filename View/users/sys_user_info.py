from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Common.StaticFunc import md5
from View.users.ui.ui_sys_user_info import Ui_MainWindow as UiSysUserInfo
from View.utils.table_utils import set_table_content
from database.dao.users.user_handler import get_all_sys_user, insert_sys_user_info


class SystemUserInfo(QtWidgets.QDialog, UiSysUserInfo):
    def __init__(self, sys_user_table, window_title, table_title):
        super(SystemUserInfo, self).__init__()
        self.setupUi(self)

        self.sys_user_table = sys_user_table
        self.setWindowTitle(window_title)
        self.table_title = table_title

        self.submit.clicked.connect(self._submit)

    def _submit(self):
        name = self.username.text()
        pwd = self.password.text() + 'udontknowwhy'
        pwd = md5(pwd)

        insert_sys_user_info(name, pwd)

        QMessageBox.information(self.submit, "提示", "提交成功")
        self.close()

        # 刷新页面显示内容
        set_table_content(self.sys_user_table, get_all_sys_user(), self.table_title)
