# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
                   ┏┓      ┏┓
                ┏┛┻━━━┛┻┓
               ┃      ☃      ┃
              ┃  ┳┛  ┗┳  ┃
             ┃      ┻      ┃
            ┗━┓      ┏━┛
               ┃      ┗━━━┓
              ┃              ┣┓
             ┃　            ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
import json
import time
# 这个并发库在python3自带在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor

import tornado
from tornado import web, gen, ioloop

import Common.config as config
from Common import Common, time_utils
from Common.Common import get_store_id
from Common.MyExecption import ApiException
from Common.StaticFunc import ErrorCode, set_return_dicts
from Controller.DbHandler import DB_Handler
from database.dao.device import device_handler
from domain.device import Device


class BaseHandler(web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.executor = ThreadPoolExecutor(10)
        self.__keyWord = None
        self.func = None
        self.dbhelp = DB_Handler()
        # 请求ip
        self.spbill_create_ip = self.request.remote_ip
        self.deviceName = self.request.headers.get("Devicename", "")
        self.connect = config.connect
        try:
            self.storeId = get_store_id()
        except:
            self.storeId = None

    # 设置头部
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    # 获取表单内容
    def get_all_argument(self):
        argument = self.request.arguments
        result = dict()
        for name, value in argument.items():
            if len(value) == 1:
                result[name] = value[0].decode()
            else:
                for data in value:
                    data = data.decode()
                result[name] = value
        print("入参：", result)

        return result

    @web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            # 异步
            yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout, time.time())
            if args != ():
                self.__keyWord = args[0]

            get_data = self.get_all_argument()
            if len(args) > 1:
                get_data['args'] = list(args)
                get_data['args'].remove(self.__keyWord)

            check_result = self.check_device()
            if not check_result:
                raise ApiException(ErrorCode.UserStateError)
            elif check_result == 2:
                raise ApiException(ErrorCode.UserStateWaitError)

            if self.__keyWord:
                result = yield self.func(self.__keyWord, get_data)
            else:
                result = yield self.func(get_data)

            transmission_result = json.dumps(result)

            self.write(transmission_result)
            self.finish()

        except ApiException as e:
            self.write(json.dumps(set_return_dicts(forWorker=e.error_result['forWorker'],
                                                   code=e.error_result['errorCode'],
                                                   forUser=e.error_result['forUser'])))
            self.finish()

        except Exception as commException:
            print(commException)
            self.write(json.dumps(set_return_dicts(forWorker='不合法的参数',
                                                   code=ErrorCode.ParameterError,
                                                   forUser='请求超时')))

            self.finish()

    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        try:
            # 异步
            yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout, time.time())
            if args != ():
                self.__keyWord = args[0]

            # json传输
            try:
                get_data = json.loads(self.request.body.decode())
            except Exception as outer:
                print(outer)
                try:
                    get_data = self.get_all_argument()
                except Exception as inner:
                    print(inner)
                    raise ApiException(ErrorCode.JsonError)
            # print ('post:',get_Data)

            check_result = self.check_device()
            if not check_result:
                raise ApiException(ErrorCode.UserStateError)
            elif check_result == 2:
                raise ApiException(ErrorCode.UserStateWaitError)

            if self.__keyWord:
                result = yield self.func(self.__keyWord, get_data)
            else:
                result = yield self.func(get_data)

            transmission_result = json.dumps(result)
            self.write(transmission_result.encode('utf-8'))
            self.finish()

        except ApiException as e:
            self.write(json.dumps(set_return_dicts(forWorker=e.error_result['forWorker'],
                                                   code=e.error_result['errorCode'],
                                                   forUser=e.error_result['forUser'])))

            self.finish()

    def check_device(self):
        device = Device()
        device.ip(self.spbill_create_ip)
        device.create_time(time_utils.get_now())
        device.name(self.deviceName)

        data = device_handler.get_device_info_by_ip(self.spbill_create_ip)
        if not data:
            Common.config.ui.pad_connect_signal.emit(device)
            check_result = 2
        else:
            check_result = (data[1] == Device.enable())

        return check_result
