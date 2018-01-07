from PyQt5 import QtWidgets

from View.stock.ui.ui_stock_money import Ui_StockMoney
from View.utils import table_utils
from database.dao.stock import stock_handler


class StockMoney(QtWidgets.QWidget, Ui_StockMoney):
    def __init__(self):
        super(StockMoney, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库存金额')
        self.table_title = ('一级分类', '二级分类', '库存数量', '库存金额')

        self._init_table()

    def _init_table(self):
        record = stock_handler.get_stock_money()
        table_utils.set_table_content_with_merge(self.tableView, record, self.table_title, 0)
