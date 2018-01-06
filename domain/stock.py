class Stock(object):
    __id = 0
    __unit = ''
    __first_service_id = 0
    __first_service_name = ''
    __second_service_id = 0
    __second_service_name = ''
    __brand_id = 0
    __brand_name = ''
    __model_id = 0
    __model_name = ''
    __name = ''
    __balance = 0
    __total_cost = 0.0
    __create_time = ''
    __create_op = 0

    def id(self, stock_id=0):
        if stock_id:
            self.__id = stock_id
            return self

        return self.__id

    def name(self, name=''):
        if name:
            self.__name = name
            return self

        return self.__name

    def unit(self, unit=''):
        if unit:
            self.__unit = unit

        return self.__unit

    def first_service_id(self, first_service_id=0):
        if first_service_id:
            self.__first_service_id = first_service_id
            return self

        return self.__first_service_id

    def first_service_name(self, first_service_name=''):
        if first_service_name:
            self.__first_service_name = first_service_name
            return self

        return self.__first_service_name

    def second_service_id(self, second_service_id=0):
        if second_service_id:
            self.__second_service_id = second_service_id
            return self

        return self.__second_service_id

    def second_service_name(self, second_service_name=''):
        if second_service_name:
            self.__second_service_name = second_service_name
            return self

        return self.__second_service_name

    def brand_id(self, brand_id=0):
        if brand_id:
            self.__brand_id = brand_id
            return self

        return self.__brand_id

    def brand_name(self, brand_name=''):
        if brand_name:
            self.__brand_name = brand_name
            return self

        return self.__brand_name

    def model_id(self, model_id=0):
        if model_id:
            self.__model_id = model_id
            return self

        return self.__model_id

    def model_name(self, model_name=''):
        if model_name:
            self.__model_name = model_name
            return self

        return self.__model_name

    def balance(self, balance=0):
        if balance:
            self.__balance = balance
            return self

        return self.__balance

    def total_cost(self, total_cost=0.0):
        if total_cost:
            self.__total_cost = total_cost

        return self.__total_cost

    def create_time(self, create_time):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time

    def create_op(self, create_op=0):
        if create_op:
            self.__create_op = create_op
            return self

        return self.__create_op
