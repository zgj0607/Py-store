from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QLineEdit, QWidget, QCompleter

from Common import time_utils
from View.stock.ui.ui_stock_calibration import Ui_stock_calibration
from View.utils import table_utils, excel_utils
from database.dao.service import service_handler
from database.dao.stock import stock_handler, brand_handler, model_handler
from domain.stock import Stock


class stock_calibration_review(QtWidgets.QWidget, Ui_stock_calibration):
    def __init__(self):
        super(stock_calibration_review, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('校准')
        self.table_title = ('一级分类', '二级分类', '品牌', '商品型号', '库存数量', '库存金额', '销量')
        self._init_ui()
        self._init_signal_and_slot()

    def _init_ui(self):
        table_utils.set_table_content(self.tableView, (), self.table_title)
        time_now = time_utils.get_now()
        self.start_date.setDateTime(QDateTime.fromString(time_now, 'yyyy-MM-dd hh:mm:ss'))
        self.end_date.setDateTime(QDateTime.fromString(time_now, 'yyyy-MM-dd hh:mm:ss'))

        self._init_brand_and_model()
        self._init_first_srv()

    def _init_signal_and_slot(self):
        self.seachButton.clicked.connect(self.search)
        self.exportButton.clicked.connect(self.export)

        self.first_srv_combo.currentIndexChanged.connect(self._first_srv_changed)

    def _init_brand_and_model(self):
        self._set_completer(self.brand, 'brand')
        self._set_completer(self.model, 'model')

    def _init_first_srv(self):
        first_srv_combo = self.first_srv_combo
        first_srv_combo.addItem('请选择')

        first_srvs = service_handler.get_all_first_level_service()
        for first_srv in first_srvs:
            first_srv_combo.addItem(first_srv[1], first_srv[0])

        if first_srvs:
            first_srv_id = first_srvs[0][0]
            self._refresh_second_srv(first_srv_id)

    def _refresh_second_srv(self, first_srv_id):
        second_srv_combo = self.second_srv_combo
        second_srv_combo.clear()
        second_srv_combo.addItem('请选择')
        if first_srv_id:
            second_srvs = service_handler.get_second_service_by_father(first_srv_id)
            for second_srv in second_srvs:
                second_srv_combo.addItem(second_srv[3], second_srv[2])

    def _first_srv_changed(self):
        father_id = self.first_srv_combo.currentData()
        if not father_id:
            self.model_combo.clear()
        else:
            self._refresh_second_srv(int(father_id))

    def search(self):
        start_date = self.start_date.date().toString('yyyy-MM-dd')
        end_date = self.end_date.date().toString('yyyy-MM-dd')
        brand_name = self.brand.text()
        model_name = self.model.text()

        first_srv_id = self.first_srv_combo.currentData()
        second_srv_id = self.second_srv_combo.currentData()

        stock = Stock()

        stock.brand_name(brand_name)
        stock.model_name(model_name)
        stock.first_service_id(first_srv_id)
        stock.second_service_id(second_srv_id)

        record = stock_handler.get_stock_buy_info(stock, start_date, end_date)
        table_utils.set_table_content_with_merge(self.tableView, record, self.table_title, 0)
        self.tableView.resizeColumnsToContents()

    def export(self):
        model = self.tableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.exportButton, "提示", '无库存明细，无法导出！')
            return
        suggest_file_name = '''库存明细-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.exportButton, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xlsx)")

        if ok and file_path:
            excel_utils.export_to_file_from_table_view(file_path, self.table_title, '库存明细', model)
            QMessageBox.information(self.exportButton, "提示", '导出成功，文件保存在: ' + file_path)

    def _set_completer(self, editor: QWidget, title: str):
        if isinstance(editor, QLineEdit):
            completer_list = []
            if title == 'brand':
                completer_list = self._get_all_brand()
            if title == 'model':
                completer_list = self._get_all_model()

            completer = QCompleter(completer_list)
            completer.setFilterMode(Qt.MatchContains)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            editor.setCompleter(completer)

    @staticmethod
    def _get_all_brand():
        brands = []
        for brand in brand_handler.get_all_brand():
            brands.append(brand[1])

        return brands

    @staticmethod
    def _get_all_model():
        models = []
        for model in model_handler.get_all_model():
            models.append(model[1])
        return models
