from PyQt5 import QtWidgets

from View.customer.return_visit_setting import ReturnVisitSetting
from View.customer.ui.ui_return_visit import Ui_ReturnVisit as UiReturnVisit
from View.utils import table_utils
from View.utils.table_utils import get_table_current_index_info
from database.dao.customer import customer_handler


class ReturnVisit(QtWidgets.QWidget, UiReturnVisit):
    def __init__(self):
        super(ReturnVisit, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('客户回访')
        self.title_list = ["ID", '回访用户', '车牌号', '联系方式', '回访时间']

        self._init_table_title()

        self.return_visit_button.clicked.connect(self._return_visit_process)

    def _init_table_title(self):
        return_visit_list = customer_handler.get_return_visit_info()
        table_utils.set_table_content(self.return_visit_table, return_visit_list, self.title_list)

    def _return_visit_process(self):
        record_id = get_table_current_index_info(self.return_visit_table, 0)
        if record_id:
            username = get_table_current_index_info(self.return_visit_table, 1)
            car_id = get_table_current_index_info(self.return_visit_table, 2)
            car_phone = get_table_current_index_info(self.return_visit_table, 3)
            return_visit_date = get_table_current_index_info(self.return_visit_table, 4)
            ui = ReturnVisitSetting(return_visit_date, record_id, car_phone, car_id, username)
            ui.exec_()
            self._init_table_title()
        else:
            QtWidgets.QMessageBox.information(self.return_visit_button, "提示", "请选择未回访记录")
