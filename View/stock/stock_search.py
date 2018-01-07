from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Common import time_utils
from View.stock.ui.ui_stock_search import Ui_StockSearch
from View.utils import table_utils, excel_utils
from database.dao.service import service_handler
from database.dao.stock import stock_handler, brand_handler, model_handler
from domain.stock import Stock


class StockSearch(QtWidgets.QWidget, Ui_StockSearch):
    def __init__(self):
        super(StockSearch, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('库存信息')
        self.table_title = ('一级分类', '二级分类', '品牌', '商品型号', '库存数量', '销量')
        self._init_ui()
        self._init_signal_and_slot()
    def _init_ui(self):
        table_utils.set_table_content(self.tableView, (), self.table_title)
        time_now = time_utils.get_now()
        self.start_date.setDateTime(QDateTime.fromString(time_now, 'yyyy-MM-dd hh:mm:ss'))
        self.end_date.setDateTime(QDateTime.fromString(time_now, 'yyyy-MM-dd hh:mm:ss'))

        self._init_combo_box()

    def _init_combo_box(self):
        self._init_brand()
        self._init_first_srv()

    def _init_signal_and_slot(self):
        self.seachButton.clicked.connect(self.search)
        self.exportButton.clicked.connect(self.export)

        self.brand_combo.currentIndexChanged.connect(self._brand_changed)
        self.first_srv_combo.currentIndexChanged.connect(self._first_srv_changed)

    def _init_brand(self):
        brands = brand_handler.get_all_brand()
        brand_combo = self.brand_combo
        brand_combo.addItem('请选择')
        for brand in brands:
            brand_combo.addItem(brand[1], brand[0])

        if brands:
            brand_id = brands[0][0]
            self._refresh_model(brand_id)

    def _refresh_model(self, brand_id):
        model_combo = self.model_combo
        model_combo.clear()
        model_combo.addItem('请选择')
        if brand_id:
            models = model_handler.get_model_by_brand(brand_id)

            for model in models:
                model_combo.addItem(model[1], model[0])

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

    def _brand_changed(self):
        brand_id = self.brand_combo.currentData()
        if not brand_id:
            self.model_combo.clear()
        else:
            self._refresh_model(int(brand_id))

    def _first_srv_changed(self):
        father_id = self.first_srv_combo.currentData()
        if not father_id:
            self.model_combo.clear()
        else:
            self._refresh_second_srv(int(father_id))

    def search(self):
        start_date = self.start_date.date().toString('yyyyMMdd')
        end_date = self.end_date.date().toString('yyyyMMdd')
        brand_id = self.brand_combo.currentData()
        model_id = self.model_combo.currentData()

        first_srv_id = self.first_srv_combo.currentData()
        second_srv_id = self.second_srv_combo.currentData()

        stock = Stock()

        stock.brand_id(brand_id)
        stock.model_id(model_id)
        stock.first_service_id(first_srv_id)
        stock.second_service_id(second_srv_id)

        record = stock_handler.get_stock_buy_info(stock, start_date, end_date)
        table_utils.set_table_content(self.tableView, record, self.table_title)

    def export(self):
        model = self.tableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.exportButton, "提示", '无库存明细，无法导出！')
            return
        suggest_file_name = '''库存明细-{}.xlsx'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.exportButton, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xlsx)")

        if ok and file_path:
            excel_utils.export_to_file(file_path, self.table_title, '库存明细', model)
            QMessageBox.information(self.exportButton, "提示", '导出成功，文件保存在: '+file_path)
