import logging
import traceback
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox

from common import time_utils
from controller.view_service import buy_service, stock_service
from database.dao.buy import buy_handler
from database.dao.stock import brand_handler, model_handler
from database.dao.stock import stock_handler
from database.dao.users import user_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock_detail import StockDetail
from view.stock.ui.ui_stock_calibration_dialog import Ui_stock_calibrationDialog
from view.utils import db_transaction_util

logger = logging.getLogger(__name__)


class StockCalibrationDialog(QtWidgets.QDialog, Ui_stock_calibrationDialog):
    def __init__(self):
        super(StockCalibrationDialog, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('请填写校准信息')
        self._init_ui_info()

        self._init_signal_and_slot()

    def _init_ui_info(self):
        self.calibration_date.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self._init_brand()
        self._init_staff_combo()

    def _init_signal_and_slot(self):
        self.addButton.clicked.connect(self._submit)
        self.brand_combo.currentIndexChanged.connect(self._brand_index_changed)
        self.model_combo.currentIndexChanged.connect(self._model_index_changed)

    def _submit(self):
        money_changed = self.money_changed.text()
        balance_changed = self.balance_changed.text()
        if not money_changed or not balance_changed:
            QMessageBox.information(self.addButton, '提示', '调整金额和调整数量不能为空！')
            self.balance_changed.setFocus()
            return
        money_changed = Decimal(money_changed)
        balance_changed = int(balance_changed)

        if money_changed == self.original_cost and balance_changed == self.original_balance:
            QMessageBox.information(self.addButton, '提示', '金额和数量未做调整，请重新填写！')
            self.balance_changed.setFocus()
            return

        changed_number = balance_changed - self.original_balance
        changed_cost = money_changed - self.original_cost
        buy_date = self.calibration_date.date().toString('yyyy-MM-dd')
        payment_method = list(Payment.get_payment_method().keys())[0]
        note = self.notes.text()
        create_op = int(self.staffComb.currentData())
        try:
            db_transaction_util.begin()
            logger.info('新增库存校准数据')
            buy_id = buy_service.add_buy_info(self.stock_id, 9999, 0.0, changed_number, buy_date, 0.0, 0.0,
                                              changed_cost, payment_method, note, 0, create_op, BuyInfo.calibrated(),
                                              BuyInfo.under_reviewed())
            if changed_number >= 0:
                change_type = StockDetail.by_increased()
            else:
                change_type = StockDetail.by_decreased()

            stock_service.add_stock_detail(self.stock_id, buy_id, abs(changed_cost), abs(changed_number), change_type)
            db_transaction_util.commit()
            logger.info('库存校准数据新增完成')
            QMessageBox.information(self.addButton, '提示', '库存校准成功，请等待数据审核！')
            self.close()
        except Exception as e:
            db_transaction_util.rollback()
            logger.error(e)
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))

    def _update_buy_pay_info(self, paid: float, unpaid: float, notes: str):
        buy_handler.update_paid_info(self.buy_id, unpaid, paid, notes)

    def _init_staff_combo(self):
        users = user_handler.get_all_sys_user()
        for user in users:
            self.staffComb.addItem(user['username'], user['id'])

    def _init_brand(self):
        brands = brand_handler.get_all_brand()
        for brand in brands:
            self.brand_combo.addItem(brand[1], brand[0])
        if brands:
            brand_id = brands[0][0]
            self._refresh_model(brand_id)

    def _brand_index_changed(self):
        self._refresh_model()

    def _refresh_model(self, brand_id=0):
        if not brand_id:
            brand_id = self.brand_combo.currentData()
        if brand_id:
            brand_id = int(brand_id)
            models = model_handler.get_model_by_brand(brand_id)
            self.model_combo.clear()
            for model in models:
                self.model_combo.addItem(model[1], model[0])

        self._model_index_changed()

    def _model_index_changed(self):
        model_id = self.model_combo.currentData()
        if not model_id:
            balance = 0
            cost = 0.0
            self.stock_id = 0
        else:
            model_id = int(model_id)
            stock_info = stock_handler.get_stock_by_model(model_id)
            balance = stock_info['balance']
            cost = stock_info['total_cost']
            self.stock_id = stock_info['id']
        self.original_balance = balance
        self.original_cost = cost
        self.balance_in_db.setText(str(balance))
        self.money_in_db.setText(str(cost))
