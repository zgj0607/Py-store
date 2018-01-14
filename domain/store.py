class Store(object):
    __store_id = ''
    __store_name = ''
    __store_phone = ''
    __store_address = ''

    def id(self, store_id=''):
        if store_id:
            self.__store_id = store_id
            return self

        return self.__store_id

    def name(self, store_name=''):
        if store_name:
            self.__store_name = store_name
            return self

        return self.__store_name

    def phone(self, store_phone=''):
        if store_phone:
            self.__store_phone = store_phone
            return self

        return self.__store_phone

    def address(self, store_address=''):
        if store_address:
            self.__store_address = store_address
            return self

        return self.__store_address
