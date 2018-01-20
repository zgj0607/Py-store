import logging
import traceback
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from common import time_utils, common
from database.dao.buy import payment_handler, buy_handler
from database.dao.dictionary import dictionary_handler
from database.dao.supplier import supplier_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from view.supplier.ui.ui_supplier_payment_dialog import Ui_SupplierArrearPayOffDialog
from view.utils import db_transaction_util

logger = logging.getLogger(__name__)


class PayOffArrearsDialog(QtWidgets.QDialog, Ui_SupplierArrearPayOffDialog):
    def __init__(self, buy: BuyInfo):
        super(PayOffArrearsDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('请填写支付金额')

        self._init_input_info(buy)
        self._init_signal_and_slot()

        self.buy_id = buy.buy_id()
        self.supplier_id = buy.supplier_id()

    def _init_input_info(self, buy):
        self.pay_to.setText(buy.note())
        self.unpaid.setText('0.0')
        self.need_pay.setText(str(buy.unpaid()))
        self.paid.setText(str(buy.paid()))
        self.pay.setText(str(buy.unpaid()))

        Payment.get_all_payment(self.payment_method)
        self.payment_method.addItem('点击添加')
        self.pay.setFocus()

    def _init_signal_and_slot(self):
        self.payButton.clicked.connect(self.do_pay)
        self.pay.textEdited.connect(self._pay_changed)
        self.payment_method.activated['int'].connect(self._need_add_payment)

    def _pay_changed(self):
        pay = self.pay.text()
        if not pay:
            pay = '0.0'
        pay = Decimal(pay)
        need_pay = Decimal(self.need_pay.text())

        changed = need_pay - pay

        self.unpaid.setText(str(changed))

    def do_pay(self):

        unpaid = Decimal(self.unpaid.text())
        if unpaid < 0:
            QMessageBox.information(self.payButton, '提示', '付款额度超过未付款额度，请重新填写！')
            return
        pay = Decimal(self.pay.text())
        note = self.notes.text()
        paid = Decimal(self.paid.text())
        new_paid = paid + pay
        try:
            db_transaction_util.begin()

            # 新增付款明细
            self._add_payment_detail(paid, unpaid)
            # 更新进货付款信息
            self._update_buy_pay_info(new_paid, unpaid, note)
            # 更新供应商未付信息
            self._update_supplier_unpaid(pay)

            db_transaction_util.commit()

            QMessageBox.information(self.payButton, '提示', '付款成功！')
            self.close()

        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            db_transaction_util.rollback()
            QMessageBox.information(self.payButton, '提示', '付款失败！')

    def _add_payment_detail(self, paid: float, unpaid: float, ):
        payment = Payment()

        payment.buy_id(self.buy_id)

        payment_method = int(self.payment_method.currentData())
        payment.payment_method(payment_method)

        payment.paid(paid)
        payment.unpaid(unpaid)

        payment.create_op(common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())
        payment.refund_type(Payment.payoff())

        payment_handler.add_payment_detail(payment)

    def _update_buy_pay_info(self, paid: float, unpaid: float, notes: str):
        buy_handler.update_paid_info(self.buy_id, unpaid, paid, notes)

    def _update_supplier_unpaid(self, pay):
        update_pay = 0 - pay

        supplier_handler.update_supplier_unpaid(self.supplier_id, update_pay)

    def _need_add_payment(self, index):
        if index == self.payment_method.count() - 1:
            self._add_new_payment_method()

    def _add_new_payment_method(self):
        payment_method, ok = QInputDialog.getText(self.payButton, '新增付款方式', '请输入付款方式')
        if ok and not payment_method:
            QMessageBox.warning(self.payButton, '警告', '付款方式不能为空，请重新添加！')
            return
        exist_num = dictionary_handler.get_count_by_group_and_value(Payment.group_name(), payment_method)
        if exist_num:
            QMessageBox.warning(self.payButton, '警告', '付款方式已经存在，请重新添加！')
            return
        key_id = dictionary_handler.get_max_key_id_by_group_name(Payment.group_name()) + 1
        dictionary_handler.add_dictionary(key_id, payment_method, Payment.group_name())
        QMessageBox.warning(self.payButton, '提示', '付款方式添加成功！')
        self.payment_method.insertItem(0, payment_method, key_id)
        self.payment_method.setCurrentIndex(0)
