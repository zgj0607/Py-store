# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from View.buy.ui.ui_write_off_query import Ui_writeOffForm
from View.buy.write_off_dialog import WriteOffDialog
from View.utils import table_utils
from database.dao.stock import stock_detail_handler
from domain.stock import Stock


class WriteOff(QtWidgets.QWidget, Ui_writeOffForm):
    def __init__(self):
        super(WriteOff, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销负进货信息')
        self.writeOffButton.clicked.connect(self.do_write_off)

        self.table_title = ('序号', '销售日期', '商品品牌', '商品型号', '销售数量', '库存数量', '单位',
                            '品牌ID', '型号ID', '库存ID', '一级项目', '一级项目ID', '二级项目', '二级项目ID')

        self._init_write_off_table()

    def _init_write_off_table(self):
        write_off_date = stock_detail_handler.get_negative_on_hand()
        table_utils.set_table_content(self.write_off_table, write_off_date, self.table_title)
        self.write_off_table.setColumnHidden(7, True)
        self.write_off_table.setColumnHidden(8, True)
        self.write_off_table.setColumnHidden(9, True)
        self.write_off_table.setColumnHidden(11, True)
        self.write_off_table.setColumnHidden(13, True)
        self.write_off_table.horizontalHeader().setStretchLastSection(True)

    # 新增进货录入信息
    def do_write_off(self):
        sale_id = table_utils.get_table_current_index_info(self.write_off_table, 0)
        if not sale_id:
            QMessageBox.information(self.writeOffButton, "提示", '请选择需要销负的记录！')
            return

        brand_name = table_utils.get_table_current_index_info(self.write_off_table, 2)
        brand_id = table_utils.get_table_current_index_info(self.write_off_table, 7)
        model_name = table_utils.get_table_current_index_info(self.write_off_table, 3)
        model_id = table_utils.get_table_current_index_info(self.write_off_table, 8)
        sale_number = table_utils.get_table_current_index_info(self.write_off_table, 4)
        balance = int(table_utils.get_table_current_index_info(self.write_off_table, 5))
        unit = table_utils.get_table_current_index_info(self.write_off_table, 6)
        stock_id = table_utils.get_table_current_index_info(self.write_off_table, 9)
        first_srv_name = table_utils.get_table_current_index_info(self.write_off_table, 10)
        first_srv_id = table_utils.get_table_current_index_info(self.write_off_table, 11)
        second_srv_name = table_utils.get_table_current_index_info(self.write_off_table, 12)
        second_srv_id = table_utils.get_table_current_index_info(self.write_off_table, 13)

        stock = Stock()
        stock.id(stock_id)
        stock.brand_id(brand_id).brand_name(brand_name)
        stock.model_id(model_id).model_name(model_name)
        stock.unit(unit)
        stock.balance(balance)
        stock.first_service_name(first_srv_name).first_service_id(first_srv_id)
        stock.second_service_name(second_srv_name).second_service_id(second_srv_id)

        dialog = WriteOffDialog(stock, sale_number, sale_id)
        dialog.exec()

        self._init_write_off_table()
