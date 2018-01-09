class Device(object):
    __id = 0
    __name = ''
    __ip = ''
    __state = 0
    __create_time = ''

    def id(self, device_id=0):
        if device_id:
            self.__id = device_id
            return self

        return self.__id

    def name(self, name=''):
        if name:
            self.__name = name
            return self

        return self.__name

    def ip(self, ip=''):
        if ip:
            self.__ip = ip
            return self

        return self.__ip

    def state(self, state=None):
        if state:
            self.__state = state
            return self

        return self.__state

    def create_time(self, create_time=''):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time

    @staticmethod
    def enable():
        return 1

    @staticmethod
    def disable():
        return 0
