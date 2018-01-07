# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from View.operation.ui.ui_sub_service_operation_data import Ui_sub_serviceoperationdataForm
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from datetime import datetime
from View.utils import excel_utils, table_utils
from database.dao.operation import operation_handler


class sub_serviceoperationdataForm(QtWidgets.QWidget, Ui_sub_serviceoperationdataForm):
    def __init__(self):
        super(sub_serviceoperationdataForm, self).__init__()
        self.setupUi(self)
        self.serchButton.clicked.connect(self.serch)
        self.exportButton.clicked.connect(self.export)
        self.setWindowTitle('二级分类经营数据')
        self.sub_serviceoperationtableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_title = (
            '一级分类', '二级分类', '成交单量', '成交车次','成交数量', '成交金额', '成交毛利')
    def _retranslateUi(self):
        print('123')

    # 按照时间查询
    def serch(self):
        start_date = self.startdateTimeEdit.date().toString('yyyy-MM-dd')
        end_date = self.enddateTimeEdit.date().toString('yyyy-MM-dd')

        record = operation_handler.get_operation_by_time(start_date, end_date)
        table_utils.set_table_content_with_merge(self.sub_serviceoperationtableView, record, self.table_title)
    # 导出
    def export(self):
        model = self.sub_serviceoperationtableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.exportButton, "提示", '无二级分类经营数据明细，无法导出！')
            return
        suggest_file_name = '''二级分类经营数据-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.exportButton, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xls)")

        if ok and file_path:
            excel_utils.export_to_file(file_path, self.table_title, '二级分类经营数据', model)
            QMessageBox.information(self.exportButton, "提示", '导出成功，文件保存在: ' + file_path)




