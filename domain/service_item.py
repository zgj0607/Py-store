class ServiceItem(object):
    __id = 0
    __service_id = 0
    __attribute_id = 0
    __attribute_name = ''
    __create_time = ''
    __create_op = 0

    def item_id(self, item_id=''):
        if item_id:
            self.__id = item_id
            return self

        return self.__id

    def service_id(self, service_id=None):
        if service_id:
            self.__service_id = service_id
            return self

        return self.__service_id

    def attribute_id(self, attribute_id=None):
        if attribute_id:
            self.__attribute_id = attribute_id
            return self

        return self.__attribute_id

    def attribute_name(self, attribute_name=None):
        if attribute_name:
            self.__attribute_name = attribute_name
            return self

        return self.__attribute_name

    def create_time(self, create_time=''):
        if create_time:
            self.__create_time = create_time
            return self

        return self.__create_time

    def create_op(self, create_op=None):
        if create_op:
            self.__create_op = create_op
            return self

        return self.__create_op
