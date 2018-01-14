class Customer(object):
    __id = 0
    __username = ''
    __car_model = ''
    __phone = ''
    __car_id = ''
    __create_time = ''

    def id(self, customer_id=None):
        if customer_id:
            self.__id = customer_id
            return self

        return self.__id

    def username(self, username=None):
        if username:
            self.__username = username
            return self

        return self.__username

    def car_model(self, car_model=None):
        if car_model:
            self.__car_model = car_model
            return self

        return self.__car_model

    def phone(self, phone=None):
        if phone:
            self.__phone = phone
            return self

        return self.__phone

    def car_id(self, car_id=None):
        if car_id:
            self.__car_id = car_id
            return self

        return self.__car_id

    def create_time(self, create_time=None):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time
