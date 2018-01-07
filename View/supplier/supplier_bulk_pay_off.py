from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Common import Common, time_utils
from View.supplier.ui.ui_supplier_bulk_pay_off import Ui_BulkPayOff
from View.utils import db_transaction_util
from database.dao.buy import payment_handler, buy_handler
from domain.payment import Payment


class SupplierBulkPayOff(QtWidgets.QDialog, Ui_BulkPayOff):
    def __init__(self, buys: list, total: str, supplier_name: str):
        super(SupplierBulkPayOff, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('批量付款')
        self.buys = buys

        self._init_input_info(total, supplier_name)

        self.payButton.clicked.connect(self.do_bulk_pay)

    def _init_input_info(self, total, supplier_name):
        self.pay_to.setText(supplier_name)
        self.pay.setText(str(total))

        payments = Payment.get_payment_method()
        for key in list(payments.keys()):
            self.payment_method.addItem(payments[key], key)

    def do_bulk_pay(self):
        notes = self.note.text()

        try:
            db_transaction_util.begin()
            for buy_info in self.buys:
                # 新增付款明细
                self._add_payment_detail(buy_info[1], buy_info[2], buy_info[0])
                # 更新进货付款信息
                self._update_buy_pay_info(buy_info[1], buy_info[2], notes, buy_info[0])

            db_transaction_util.commit()

            QMessageBox.information(self.payButton, '提示', '付款成功！')
            self.close()

        except Exception as e:
            print(e)
            db_transaction_util.rollback()
            QMessageBox.information(self.payButton, '提示', '付款失败！')

    def _add_payment_detail(self, paid: float, unpaid: float, buy_id: int):
        payment = Payment()

        payment.buy_id(buy_id)

        payment_method = int(self.payment_method.currentData())
        payment.payment_method(payment_method)

        payment.paid(paid)
        payment.unpaid(unpaid)

        payment.create_op(Common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())
        payment.refund_type(Payment.payoff())

        payment_handler.add_payment_detail(payment)

    def _update_buy_pay_info(self, paid: float, unpaid: float, notes: str, buy_id: int):
        buy_handler.update_paid_info(buy_id, unpaid, paid, notes)
