# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '1/5/2017'

                ┏┓     ┏┓
              ┏┛┻━━━┛┻┓
             ┃     ☃     ┃
             ┃ ┳┛  ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓     ┏━┛
               ┃     ┗━━━┓
              ┃  神兽保佑   ┣┓
             ┃　永无BUG！  ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
from tornado.concurrent import run_on_executor

from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts
from controller.Api.BaseHandler import BaseHandler
from database.dao.service import service_handler


class ApiService_Handler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ApiService_Handler, self).__init__(application, request, **kwargs)
        self.func = self.ApiService

    @run_on_executor
    def ApiService(self, keyWord, getData):
        try:
            if self.request.method == "GET":
                if keyWord == "one":
                    second_services = service_handler.get_all_first_level_service()
                    send_data = list()
                    for data in second_services:
                        send_data.append({
                            "oneMenuId": data[0],
                            "name": data[1]
                        })
                    return set_return_dicts(send_data)

                elif keyWord == "two":
                    first_service_id = getData.get("oneMenuId")
                    second_services = service_handler.get_second_service_by_father(first_service_id)
                    send_data = list()
                    for data in second_services:
                        second_service_id = data[2]
                        second_service_name = data[3]
                        attribute_dict = {}
                        for attr in service_handler.get_attribute_by_service(second_service_id):
                            attribute_dict[attr[1]] = '1'

                        send_data.append({
                            "twoMenuId": second_service_id,
                            "name": second_service_name,
                            "attribute": attribute_dict,
                        })
                    return set_return_dicts(send_data)

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])
