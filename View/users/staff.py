from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from View.users.staff_info import StaffInfo
from View.users.ui.ui_staff import Ui_Staff as UiStaff
from View.utils.table_utils import get_table_current_index_info, set_table_content
from database.dao.users.user_handler import delete_staff_by_id, get_all_staff


class Staff(QtWidgets.QWidget, UiStaff):
    def __init__(self):
        super(Staff, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('门店人员管理')

        self.staff_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.table_title = ("ID", '姓名', '性别', '身份证号码', '创建时间')

        self._init_signal_and_slot()

        set_table_content(self.staff_table, get_all_staff(), self.table_title)

    def _init_signal_and_slot(self):
        self.add_staff.clicked.connect(self._add_staff)
        self.delete_staff.clicked.connect(self._delete_staff)
        self.update_staff.clicked.connect(self._update_staff)

    def _add_staff(self):
        self.staff = StaffInfo(self.staff_table, '新增员工信息', self.table_title, None)
        self.staff.exec()

    def _update_staff(self):
        record_id = get_table_current_index_info(self.staff_table, 0)
        staff_name = get_table_current_index_info(self.staff_table, 1)
        sex = get_table_current_index_info(self.staff_table, 2)
        id_card_no = get_table_current_index_info(self.staff_table, 3)
        if record_id:
            staff = StaffInfo(staff_table=self.staff_table, window_title="修改员工信息", table_tile=self.table_title,
                              staff_id=record_id, name=staff_name, id_card_no=id_card_no, sex=sex)
            staff.exec()
        else:
            QtWidgets.QMessageBox.information(self.update_staff, "提示", "请选择员工")

    def _delete_staff(self):
        staff_id = get_table_current_index_info(self.staff_table, 0)
        if staff_id:
            reply = QtWidgets.QMessageBox.question(self.delete_staff, 'Message',
                                                   "是否删除此员工?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                delete_staff_by_id(staff_id)
                set_table_content(self.staff_table, get_all_staff(), self.table_title)
        else:
            QtWidgets.QMessageBox.information(self.delete_staff, "提示", "请选择员工")
