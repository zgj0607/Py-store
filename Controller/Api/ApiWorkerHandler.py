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
from Controller.Api.BaseHandler import BaseHandler
from Common.StaticFunc import ErrorCode,set_return_dicts
from Common.MyExecption import ApiException
import configparser
from tornado.concurrent import run_on_executor
from datetime import datetime
import requests
from Common.config import domain
import json

class ApiWorker_Handler(BaseHandler):
    def __init__(self,application,request,**kwargs):
        super(ApiWorker_Handler,self).__init__(application,request,**kwargs)
        self.func = self.ApiWorker

    @run_on_executor
    def ApiWorker(self,keyWord,getData):
        try:
            if self.request.method == 'POST':
                if keyWord == "code":
                   result = {}
                   code = getData.get("code","").strip()
                   root = 'config.ini'
                   basicMsg = configparser.ConfigParser()
                   basicMsg.read(root)
                   localCode = basicMsg.get("msg","code")
                   if code != "" and localCode == code:
                      #请求获取门店信息
                      if self.connect:
                          url = domain + "store/api/detail?code={}".format(code)
                          try:
                              req = requests.get(url)
                              jsonData = req.text
                              data = json.loads(jsonData)
                          except:
                              fp = open("pc.conf",'rb')
                              pcData = fp.readline().decode()
                              fp.close()
                              pcData = pcData.split(',')
                              if len(pcData) < 4:
                                  pcData = [pcData[0],"","",""]
                              data = {
                                  'data' : {
                                              "pcId" : pcData[0],
                                              "pcPhone" : pcData[1],
                                              "pcAddress" : pcData[2],
                                              "pcSign" : pcData[3],
                                  },
                                  'code' : 200
                              }
                      else:
                          fp = open("pc.conf",'rb')
                          pcData = fp.readline().decode()
                          fp.close()
                          pcData = pcData.split(',')
                          if len(pcData) < 4:
                             pcData = [pcData[0],"","",""]
                          data = {
                                  'data' : {
                                            "pcId" : pcData[0],
                                            "pcPhone" : pcData[1],
                                            "pcAddress" : pcData[2],
                                            "pcSign" : pcData[3],
                                },
                                'code' : 200
                          }
                      if data.get('code') == 200:
                          result = data.get("data")
                      else:
                          raise ApiException(ErrorCode.CodeError)
                   else:
                       raise ApiException(ErrorCode.CodeError)

                   return set_return_dicts(result)

                elif keyWord == "ip":
                   return set_return_dicts(True)

                else:
                   raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":
                if keyWord == "list":
                   worker = self.dbhelp.GetWorker()
                   workerList = list()
                   for data in worker:
                       workerList.append({
                           "workerId" : data[0],
                           "workerName" : data[1]
                       })
                   return set_return_dicts(workerList)
                else:
                   raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])

