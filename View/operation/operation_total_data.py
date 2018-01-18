from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime

from Common import time_utils
from View.operation.ui.ui_operation_total_data import Ui_operationtotaldataForm
from View.utils import table_utils
from database.dao.operation import operation_handler


class OperationTotalData(QtWidgets.QWidget, Ui_operationtotaldataForm):
    def __init__(self):
        super(OperationTotalData, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('总体经营数据')
        self.table_title = ('到店车辆', '总产值', '总毛利')

        self.search.clicked.connect(self._do_search)

        self._init_date()

    def _init_date(self):
        date_dict = time_utils.get_this_year()
        start_date = date_dict['start_time'] + " 00:00:00"
        end_date = date_dict['end_time'] + " 00:00:00"
        self.start_date.setDateTime(QDateTime.fromString(start_date, 'yyyy-MM-dd hh:mm:ss'))
        self.end_date.setDateTime(QDateTime.fromString(end_date, 'yyyy-MM-dd hh:mm:ss'))

    # 历史进货信息查询
    def _do_search(self):
        start_time = self.start_date.date().toString('yyyy-MM-dd')
        end_time = self.end_date.date().toString('yyyy-MM-dd')
        record = operation_handler.get_total_operation_by_time(start_time, end_time)
        table_utils.set_table_widget_content(self.tableWidget, record, self.table_title)
        print(start_time, end_time)
