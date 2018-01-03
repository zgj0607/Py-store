# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from View.buy.ui.ui_normal_buy_dialog import Ui_Dialog
from database.dao.good import brand_handler, model_handler
from database.dao.service import service_handler
from database.dao.supplier import supplier_handler


class StockInputDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(StockInputDialog, self).__init__()
        self.setupUi(self)
        self._init_combo_box()
        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.commitButton.clicked.connect(self._commit)
        self.first_service_combo_box.currentTextChanged.connect(self._first_srv_text_change)

    def _init_combo_box(self):
        self._init_service()
        self._init_brand_and_model()
        self._init_supplier()

    def _init_service(self):
        first_srv = service_handler.get_all_first_level_service()

        self.first_service_combo_box.clear()
        for father_srv in first_srv:
            self.first_service_combo_box.addItem(father_srv[1], father_srv[0])

        self._update_second_service(first_srv[0][0])

    def _init_brand_and_model(self):
        brands = brand_handler.get_all_brand()

        brand_combo = self.brand_comboBox
        brand_combo.clear()

        for brand in brands:
            brand_combo.addItem(brand[1], brand[0])

        self._update_model(brands[0][0])

    def _init_supplier(self):
        suppliers = supplier_handler.get_all_supplier()
        supplier_combo = self.supplier_combo_box
        supplier_combo.clear()

        for supplier in suppliers:
            supplier_combo.addItem(supplier[1], supplier[0])

    def _update_second_service(self, father_id):
        second_srv = service_handler.get_second_service_by_father(father_id)
        self.second_service_combo_box.clear()
        for child_srv in second_srv:
            self.second_service_combo_box.addItem(child_srv[3], child_srv[2])

    def _update_model(self, brand_id: int):
        model_combo = self.model_combo_box
        model_combo.clear()
        models = model_handler.get_model_by_brand(brand_id)
        for model in models:
            model_combo.addItem(model[1], model[0])

    def _first_srv_text_change(self):
        father_id = self.first_service_combo_box.currentData()
        self._update_second_service(father_id)

    def _brand_text_change(self):
        brand_id = self.brand_comboBox.currentData()
        self._update_model(brand_id)

    # 进货信息录入
    def _commit(self):
        buydate = self.staff_name.text()
        goodModel = self.gender.text()
        goodBrand = self.gender.text()
        number = self.gender.text()
        goodUnit = self.gender.text()
        price = self.gender.text()
        supplierName = self.gender.text()
        payAmount = self.gender.text()
        # id_card_no = self.id_card_no.text()
        # submit_staff_info(name, sex, id_card_no, self.staff_id)
        # QMessageBox.information(self.submit, "提示", "提交成功")
        # self.close()
        # set_table_content(self.staff_table, get_all_staff(), self.table_title)
