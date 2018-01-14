class StockDetail(object):
    __id = 0
    __stock_id = 0
    __changed_id = 0
    __changed_number = 0
    __changed_money = 0.0
    __type = 0
    __update_time = ''
    __update_op = 0

    def detail_id(self, detail_id=0):
        if detail_id:
            self.__id = detail_id
            return self
        return self.__id

    def stock_id(self, stock_id=0):
        if stock_id:
            self.__stock_id = stock_id
            return self

        return self.__stock_id

    def changed_id(self, changed_id=0):
        if changed_id:
            self.__changed_id = changed_id
            return self

        return self.__changed_id

    def changed_money(self, changed_money=0.0):
        if changed_money:
            self.__changed_money = changed_money
            return self

        return self.__changed_money

    def changed_number(self, changed_number=0):
        if changed_number:
            self.__changed_number = changed_number
            return self

        return self.__changed_number

    def type(self, stock_type=0):
        if stock_type:
            self.__type = stock_type
            return self

        return self.__type

    def update_time(self, update_time=''):
        if update_time:
            self.__update_time = update_time
            return self

        return self.__update_time

    def update_op(self, update_op=0):
        if update_op:
            self.__update_op = update_op
            return self

        return self.__update_op

    @staticmethod
    def types():
        return {0: '进货库存', 1: '退货库存', 2: '核增库存', 3: '核减库存', 4: '正库存销售', 5: '负库存销售', 6: '已销负销售'}

    # 进货库存
    @staticmethod
    def by_bought():
        return 0

    # 退货库存
    @staticmethod
    def by_returned():
        return 1

    # 核增库存
    @staticmethod
    def by_increased():
        return 2

    # 核减库存
    @staticmethod
    def by_decreased():
        return 3

    # 正库存销售
    @staticmethod
    def by_sold():
        return 4

    # 负库存销售
    @staticmethod
    def by_negative():
        return 5

    # 已销负销售
    @staticmethod
    def by_write_off():
        return 6
