from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Common import time_utils, Common
from View.supplier.ui.ui_supplier_payment_dialog import Ui_SupplierArrearPayOffDialog
from View.utils import db_transaction_util
from database.dao.buy import payment_handler, buy_handler
from domain.buy import BuyInfo
from domain.payment import Payment


class PayOffArrearsDialog(QtWidgets.QDialog, Ui_SupplierArrearPayOffDialog):
    def __init__(self, buy: BuyInfo):
        super(PayOffArrearsDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('请填写支付金额')

        self._init_input_info(buy)
        self._init_signal_and_slot()

        self.buy_id = buy.buy_id()

    def _init_input_info(self, buy):
        self.pay_to.setText(buy.note())
        self.unpaid.setText('0.0')
        self.need_pay.setText(str(buy.unpaid()))
        self.paid.setText(str(buy.paid()))
        self.pay.setText(str(buy.unpaid()))

        payment_methods = Payment.get_payment_method()

        for key in list(payment_methods.keys()):
            self.payment_method.addItem(payment_methods[key], key)
        self.pay.setFocus()

    def _init_signal_and_slot(self):
        self.payButton.clicked.connect(self.do_pay)
        self.pay.textEdited.connect(self._pay_changed)

    def _pay_changed(self):
        pay = Decimal(self.pay.text())
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
            self._add_payment_detail(new_paid, unpaid)
            # 更新进货付款信息
            self._update_buy_pay_info(new_paid, unpaid, note)

            db_transaction_util.commit()

            QMessageBox.information(self.payButton, '提示', '付款成功！')
            self.close()

        except Exception as e:
            print(e)
            db_transaction_util.rollback()
            QMessageBox.information(self.payButton, '提示', '付款失败！')

    def _add_payment_detail(self, paid: float, unpaid: float, ):
        payment = Payment()

        payment.buy_id(self.buy_id)

        payment_method = int(self.payment_method.currentData())
        payment.payment_method(payment_method)

        payment.paid(paid)
        payment.unpaid(unpaid)

        payment.create_op(Common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())
        payment.refund_type(Payment.payoff())

        payment_handler.add_payment_detail(payment)

    def _update_buy_pay_info(self, paid: float, unpaid: float, notes: str):
        buy_handler.update_paid_info(self.buy_id, unpaid, paid, notes)
