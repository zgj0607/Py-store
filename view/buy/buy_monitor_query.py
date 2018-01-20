from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from common import time_utils
from view.buy.ui.ui_buy_monitor import Ui_BuyInfoMonitor
from view.utils import table_utils, excel_utils
from database.dao.buy import buy_handler


class BuyInfoMonitor(QtWidgets.QWidget, Ui_BuyInfoMonitor):
    def __init__(self):
        super(BuyInfoMonitor, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('进货监控')
        self.summary_table_title = ('一级项目ID', '二级项目ID', '一级分类', '二级分类', '进货数量', '进货金额')
        self.detail_table_title = ("ID", '进货日期', '商品品牌', '商品型号', '进货数量', '单位', '进货单价', '单品小计', '供应商ID',
                                   '供应商', '所属项目', '付款金额', '未付金额', '进货类型', '库存ID')
        self.end_date.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self.end_date.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self.start_time_str = self.start_date.date().toString('yyyy-MM-dd')
        self.end_time_str = self.end_date.date().toString('yyyy-MM-dd')
        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.pushButton.clicked.connect(self.search_summary_buy_info)
        self.summary_table.clicked['QModelIndex'].connect(self._refresh_detail_table)
        self.export.clicked.connect(self.export_buy_info)

    def _init_table(self):
        self._refresh_table([])

    def _refresh_table(self, record):
        self._refresh_summary_table(record)
        self._init_detail_table(record)

    def _refresh_summary_table(self, record):
        table_utils.set_table_content(self.summary_table, record, self.summary_table_title)
        self.summary_table.setColumnHidden(0, True)
        self.summary_table.setColumnHidden(1, True)

    def _init_detail_table(self, record):
        table_utils.set_table_content(self.detail_table, record, self.detail_table_title)
        self.detail_table.setColumnHidden(0, True)
        self.detail_table.setColumnHidden(8, True)
        self.detail_table.setColumnHidden(14, True)
        self.detail_table.resizeColumnsToContents()

    def _refresh_detail_table(self, index):
        second_srv_id = table_utils.get_table_current_index_info(self.summary_table, 1)
        if second_srv_id:
            record = buy_handler.get_detail_info(second_srv_id, self.start_time_str, self.end_time_str)
            self._init_detail_table(record)

    def search_summary_buy_info(self):
        self.start_time_str = self.start_date.date().toString('yyyy-MM-dd')
        self.end_time_str = self.end_date.date().toString('yyyy-MM-dd')
        record = buy_handler.get_buy_info_summary_by_time(self.start_time_str, self.end_time_str)

        table_utils.set_table_content_with_merge(self.summary_table, record, self.summary_table_title, 2)
        self.summary_table.setColumnHidden(0, True)
        self.summary_table.setColumnHidden(1, True)
        self.summary_table.resizeColumnsToContents()

    def export_buy_info(self):
        start_time_str = self.start_date.date().toString('yyyy-MM-dd')
        end_time_str = self.end_date.date().toString('yyyy-MM-dd')

        if start_time_str == end_time_str:
            QMessageBox.information(self.export, "提示", '请选择进货时间区间！')
            return
        QMessageBox.information(self.export, "提示", '将导出该时间段内所有进货和退货记录！')

        suggest_file_name = '''进货明细-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.export, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xlsx)")
        table_title = ('进货日期', '商品品牌', '商品型号', '进货数量', '单位', '进货单价', '单品小计',
                       '供应商', '所属项目', '付款金额', '未付金额', '进货类型')
        if ok and file_path:
            record = buy_handler.get_buy_info_detail_by_time(start_time_str, end_time_str)
            excel_utils.export_to_file_from_db(file_path, table_title, '进货明细', record)
            QMessageBox.information(self.export, "提示", '导出成功，文件保存在: ' + file_path)
