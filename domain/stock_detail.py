class StockDetail(object):
    __id = 0
    __stock_id = 0
    __buy_id = 0
    __buy_price = 0.0
    __sale_id = 0
    __sale_price = 0.0
    __state = 0
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

    def buy_id(self, buy_id=0):
        if buy_id:
            self.__buy_id = buy_id
            return self

        return self.__buy_id

    def buy_price(self, buy_price=0.0):
        if buy_price:
            self.__buy_price = buy_price
            return self

        return self.__buy_price

    def sale_id(self, sale_id=0):
        if sale_id:
            self.__sale_id = sale_id
            return self

        return self.__sale_id

    def sale_price(self, sale_price=0.0):
        if sale_price:
            self.__sale_price = sale_price
            return self

        return self.__sale_price

    def state(self, state=0):
        if state:
            self.__state = state
            return self

        return self.__state

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
    def states():
        return {0: '在库', 1: '已售', 2: '已退货', 3: '已核减', 4: '待销负'}

    # 在库
    @staticmethod
    def in_store():
        return 0

    # 已售
    @staticmethod
    def sold():
        return 1

    # 已退货
    @staticmethod
    def returned():
        return 2

    # 已核减
    @staticmethod
    def increased():
        return 3

    # 待销负
    @staticmethod
    def under_write_off():
        return 4

    @staticmethod
    def types():
        return {0: '进货库存', 1: '退货库存', 2: '核增库存', 3: '销负库存'}

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

    # 销负库存
    @staticmethod
    def by_write_off():
        return 3

    @staticmethod
    def to_stock_detail(details: ()):
        detail = StockDetail()

        detail.detail_id(details[0])
        detail.stock_id(details[1])
        detail.buy_id(details[2])
        detail.buy_price(details[3])
        detail.sale_id(details[4])
        detail.sale_price(details[5])
        detail.state(details[6])
        detail.type(details[7])
        detail.update_time(details[8])
        detail.update_op(details[9])

        return detail
