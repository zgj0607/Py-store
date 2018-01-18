from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from View.users.change_password import ChangePassword
from View.users.sys_user_info import SystemUserInfo
from View.users.ui.ui_system_user import Ui_SystemUserForm as UiSystemUser
from View.utils.table_utils import set_table_content, get_table_current_index_info
from database.dao.users.user_handler import get_all_sys_user, delete_sys_user_by_id


class SystemUser(QtWidgets.QDialog, UiSystemUser):
    def __init__(self):
        super(SystemUser, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('系统人员管理')

        self.sys_user_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.table_title = ("ID", '用户名', '密码', '创建时间')

        self._init_signal_and_slot()

        set_table_content(self.sys_user_table, get_all_sys_user(), self.table_title)
        self.sys_user_table.resizeColumnsToContents()

    def _init_signal_and_slot(self):
        self.add_sys_user.clicked.connect(self._add_sys_user)
        self.remove_sys_user.clicked.connect(self._remove_sys_user)
        self.change_sys_user.clicked.connect(self._change_sys_user)

    def _add_sys_user(self):
        self.admin = SystemUserInfo(self.sys_user_table, "新增管理员", self.table_title)
        self.admin.exec()

    def _change_sys_user(self):
        user_id = get_table_current_index_info(self.sys_user_table, 0)
        if user_id:
            sys_user = ChangePassword(user_id)
            sys_user.exec()
        else:
            QtWidgets.QMessageBox.information(self.change_sys_user, "提示", "请选择管理员")

    def _remove_sys_user(self):
        id = get_table_current_index_info(self.sys_user_table, 0)
        if id:
            reply = QtWidgets.QMessageBox.question(self.remove_sys_user, 'Message',
                                                   "是否删除此管理员?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                delete_sys_user_by_id(id)
                set_table_content(self.sys_user_table, get_all_sys_user(), self.table_title)
        else:
            QtWidgets.QMessageBox.information(self.remove_sys_user, "提示", "请选择一条记录")
