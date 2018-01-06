from PyQt5.QtWidgets import QDialog, QComboBox

from Common import Common
from Common.time_utils import get_now
from View.stock.ui.ui_add_stock import Ui_Dialog as UiAddStock
from database.dao.service import service_handler
from database.dao.stock import stock_handler
from domain.stock import Stock


class AddStock(QDialog, UiAddStock):
    def __init__(self, brand_combo: QComboBox):
        super(AddStock, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('新增商品信息')
        self._init_service()

        self.first_service_combo_box.currentIndexChanged.connect(self._first_srv_text_change)
        self.commitButton.clicked.connect(self._submit)

    # 服务项目下拉框初始化
    def _init_service(self):
        first_srv = service_handler.get_all_first_level_service()

        if first_srv:
            self.first_service_combo_box.clear()
            for father_srv in first_srv:
                self.first_service_combo_box.addItem(father_srv[1], father_srv[0])

            self._update_second_service(first_srv[0][0])

    # 一级服务项目下拉联动出发二级服务项目变更
    def _first_srv_text_change(self):
        father_id = self.first_service_combo_box.currentData()
        self._update_second_service(father_id)

    # 二级服务项目初始化
    def _update_second_service(self, father_id):
        self.second_service_combo_box.clear()

        second_srv = service_handler.get_second_service_by_father(father_id)
        for child_srv in second_srv:
            self.second_service_combo_box.addItem(child_srv[3], child_srv[2])

    def _submit(self):
        stock = Stock()

        brand = self.brand_comboBox
        stock.brand_name(brand.currentText()).brand_id(brand.currentData())

        model = self.model_combo_box
        stock.model_name(model.currentText()).model_id(model.currentData())

        first_service = self.first_service_combo_box
        stock.first_service_id(first_service.currentData()).first_service_name(first_service.currentText())

        second_service = self.second_service_combo_box
        stock.second_service_name(second_service.currentText()).second_service_id(second_service.currentData())

        name = brand.currentText()+'-'+model.currentText()
        stock.name(name)
        stock.unit(self.unit.text())
        stock.create_op(Common.config.login_user_info[0])
        stock.create_time(get_now())

        stock_id = stock_handler.add_stock_info(stock)

        stock.id(stock_id)
