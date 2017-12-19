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
from Controller.Api.BaseHandler import Base_Handler
from Common.StaticFunc import ErrorCode,Set_return_dicts
from Common.MyExecption import ApiException
import configparser
from tornado.concurrent import run_on_executor
from datetime import datetime

class ApiService_Handler(Base_Handler):
    def __init__(self,application,request,**kwargs):
        super(ApiService_Handler,self).__init__(application,request,**kwargs)
        self.func = self.ApiService

    @run_on_executor
    def ApiService(self,keyWord,getData):
        try:
            if self.request.method == "GET":
                if keyWord == "one":
                   resultData = self.dbhelp.getOneMenu()
                   sendData = list()
                   for data in resultData:
                       sendData.append({
                           "oneMenuId":data[0],
                           "name":data[1]
                       })
                   return Set_return_dicts(sendData)

                elif keyWord == "two":
                   id = getData.get("oneMenuId")
                   resultData = self.dbhelp.getTwoMenu(id)
                   sendData = list()
                   for data in resultData:
                       attribute = data[2].split(',')
                       attributeState = data[3].split(',')
                       attributeDict = {}
                       for i in range(len(attribute)):
                           if attribute[i] != "" and attributeState[i] == '1':
                              attributeDict[attribute[i]] = attributeState[i]

                       sendData.append({
                           "twoMenuId" : data[0],
                           "name" : data[1],
                           "attribute" : attributeDict,
                       })
                   return Set_return_dicts(sendData)

                else:
                   raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return Set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])

