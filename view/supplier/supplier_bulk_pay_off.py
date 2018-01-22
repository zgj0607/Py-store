import logging
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from common import common, time_utils
from database.dao.buy import payment_handler, buy_handler
from database.dao.dictionary import dictionary_handler
from database.dao.supplier import supplier_handler
from domain.payment import Payment
from view.supplier.ui.ui_supplier_bulk_pay_off import Ui_BulkPayOff
from view.utils import db_transaction_util, view_utils

logger = logging.getLogger(__name__)


class SupplierBulkPayOff(QtWidgets.QDialog, Ui_BulkPayOff):
    def __init__(self, buys: list, total: str, supplier_name: str, supplier_id: int):
        super(SupplierBulkPayOff, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('批量付款')
        self.buys = buys
        self.supplier_id = supplier_id
        self.total = total
        self._init_input_info(total, supplier_name)

        self.payButton.clicked.connect(self.do_bulk_pay)
        self.payment_method.activated['int'].connect(self._need_add_payment)

    def _init_input_info(self, total, supplier_name):
        self.pay_to.setText(supplier_name)
        self.pay.setText(str(total))

        view_utils.get_all_payment(self.payment_method)
        self.payment_method.addItem('点击添加')

    def do_bulk_pay(self):
        notes = self.note.text()

        try:
            db_transaction_util.begin()
            for buy_info in self.buys:
                # 新增付款明细
                self._add_payment_detail(buy_info[3], buy_info[2], buy_info[0])
                # 更新进货付款信息
                self._update_buy_pay_info(buy_info[1], buy_info[2], notes, buy_info[0])
            self._update_supplier_unpaid(self.total)

            db_transaction_util.commit()

            QMessageBox.information(self.payButton, '提示', '付款成功！')
            self.close()

        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            db_transaction_util.rollback()
            QMessageBox.information(self.payButton, '提示', '付款失败！')

    def _add_payment_detail(self, paid: float, unpaid: float, buy_id: int):
        payment = Payment()

        payment.buy_id(buy_id)

        payment_method = int(self.payment_method.currentData())
        payment.payment_method(payment_method)

        payment.paid(paid)
        payment.unpaid(unpaid)

        payment.create_op(common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())
        payment.refund_type(Payment.payoff())

        payment_handler.add_payment_detail(payment)

    @staticmethod
    def _update_buy_pay_info(paid: float, unpaid: float, notes: str, buy_id: int):
        buy_handler.update_paid_info(buy_id, unpaid, paid, notes)

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
