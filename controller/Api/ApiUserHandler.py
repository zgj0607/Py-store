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
import json
from collections import OrderedDict, defaultdict

from tornado.concurrent import run_on_executor

from common import time_utils
from common.common import SocketServer
from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts
from controller.Api.BaseHandler import BaseHandler
from database.dao.customer import customer_handler
from database.dao.customer.customer_handler import get_like_customer_by_key
from database.dao.sale import sale_handler
from domain.customer import Customer


class ApiUserHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ApiUserHandler, self).__init__(application, request, **kwargs)
        self.func = self.user

    @run_on_executor
    def user(self, keyword, get_data):
        try:
            if self.request.method == 'POST':
                if keyword == "add":
                    try:
                        username = get_data.pop("username")
                        phone = get_data.pop("carPhone")
                        car_model = get_data.pop("carModel")
                        car_id = get_data.pop("carId")
                    except Exception as e:
                        print(e)
                        raise ApiException(ErrorCode.ParameterMiss)

                    customer = Customer()
                    customer.username(username)
                    customer.car_model(car_model)
                    customer.phone(phone)
                    customer.car_id(car_id)
                    customer.create_time(time_utils.get_now())

                    temp_user = customer_handler.get_customer_by_key("carId", car_id)
                    if temp_user:
                        try:
                            customer_handler.update_customer_by_car_id(customer)
                        except Exception as update_exception:
                            print(update_exception)
                            raise ApiException(ErrorCode.ParameterError)
                        customer_id = temp_user[0][0]
                    else:
                        try:
                            customer_id = customer_handler.add_customer(customer)
                        except Exception as insert_exception:
                            print(insert_exception)
                            raise ApiException(ErrorCode.UserMore)

                    return set_return_dicts({"userId": customer_id})

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":

                if not self.storeId:
                    raise ApiException(ErrorCode.PCError)

                if keyword == "find":
                    key = get_data.get("key", "")
                    if key not in ["carPhone", "carId"]:
                        raise ApiException(ErrorCode.ParameterError)

                    value = get_data.get("value", "")

                    if self.connect:
                        temp = SocketServer("user {} {} {}".format(self.storeId, key, value))
                        if not temp:
                            temp = self.find_customer(key, value)

                    else:
                        temp = self.find_customer(key, value)
                    result = []
                    key_temp = []
                    if temp == 'restart':
                        raise ApiException(ErrorCode.ReStartPC)
                    else:
                        for data in temp:
                            key = data.get("phone") + data.get("carId") + data.get("carModel") + data.get("userName")
                            if key in key_temp:
                                pass
                            else:
                                result.append(data)
                                key_temp.append(key)

                    return set_return_dicts(result)

                elif keyword == 'order':
                    car_id = get_data.get("carId", "")
                    phone = get_data.get("carPhone", "")

                    if not car_id:
                        raise ApiException(ErrorCode.ParameterMiss)

                    if self.connect:
                        all_order_money = 0.0
                        result = SocketServer("userorder {} {} {}".format(self.storeId, car_id, phone))
                        if result:
                            order_number = len(result)
                            for data in result:
                                all_order_money += data.get("totalPrice")
                        else:
                            result, order_number, all_order_money = self.get_order(car_id)

                    else:
                        result, order_number, all_order_money = self.get_order(car_id)
                    if result == 'restart':
                        raise ApiException(ErrorCode.ReStartPC)
                        # result = []
                    else:
                        print('sort')
                        try:
                            result.sort(key=lambda obj: obj.get('createdTime'), reverse=True)
                        except Exception as sortE:
                            print(sortE)
                    try:
                        for data in result:
                            print(data)
                            msg = data.get("msg")
                            for msg_data in msg:
                                temp = {}
                                attribute = msg_data.get("attribute")
                                for k, v in attribute.items():
                                    if v != "" and v != "-":
                                        temp[k] = v
                                msg_data['attribute'] = temp
                    except Exception as forException:
                        print(forException)

                    send_msg = {
                        'orderMsg': result,
                        'orderNumber': order_number,
                        'allOrderMoney': all_order_money
                    }
                    print(send_msg)
                    return set_return_dicts(send_msg)

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])

    @staticmethod
    def get_order(car_id):
        all_order_money = 0.0
        order_number = 0
        result = sale_handler.get_sale_info_by_one_key('carId', car_id)
        sale_info_list = defaultdict(list)
        print(car_id)
        for data in result:
            attribute = OrderedDict(json.loads(data[8]))
            pc_sign = data[11]
            try:
                price = float(attribute.pop("总价", 0))
            except Exception as e:
                print(e)
                price = 0
            print(price)
            all_order_money += price
            order_no = data[1]
            order_check_id = data[10]
            msg = {
                "project": data[7],
                "price": price,
                'attribute': attribute,
            }
            if order_no not in sale_info_list.keys():
                # 如果没有保存此项则新建
                temp = {
                    "createdTime": data[0],
                    "msg": [msg],
                    "orderNo": order_no,
                    "orderCheckId": order_check_id,
                    'pcSign': pc_sign,
                }
                temp["totalPrice"] = price

                sale_info_list[order_no] = temp
            else:
                temp = sale_info_list[order_no]
                temp["totalPrice"] = price + temp.get("totalPrice")
                temp["msg"].append(msg)
                sale_info_list[order_no] = temp
        result = list()
        for k, v in sale_info_list.items():
            result.append(v)
            order_number += 1
        print(result)
        return result, order_number, all_order_money

    @staticmethod
    def find_customer(key, value):
        result = get_like_customer_by_key(key, value)
        temp = list()
        for data in result:
            # userName,carModel,carPhone,carId
            temp.append({
                "userId": data[0],
                "userName": data[1],
                "carModel": data[2],
                "phone": data[3],
                "carId": data[4],
            })
        return temp
