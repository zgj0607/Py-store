from PyQt5 import QtWidgets

from Common import time_utils
from View.operation.ui.ui_performance import Ui_Form as UiPerformance
from View.utils import table_utils
from database.dao.operation import operation_handler


class Performance(QtWidgets.QWidget, UiPerformance):
    def __init__(self):
        super(Performance, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('业绩报表')

        self.selected_button = "background: rgb(0, 78, 161)"
        self.unselected_button = "background: rgb(120, 170, 220)"

        self.buttons = ('today', 'week', 'month', 'year')
        self.table_title = ('一级分类', '二级分类', '成交单数', '成交金额')

        self._init_signal_and_slot()
        self._init_performance_table()

        self.performance_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.performance_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def _init_signal_and_slot(self):
        self.today.clicked.connect(self._check_today)
        self.week.clicked.connect(self._check_week)
        self.month.clicked.connect(self._check_month)
        self.year.clicked.connect(self._check_year)

    def _init_performance_table(self):
        self._check_today()

    def _change_style(self, button_name: str):
        for button in self.buttons:
            button_obj = self.__dict__[button]
            if button == button_name:
                button_obj.setStyleSheet(self.selected_button)
            else:
                button_obj.setStyleSheet(self.unselected_button)

    def _check_today(self):
        self._change_style('today')

        time_dict = time_utils.get_this_day()

        self._update_performance_table(time_dict)

    def _check_week(self):
        self._change_style('week')
        time_dict = time_utils.get_this_week()

        self._update_performance_table(time_dict)

    def _check_month(self):
        self._change_style('month')
        time_dict = time_utils.get_this_month()

        self._update_performance_table(time_dict)

    def _check_year(self):
        self._change_style('year')
        time_dict = time_utils.get_this_year()

        self._update_performance_table(time_dict)

    def _update_performance_table(self, time_dict: dict):
        all_data = operation_handler.get_performance_by_time(time_dict)
        table_utils.set_table_content_with_merge(self.performance_table, all_data, self.table_title, 0)
        self._set_total_text(all_data)

    def _set_total_text(self, record: list):
        total_num = len(record)
        total_money = 0
        for data in record:
            total_money += data[3]

        total_text = "总交易单数：{} 单\n\n总交易金额：￥{}".format(total_num, total_money)
        self.deal_price.setText(total_text)
