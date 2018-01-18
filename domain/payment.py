from PyQt5.QtWidgets import QComboBox

from database.dao.dictionary import dictionary_handler


class Payment(object):
    __id = 0
    __buy_id = 0
    __payment_method = 1
    __paid = 0.0
    __unpaid = 0.0
    __create_time = ''
    __create_op = 0
    __refund_type = 1
    __supplier_id = 0
    __note = ''

    def id(self, pay_id=0):
        if pay_id:
            self.__id = pay_id
            return self

        return self.__id

    def buy_id(self, buy_id=0):
        if buy_id:
            self.__buy_id = buy_id
            return self

        return self.__buy_id

    def payment_method(self, payment_method=0):
        if payment_method:
            self.__payment_method = payment_method
            return self

        return self.__payment_method

    def paid(self, paid=0.0):
        if paid:
            self.__paid = paid
            return self

        return self.__paid

    def unpaid(self, unpaid=0.0):
        if unpaid:
            self.__unpaid = unpaid
            return self

        return self.__unpaid

    def create_time(self, create_time=''):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time

    def create_op(self, create_op):
        if create_op:
            self.__create_op = create_op
            return self

        return self.__create_op

    def refund_type(self, refund_type=0):
        if refund_type:
            self.__refund_type = refund_type
            return self

        return self.__refund_type

    def supplier_id(self, supplier_id=None):
        if supplier_id:
            self.__supplier_id = supplier_id
            return self

        return self.__supplier_id

    def note(self, note=None):
        if note:
            self.__note = note
            return self

        return self.__note

    @staticmethod
    def get_payment_method():
        return {1: '现金/转账', 2: '信用卡', 3: '微信', 4: '支付宝', 5: '支票'}

    @staticmethod
    def get_refund_type():
        return {1: '付款', 2: '退款'}

    @staticmethod
    def returned(refund_type=None):
        if refund_type:
            return '退款'
        return 2

    @staticmethod
    def payoff(refund_type=None):
        if refund_type:
            return '付款'
        return 1

    @staticmethod
    def group_name():
        return 'payment'

    @staticmethod
    def get_all_payment(combo_box: QComboBox):
        payments = dictionary_handler.get_key_and_value_by_group_name(Payment.group_name())
        for k_v in payments:
            combo_box.addItem(k_v['value_desc'], k_v['key_id'])