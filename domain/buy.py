class BuyInfo(object):
    __buy_id = 0
    __stock_id = 0
    __supplier_id = 0
    __unit_price = 0.00
    __number = 0
    __payment_method = 1
    __paid = 0.0
    __unpaid = 0.0
    __total = 0.0
    __buy_date = ''
    __create_time = ''
    __create_op = 0
    __rela_buy_id = 0
    __buy_type = 1
    __note = ''
    __left = 0
    __state = 0

    def buy_id(self, buy_id=0):
        if buy_id:
            self.__buy_id = buy_id
            return self

        return self.__buy_id

    def stock_id(self, stock_id=0):
        if stock_id:
            self.__stock_id = stock_id
            return self

        return self.__stock_id

    def supplier_id(self, supplier_id=0):
        if supplier_id:
            self.__supplier_id = supplier_id
            return self

        return self.__supplier_id

    def unit_price(self, unit_price=0.0):
        if unit_price:
            self.__unit_price = unit_price
            return self

        return self.__unit_price

    def number(self, number=0):
        if number:
            self.__number = number
            return self

        return self.__number

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

    def total(self, total=0.0):
        if total:
            self.__total = total
            return self

        return self.__total

    def buy_date(self, buy_date=''):
        if buy_date:
            self.__buy_date = buy_date
            return self

        return self.__buy_date

    def create_time(self, create_time=''):
        if create_time:
            self.__create_time = create_time
            return self
        return self.__create_time

    def create_op(self, create_op=0):
        if create_op:
            self.__create_op = create_op
            return self

        return self.__create_op

    def rela_buy_id(self, rela_buy_id=0):
        if rela_buy_id:
            self.__rela_buy_id = rela_buy_id
            return self

        return self.__rela_buy_id

    def buy_type(self, buy_type=0):
        if buy_type:
            self.__buy_type = buy_type
            return self

        return self.__buy_type

    def note(self, note=''):
        if note:
            self.__note = note
            return self

        return self.__note

    def left(self, left=0):
        if left:
            self.__left = left
            return self

        return self.__left

    def state(self, state=0):
        if state:
            self.__state = state
            return self

        return self.__state

    @staticmethod
    def buy_types():
        return {1: '进货', 2: '退货'}

    @staticmethod
    def bought(buy_type=None):
        if buy_type:
            return '进货'
        return 1

    @staticmethod
    def returned(buy_type=None):
        if buy_type:
            return '退货'
        return 2

    @staticmethod
    def calibrated(buy_type=None):
        if buy_type:
            return '库存校准'
        return 8

    @staticmethod
    def normal(state=None):
        if state == 0:
            return '已审核'
        return 0

    @staticmethod
    def under_reviewed(state=None):
        if state == 1:
            return '待审核'
        return 1

    @staticmethod
    def rejected(state=None):
        if state == 2:
            return '已拒绝'
        return 2
