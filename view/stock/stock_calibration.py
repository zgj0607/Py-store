import logging
import traceback
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controller.view_service import buy_service
from database.dao.buy import buy_handler
from database.dao.stock import stock_handler, stock_detail_handler
from domain.buy import BuyInfo
from domain.stock_detail import StockDetail
from view.stock.stock_calibration_dialog import StockCalibrationDialog
from view.stock.ui.ui_stock_calibration import Ui_stock_calibration
from view.utils import table_utils, db_transaction_util

logger = logging.getLogger(__name__)


class StockCalibration(QtWidgets.QWidget, Ui_stock_calibration):
    def __init__(self):
        super(StockCalibration, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('校准信息')
        self.table_title = ('id', '库存ID', '日期', '品牌', '商品型号', '调整类型',
                            '库存数量', '调整数量', '库存金额', '调整金额', '经手人', '备注', '审核状态')
        self._init_ui()
        self._init_signal_and_slot()

    def _init_ui(self):
        self._init_table()
        self._init_combo()

    def _init_table(self):
        record = stock_handler.get_all_calibration()
        table_utils.set_table_content(self.tableView, record, self.table_title)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(1, True)

        self.tableView.resizeColumnsToContents()

    def _init_combo(self):
        self.second_srv_combo.addItem("未审核", "1")
        self.second_srv_combo.addItem("已审核", "0")
        self.second_srv_combo.addItem("已作废", "2")

    def _init_signal_and_slot(self):
        self.searchButton.clicked.connect(self.search)
        self.calibrationButton.clicked.connect(self.do_calibration)
        self.reviewButton.clicked.connect(self.do_review)

    def search(self):
        state = int(self.second_srv_combo.currentData())
        record = stock_handler.get_calibration(state)
        table_utils.set_table_content(self.tableView, record, self.table_title)

        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(1, True)

        self.tableView.resizeColumnsToContents()

    def do_calibration(self):
        dialog = StockCalibrationDialog()
        dialog.exec()
        self._init_table()

    def do_review(self):
        review_id = table_utils.get_table_current_index_info(self.tableView, 0)
        if not review_id:
            QMessageBox.information(self.reviewButton, '提示', '请选择待审核的库存校准数据！')
            return
        stock_id = int(table_utils.get_table_current_index_info(self.tableView, 1))
        stock_detail = stock_detail_handler.get_calibration_detail_by_buy_id(review_id)
        changed_type = stock_detail['type']

        answer = QMessageBox.information(self.reviewButton, '校准审核', '是否审核通过该项库存校准？',
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
        try:
            db_transaction_util.begin()
            if answer == QMessageBox.Yes:

                changed_cost = Decimal(table_utils.get_table_current_index_info(self.tableView, 9))
                changed_number = int(table_utils.get_table_current_index_info(self.tableView, 7))

                if changed_type == StockDetail.by_decreased():
                    buy_service.decrease_buy_left(stock_id, abs(changed_number))
                else:
                    buy_service.increase_buy_left(stock_id, abs(changed_number))

                stock_handler.update_stock_balance(stock_id, changed_number, changed_cost)
                buy_handler.update_buy_state(review_id, BuyInfo.normal())

            elif answer == QMessageBox.No:
                buy_handler.update_buy_state(review_id, BuyInfo.rejected())
            db_transaction_util.commit()
            self._init_table()
        except Exception as e:
            db_transaction_util.rollback()
            logger.error(e)
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
