import traceback

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog

from Common import time_utils
from View.sale.excel_process import ExcelProcess
from View.sale.ui.ui_sale_detail import Ui_SaleDetail as SaleDetail
from View.utils import table_utils


class SaleBase(QtWidgets.QWidget, SaleDetail):
    def __init__(self):
        super(SaleBase, self).__init__()
        self.setupUi(self)
        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)
        self._signal_slot_init()

        self.table_title = (
            '订单号', '消费时间', '消费门店', '车牌号', '车主姓名', '联系电话', '车型', '操作人员', '消费项目', '数量', '单价', '小计', '总价', '单位', '备注')

        self._init_table()

        self._init_date()

    def _init_date(self):
        date_dict = time_utils.get_this_year()
        start_date = date_dict['start_time'] + " 00:00:00"
        end_date = date_dict['end_time'] + " 00:00:00"
        self.start_date.setDateTime(QDateTime.fromString(start_date, 'yyyy-MM-dd hh:mm:ss'))
        self.end_date.setDateTime(QDateTime.fromString(end_date, 'yyyy-MM-dd hh:mm:ss'))

    def _init_table(self):
        table_utils.set_table_content(self.sales_details_result_table, [], self.table_title)

    def _signal_slot_init(self):
        self.details_import_button.clicked.connect(self._sale_detail_import)
        self.details_export_button.clicked.connect(self._sale_detail_export)

    def _sale_detail_import(self):
        file_dialog = QFileDialog()
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(file_dialog, "选取文件", "C:/",
                                                                     "Text Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,注意用分号间隔
        if file_name:
            try:
                excel_handler = ExcelProcess()
                excel_handler.import_sale_detail(file_name, self)
                QtWidgets.QMessageBox.information(self.details_import_button, "提示", "导入成功")
            except Exception as e:
                print(e)
                print('traceback.print_exc():{}'.format(traceback.print_exc()))
                print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                QtWidgets.QMessageBox.information(self.details_import_button, "提示", "文件错误")

    def _sale_detail_export(self):
        start_time = self.start_date.text()
        end_time = self.end_date.text()
        excel_handler = ExcelProcess()
        file_name = excel_handler.export_sale_detail(start_time, end_time)
        if file_name:
            QtWidgets.QMessageBox.information(self.details_export_button, "提示", "文件名为：{}".format(file_name))
        else:
            QtWidgets.QMessageBox.information(self.details_export_button, "提示", "暂无消费记录")

    def _result_process(self, result_str):
        if result_str:
            pass
        elif not result_str:
            QtWidgets.QMessageBox.information(self.details_query_button, "提示", "暂无消费记录")
        elif result_str == 'restart':
            QtWidgets.QMessageBox.information(self.details_query_button, "提示", "与服务器链接中断，请重新运行软件")
        else:
            pass
