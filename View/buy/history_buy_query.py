from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QCompleter

from View.buy.ui.ui_history_buy import Ui_HistorySock
from View.utils import table_utils
from database.dao.buy import buy_handler
from database.dao.stock import brand_handler, model_handler


class HistoryStock(QtWidgets.QWidget, Ui_HistorySock):
    def __init__(self):
        super(HistoryStock, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('历史进货信息')
        self.history_table_title = ('品牌ID', '型号ID', '商品品牌', '商品型号', '最低进货价', '进货平均价', '最后一次进货价')
        self.compare_table_title = ('供应商', '商品品牌', '商品型号', '进货平均价', '进货次数', '进货数量')
        self.brand_edited = False
        self.model_edited = False

        self._init_combo_box()
        self._init_table()

        self._init_signal_and_slot()

    # 初始化品牌和型号
    def _init_combo_box(self):
        self._init_brand()

    def _init_table(self):
        self._refresh_table()
        self.history_table.setColumnHidden(0, True)
        self.history_table.setColumnHidden(1, True)

    def _init_signal_and_slot(self):
        self.pushButton.clicked.connect(self._do_search)
        self.brand_combo.currentIndexChanged.connect(self._brand_index_changed)
        self.brand_combo.editTextChanged.connect(self._brand_combo_edited)
        self.history_table.clicked['QModelIndex'].connect(self._refresh_compare_table)

    def _init_brand(self):
        brands = brand_handler.get_all_brand()
        for brand in brands:
            self.brand_combo.addItem(brand[1], brand[0])
        if brands:
            brand_id = brands[0][0]
            self._refresh_model(brand_id)
        completer = QCompleter(self._get_all_brand())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.brand_combo.setCompleter(completer)

    def _brand_index_changed(self):
        self._refresh_model()
        self.brand_edited = False
        self.model_edited = False

    def _refresh_model(self, brand_id=0):
        if not brand_id:
            brand_id = self.brand_combo.currentData()
        if brand_id:
            brand_id = int(brand_id)
            models = model_handler.get_model_by_brand(brand_id)
            self.model_combo.clear()
            for model in models:
                self.model_combo.addItem(model[1], model[0])
            completer = QCompleter(self._get_all_brand())
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            self.brand_combo.setCompleter(completer)

    def _brand_combo_edited(self):
        self.brand_edited = True
        if not self.model_edited:
            self.model_combo.clear()

    def _model_combo_edited(self):
        self.model_edited = True

    # 历史进货信息查询
    def _do_search(self):
        brand_id = self.brand_combo.currentData()
        brand_name = self.brand_combo.currentText()
        model_id = self.model_combo.currentData()
        model_name = self.model_combo.currentText()

        if not brand_name and not model_name:
            QMessageBox.information(self.pushButton, '提示', '品牌和型号为空，并选择或输入！')
            return

        if not self.brand_edited and not self.model_edited:
            if model_id:
                record = buy_handler.get_history_buy_info_by_model_id(int(model_id))
            else:
                if not model_name:
                    model_name = ''
                    record = buy_handler.get_history_buy_info_by_model_name_and_brand_id(brand_id, model_name)
                else:
                    record = ()

        elif self.model_edited and not self.brand_edited:
            record = buy_handler.get_history_buy_info_by_model_name_and_brand_id(brand_id, model_name)
        else:
            record = buy_handler.get_history_buy_info_by_model_name_and_brand_name(brand_name, model_name)

        self._refresh_history_table(record)

    def _refresh_table(self, record=()):
        self._refresh_history_table(record)
        self._init_compare_table(record)

    def _refresh_history_table(self, record):
        table_utils.set_table_content(self.history_table, record, self.history_table_title)
        self.history_table.resizeColumnsToContents()

    def _init_compare_table(self, record):
        table_utils.set_table_content(self.compare_table, record, self.compare_table_title)
        self.compare_table.resizeColumnsToContents()

    def _refresh_compare_table(self, index: int):
        model_id = table_utils.get_table_current_index_info(self.history_table, 0)
        if model_id:
            record = buy_handler.get_compare_info(model_id)
            self._init_compare_table(record)

    @staticmethod
    def _get_all_brand():
        brands = []
        for brand in brand_handler.get_all_brand():
            brands.append(brand[1])

        return brands
