from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from view.stock.ui.ui_stock_unsalable_warning import Ui_inventoryunsalablewarningForm
from view.utils import excel_utils
from view.utils.table_utils import set_table_content
from database.dao.stock import stock_unsalable_warning_handler


class StockUnsalableWarning(QtWidgets.QWidget, Ui_inventoryunsalablewarningForm):
    def __init__(self):
        super(StockUnsalableWarning, self).__init__()
        self.setupUi(self)
        self.exportButton.clicked.connect(self.export)
        self.setWindowTitle('滞销库存预警')
        self.inventorywaringtableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_title = (
            '商品品牌', '商品型号', '库存数量', '最长库龄')
        self._init_inventory_table()

    def _init_inventory_table(self):
        unsalable_warning_table = self.inventorywaringtableView

        # 填充数据
        set_table_content(unsalable_warning_table, stock_unsalable_warning_handler.get_unsalable_warning(),
                          self.table_title)

    def export(self):
        model = self.inventorywaringtableView.model()
        if not model.rowCount() or not model.columnCount():
            QMessageBox.warning(self.exportButton, "提示", '无滞销库存预警明细，无法导出！')
            return
        suggest_file_name = '''滞销库存预警-{}.xls'''.format(datetime.now().strftime('%Y%m%d'))
        file_path, ok = QFileDialog.getSaveFileName(self.exportButton, '请选择保存位置', suggest_file_name,
                                                    "All Files (*);;Excel (*.xls)")

        if ok and file_path:
            excel_utils.export_to_file_from_table_view(file_path, self.table_title, '滞销库存预警', model)
            QMessageBox.information(self.exportButton, "提示", '导出成功，文件保存在: ' + file_path)
