# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from View.stock.ui.ui_stock_unsalable_warning import Ui_inventoryunsalablewarningForm
from View.utils.table_utils import set_table_content
from database.dao.stock import inventory_unsalable_warning_handler
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from datetime import datetime
from View.utils import excel_utils


class inventory_unsalable_warningForm(QtWidgets.QWidget, Ui_inventoryunsalablewarningForm):
    def __init__(self):
        super(inventory_unsalable_warningForm, self).__init__()
        self.setupUi(self)
        self.exportButton.clicked.connect(self.export)
        self.setWindowTitle('滞销库存预警')
        self.inventorywaringtableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_title = (
            '商品品牌', '商品型号', '库存数量', '最长库龄')
        self._init_inventory_table()
    def _retranslateUi(self):
        print('123')
    def _init_inventory_table(self):
        inventorywaringtableView = self.inventorywaringtableView

        # 填充数据
        set_table_content(inventorywaringtableView, inventory_unsalable_warning_handler.get_negative_on_hand(), self.table_title)

    def export(self):
        model = self.inventorywaringtableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.exportButton, "提示", '无滞销库存预警明细，无法导出！')
            return
        suggest_file_name = '''滞销库存预警-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.exportButton, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xls)")

        if ok and file_path:
            excel_utils.export_to_file(file_path, self.table_title, '滞销库存预警', model)
            QMessageBox.information(self.exportButton, "提示", '导出成功，文件保存在: ' + file_path)
        # stockForm.




