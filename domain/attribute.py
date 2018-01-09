class Attribute(object):
    __id = 0
    __name = ''
    __is_required = 0
    __create_time = ''
    __create_op = 0
    __delete_state = 0

    def attr_id(self, attr_id=0):
        if attr_id:
            self.__id = attr_id
            return self

        return self.__id

    def name(self, name=''):
        if name:
            self.__name = name
            return self

        return self.__name

    def is_required(self, is_required=0):
        if is_required:
            self.__is_required = is_required
            return self

        return self.__is_required

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

    def delete_state(self, delete_state=0):
        if delete_state:
            self.__delete_state = delete_state
            return self

        return self.__delete_state

    @staticmethod
    def option():
        return 0

    @staticmethod
    def required():
        return 1
