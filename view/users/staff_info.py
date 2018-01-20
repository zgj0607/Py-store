from PyQt5.QtWidgets import QDialog, QMessageBox

from view.users.ui.ui_staff_info import Ui_MainWindow as UiStaffInfo
from view.utils.table_utils import set_table_content
from database.dao.users.user_handler import submit_staff_info, get_all_staff


class StaffInfo(QDialog, UiStaffInfo):
    def __init__(self, staff_table, window_title, table_tile, staff_id=None, name="", id_card_no="", sex=""):
        super(StaffInfo, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(window_title)
        self.table_title = table_tile
        self.staff_id = staff_id
        self.staff_name.setText(name)
        self.gender.setText(sex)
        self.id_card_no.setText(id_card_no)
        self.staff_table = staff_table
        self.submit.clicked.connect(self._submit)

    def _submit(self):
        name = self.staff_name.text()
        sex = self.gender.text()
        id_card_no = self.id_card_no.text()
        submit_staff_info(name, sex, id_card_no, self.staff_id)
        QMessageBox.information(self.submit, "提示", "提交成功")
        self.close()

        set_table_content(self.staff_table, get_all_staff(), self.table_title)
