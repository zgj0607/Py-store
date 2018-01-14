from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from View.operation.ui.ui_sub_service_operation_data import Ui_sub_serviceoperationdataForm
from View.utils import excel_utils, table_utils
from database.dao.operation import operation_handler


class SubServiceOperationData(QtWidgets.QWidget, Ui_sub_serviceoperationdataForm):
    def __init__(self):
        super(SubServiceOperationData, self).__init__()
        self.setupUi(self)
        self.search.clicked.connect(self._do_search)
        self.export.clicked.connect(self._do_export)
        self.setWindowTitle('二级分类经营数据')
        self.sub_serviceoperationtableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_title = (
            '一级分类', '二级分类', '成交单量', '成交车次', '成交数量', '成交金额', '成交毛利')

    # 按照时间查询
    def _do_search(self):
        start_date = self.start_date.date().toString('yyyy-MM-dd')
        end_date = self.end_date.date().toString('yyyy-MM-dd')

        record = operation_handler.get_operation_by_time(start_date, end_date)
        table_utils.set_table_content_with_merge(self.sub_serviceoperationtableView, record, self.table_title)

    # 导出
    def _do_export(self):
        model = self.sub_serviceoperationtableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.export, "提示", '无二级分类经营数据明细，无法导出！')
            return
        suggest_file_name = '''二级分类经营数据-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.export, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xls)")

        if ok and file_path:
            excel_utils.export_to_file_from_table_view(file_path, self.table_title, '二级分类经营数据', model)
            QMessageBox.information(self.export, "提示", '导出成功，文件保存在: ' + file_path)
