class ReturnVisit(object):
    __id = 0
    __create_time = ''
    __next_return_visit_time = ''
    __customer_phone = ''
    __car_id = ''
    __customer_name = ''
    __state = ''

    def id(self, record_id=0):
        if record_id:
            self.__id = record_id
            return self

        return self.__id

    def create_time(self, create_time=None):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time

    def next_time(self, next_time=None):
        if next_time:
            self.__next_return_visit_time = next_time
            return self

        return self.__next_return_visit_time

    def customer_phone(self, phone=''):
        if phone:
            self.__customer_phone = phone
            return self

        return self.__customer_phone

    def car_id(self, car_id=''):
        if car_id:
            self.__car_id = car_id
            return self

        return self.__car_id

    def customer_name(self, name=''):
        if name:
            self.__customer_name = name
            return self

        return self.__customer_name

    def state(self, state=0):
        if state:
            self.__state = state
            return self

        return self.__state

    @staticmethod
    def visited():
        return 1

    @staticmethod
    def unvisited():
        return 0
