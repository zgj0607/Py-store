class RegisterInfo(object):
    __store_id = ''
    __store_ip = ''
    __register_code = ''

    def store_id(self, store_id=''):
        if store_id:
            self.__store_id = store_id
            return self

        return self.__store_id

    def store_ip(self, store_ip=''):
        if store_ip:
            self.__store_ip = store_ip
            return self

        return self.__store_ip

    def register_code(self, reg_code=''):
        if reg_code:
            self.__register_code = reg_code
            return self

        return self.__register_code
