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
from Common.StaticFunc import ErrorCode,Set_return_dicts,GetToday
from Common.MyExecption import ApiException
from tornado.concurrent import run_on_executor
from Common.Common import SocketServer
import configparser
from collections import OrderedDict,defaultdict
import json

class ApiUser_Handler(Base_Handler):
    def __init__(self,application,request,**kwargs):
        super(ApiUser_Handler,self).__init__(application,request,**kwargs)
        self.func = self.ApiUser

    @run_on_executor
    def ApiUser(self,keyWord,getData):
        try:
            if self.request.method == 'POST':
                if keyWord == "add":
                   try:
                       userName = getData.pop("username")
                       carPhone = getData.pop("carPhone")
                       carModel = getData.pop("carModel")
                       carId = getData.pop("carId")
                   except:
                       raise ApiException(ErrorCode.ParameterMiss)

                   key = "userName,carPhone,carModel,carId,createdTime"
                   value = "'{}','{}','{}','{}','{}'".format(userName,carPhone,carModel,carId,GetToday())
                   tempUser = self.dbhelp.GetUserByKey("carId",carId)
                   if tempUser:
                       updateData = "userName=\'{}\',carPhone=\'{}\',carModel=\'{}\'".format(userName,carPhone,carModel)
                       search = "carId=\'{}\'".format(carId)
                       try:
                          self.dbhelp.UpdateData("User",updateData,search)
                       except:
                          raise ApiException(ErrorCode.ParameterError)
                       userId = tempUser[0][0]
                   else:
                       try:
                          userId = self.dbhelp.InsertData("User",key,value)
                       except:
                          raise ApiException(ErrorCode.UserMore)

                   return Set_return_dicts({"userId":userId})

                else:
                   raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":
                # basicMsg = configparser.ConfigParser()
                # root = 'config.ini'
                # basicMsg.read(root)
                # code = basicMsg.get('msg','code')
                if not self.storeId:
                       raise ApiException(ErrorCode.PCError)

                if keyWord == "find":
                   key = getData.get("key","")
                   if key not in ["carPhone","carId"]:
                       raise ApiException(ErrorCode.ParameterError)

                   value = getData.get("value","")

                   if self.connect:
                      temp = SocketServer("user {} {} {}".format(self.storeId,key,value))
                      if not temp:
                          temp = self.GetFind(key,value)

                   else:
                        temp = self.GetFind(key,value)
                   result = []
                   keyTemp = []
                   if temp == 'restart':
                       raise ApiException(ErrorCode.ReStartPC)
                       # result = []
                   else:
                       for data in temp:
                           key = data.get("phone") + data.get("carId") + data.get("carModel") + data.get("userName")
                           if key in keyTemp:
                               pass
                           else:
                               result.append(data)
                               keyTemp.append(key)

                   return Set_return_dicts(result)

                elif keyWord == 'order':
                    carId = getData.get("carId","")
                    carPhone = getData.get("carPhone","")

                    if not carId:
                        raise ApiException(ErrorCode.ParameterMiss)

                    if self.connect:
                        allOrderMoney = 0
                        result = SocketServer("userorder {} {} {}".format(self.storeId,carId,carPhone))
                        if result:
                            orderNumber = len(result)
                            for data in result:
                                allOrderMoney += data.get("totalPrice")
                        else:
                            result,orderNumber,allOrderMoney = self.GetOrder(carId,carPhone)

                    else:
                        result,orderNumber,allOrderMoney = self.GetOrder(carId,carPhone)

                    if result == 'restart':
                        raise ApiException(ErrorCode.ReStartPC)
                        # result = []
                    else:
                        result.sort(key=lambda obj:obj.get('createdTime'), reverse=True)

                    for data in result:
                        msg = data.get("msg")
                        for msgData in msg:
                            temp = {}
                            attribute = msgData.get("attribute")
                            for k,v in attribute.items():
                                if v != "" and v != "-":
                                    temp[k] = v
                            msgData['attribute'] = temp

                    sendMsg = {
                        'orderMsg' : result,
                        'orderNumber' : orderNumber,
                        'allOrderMoney' : allOrderMoney
                    }
                    return Set_return_dicts(sendMsg)

                else:
                   raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return Set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])

    def GetOrder(self,carId,carPhone):
        allOrderMoney = 0
        orderNumber = 0
        result = self.dbhelp.GetXiaoFeiByKey('carId',carId)
        xiaoFeiList = defaultdict(list)

        for data in result:
            attribute = OrderedDict(json.loads(data[8]))
            pcSign = data[11]
            try:
                price = float(attribute.pop("总价",0))
            except:
                price = 0

            allOrderMoney += price
            orderNo = data[1]
            orderCheckId = data[10]
            msg = {
                "project":data[7],
                "price":price,
                'attribute' : attribute,
            }
            if orderNo not in xiaoFeiList.keys():
                #如果没有保存此项则新建
                temp ={
                    "createdTime" : data[0],
                    "msg" : [msg],
                    "orderNo" : orderNo,
                    "orderCheckId":orderCheckId,
                     'pcSign' : pcSign,
                }
                temp["totalPrice"] = price

                xiaoFeiList[orderNo] = temp
            else:
                temp = xiaoFeiList[orderNo]
                temp["totalPrice"] = price + temp.get("totalPrice")
                temp["msg"].append(msg)
                xiaoFeiList[orderNo]  = temp


        result = list()
        for k,v in xiaoFeiList.items():
            result.append(v)
            orderNumber += 1

        return result,orderNumber,allOrderMoney

    def GetFind(self,key,value):
        result = self.dbhelp.GetLikeUserByKey(key,value)
        temp = list()
        for data in result:
            #userName,carModel,carPhone,carId
            temp.append({
                "userId":data[0],
                "userName":data[1],
                "carModel":data[2],
                "phone":data[3],
                "carId":data[4],
            })
        return temp