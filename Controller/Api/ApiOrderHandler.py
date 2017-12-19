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
from Common.StaticFunc import ErrorCode,Set_return_dicts,GetOrderId
from Common.MyExecption import ApiException
from tornado.concurrent import run_on_executor
from datetime import datetime
import configparser
from Common.Common import SocketServer,cncurrency
import json
from collections import OrderedDict
from Controller.Interface.PrinterHandler import Printer
import requests
from Common.config import domain
import logging

class ApiOrder_Handler(Base_Handler):
    def __init__(self,application,request,**kwargs):
        super(ApiOrder_Handler,self).__init__(application,request,**kwargs)
        self.func = self.ApiOrder
        # self.logger = logging.getLogger('mytest')
        # self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('test.log')
        self.fh.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)

        # 给logger添加handler
        # self.logger.addHandler(self.fh)

    def GetPreviewHtml(self,getData,getHeight=False):
        mustSet = ['数量','单价','小计','总价','单位','备注']

        if getData.get("createdTime"):
            today = getData.get("createdTime")
        else:
            today = datetime.now()

        if getData.get("orderNo"):
            orderNo = getData.get("orderNo")
        else:
            orderNo = self.dbhelp.GetOrderNo(today)

        parameter = getData.get("parameter",[])
        if type(parameter) == str:
            parameter = json.loads(parameter)

        carUser = getData.pop("carUser","1")
        carId = getData.pop("carId","1")
        carPhone = getData.pop("carPhone","1")
        pcSign = getData.pop("pcSign","1")
        pcId = getData.pop("pcId","1")
        root = 'config.ini'
        basicMsg = configparser.ConfigParser()
        basicMsg.read(root)

        try:
            if not self.connect:
                raise
            code = basicMsg.get("msg",'code')
            url = domain+"store/api/detail?code={}".format(code)
            req = requests.get(url=url)
            resultData = json.loads(req.text)
        except:
            fp = open("pc.conf",'rb')
            pcData = fp.readline().decode()
            fp.close()
            pcData = pcData.split(',')

            if len(pcData) < 4:
               pcData = [pcData[0],"","",""]

            resultData = {
                        'data' : {
                                "pcId" : pcData[0],
                                "pcPhone" : pcData[1],
                                "pcAddress" : pcData[2],
                                "pcSign" : pcData[3],
                            },
                         'code' : 200
                    }
        if resultData.get("code") != 200:
            storeName = ""
            pcAddress = ""
            pcPhone = ""
        else:
            storeName = resultData.get("data").get("pcSign","")
            pcAddress = resultData.get("data").get("pcAddress","")
            pcPhone = resultData.get("data").get("pcPhone","")

        fp = open("printer.txt",'rb')
        data = fp.readline().decode().replace("\n","").replace("\r","").replace("\ufeff","")
        fp.close()
        fontSize = 7
        if data:
            try:
                fontSize = int(data)
            except:
                fontSize = 7

        header = """<html>
                    <style>
                        table{
                            background-color:#000000
                        }

                        .linetd{
                            text-align: center;
                            border:solid 1px #000;
                            width: 820px;
                            color: red;
                            height: 30px;
                        }

                        .halftd{
                            border:solid 1px #000;
                            width: 410px;
                        }

                        #content{
                            text-align: center;
                            border:solid 1px #000;
                            position: relative;
                            top: 50%;
                            transform: translateY(-50%);
                        }

                        td{
                            padding:2px;
                            align:center;
                            border:1px solid black;
                            background-color:#ffffff
                        }

                """ + "*{font-size:"+str(fontSize)+"pt;}"+ ".bigWord{font-size:"+str(fontSize*1.5)+"pt;}" + "</style><head></head>"

        #总长度要减去备注和名称，因为名称长度另外设置，备注不打印
        try:
            if parameter:
                tempAttribute = parameter[0].get('attribute')
        except:
            raise ApiException(ErrorCode.PrinterError)

        tdWidth = 19
        # self.logger.info('begin body')
        body = """
            <body >
                <div style="width:100%;text-align:center">
                <table width=100% CELLPADDING="0" CELLSPACING="1" border="0">
                    <tr>
                        <td class="bigWord" align="center" colspan="100" width="100%">
                            {storeName}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="50">车牌号：{carId}</td>
                        <td colspan="50">销售日期：{createdTime}</td>
                    </tr>
                    <tr>
                        <td colspan="50">客户电话：{carPhone}</td>
                        <td colspan="50">销售单号：<span style="">{orderNo}</span></td>
                    </tr>
                    <tr>
                        <td colspan="100" height="20px"> </td>
                    </tr>

            """.format(storeName=pcSign,carId=carId,createdTime=today.strftime("%Y-%m-%d %H:%M:%S"),carPhone=carPhone,orderNo=orderNo)

        content = ""
        xuhao = 1
        zongjia = 0
        pageHeight = 100
        # self.logger.info('begin make attribute')
        for order in parameter:
            attribute = order.get("attribute")
            baseHeight = 180
            #手动排序
            #mustSet = ['数量','单价','小计','总价','单位','备注']
            #去除mustset后的必然顺序为："品牌","型号","工时费","更换里程"
            #后面用字符串排序key来排序
            tempKeyList2 = ["品牌","型号","工时费","更换里程"]
            tempKeyList = list()
            for t in tempKeyList2:
                if attribute.get(t) and attribute.get(t) != '-':
                    tempKeyList.append(t)

            for k,v in attribute.items():
                if k not in mustSet+["品牌","型号","工时费","更换里程"] and v != "-"  and v != "" and k != "检索ID":
                    tempKeyList.append(k)
            tempKeyList.sort()
            noMustSet = OrderedDict()
            keyListLen = 0
            for k in tempKeyList:
                noMustSet[k] = attribute.get(k)
                keyListLen += 1
            #总长度要减去备注和名称，因为名称长度另外设置，备注不打印
            td = ""
            keyDict = dict()
            i = 0
            j = 0
            tdList = list()
            keyList = list()
            for k,v in noMustSet.items():
                # if k not in mustSet:
                    td += "<td colspan=\"{tdWidth}\" align=\"center\">{key}</td>".format(tdWidth=tdWidth,key=k)
                    keyList.append(k)
                    if i >= 4:
                        i = 0
                        tdList.append(td)
                        td = ""
                        keyDict[j] = keyList
                        keyList = list()
                        j += 1
                    else:
                        i += 1
            pageHeight += int(keyListLen/5 + 1) * 60 + baseHeight
            #补齐
            if keyList:
                if len(keyList) < 5:
                    num = len(keyList)
                    for i in range(5-num):
                        keyList.append("")
                        td += "<td colspan=\"{tdWidth}\" align=\"center\"></td>".format(tdWidth=tdWidth)
                tdList.append(td)
                keyDict[j] = keyList
            #序号合并列数
            xuNum = len(tdList)*2 + 2
            content += """
                    <tr style="font-weight:800">
                        <td colspan="5" align="center">序</td>
                        <td colspan="{tdWidth}" align="center">名称</td>
                        <td colspan="{tdWidth}" align="center">单位</td>
                        <td colspan="{tdWidth}" align="center">数量</td>
                        <td colspan="{tdWidth}" align="center">单价</td>
                        <td colspan="{tdWidth}" align="center">小计</td>
                    </tr>
                    <tr>
                        <td rowspan="{xuNum}" colspan="5" align="center">{xuhao}</td>
                        <td colspan="{tdWidth}" align="center">{project}</td>
                        <td colspan="{tdWidth}" align="center">{unit}</td>
                        <td colspan="{tdWidth}" align="center">{number}</td>
                        <td colspan="{tdWidth}" align="center">{unitPrice}</td>
                        <td colspan="{tdWidth}" align="center">{xiaoji}</td>
                    </tr>

            """.format(xuNum=xuNum,xuhao=xuhao,unit=attribute.get("单位",""),number=attribute.get("数量",""),unitPrice=attribute.get("单价",""),
                        xiaoji=attribute.get('小计',""),tdWidth=tdWidth,project=order.get("project"))

            moreContent = ""
            ii = 0
            for td in tdList:
                #先放入表头
                moreContent += "<tr style=\"font-weight:800\">" + td + "</tr>"
                #再放入内容
                moreContent += """
                                <tr>
                                    <td colspan="{tdWidth}" align="center">{one}</td>
                                    <td colspan="{tdWidth}" align="center">{two}</td>
                                    <td colspan="{tdWidth}" align="center">{three}</td>
                                    <td colspan="{tdWidth}" align="center">{four}</td>
                                    <td colspan="{tdWidth}" align="center">{five}</td>
                                </tr>
                            """.format(tdWidth=tdWidth,one=attribute.get(keyDict[ii][0],"-") if keyDict[ii][0] != '' else "",
                                       two=attribute.get(keyDict[ii][1],"-") if keyDict[ii][1] != '' else "",
                                       three=attribute.get(keyDict[ii][2],"-") if keyDict[ii][2] != '' else "",
                                       four=attribute.get(keyDict[ii][3],"-") if keyDict[ii][3] != '' else "",
                                       five=attribute.get(keyDict[ii][4],"-") if keyDict[ii][4] != '' else "")
                ii += 1
            fenge = """
                <tr>
                    <td colspan="100" height="20px"> </td>
                </tr>
            """

            zongjiaconetent = """
                            <tr>
                                <td colspan="95">总价：{zongjia}</td>
                            </tr>
                        """.format(zongjia=attribute.get('总价',""))
            content += moreContent + zongjiaconetent + fenge
            xuhao += 1
            zongjia += float(attribute.get('总价',0))

        # self.logger.info('end make attribute')
        zongjia = str(zongjia)
        cn = cncurrency(zongjia)

        foot = """
            <tr>
                <td style="height:35px" colspan="70">合计人名币（大写）：{cn}</td>
                <td style="height:35px"  colspan="30">小写：{zongjia}</td>
            </tr>
            <tr>
                <td colspan="30">{storeName}</td>
                <td colspan="35">地址：{pcAddress}</td>
                <td colspan="35">联系电话：{pcPhone}</td>
            </tr>
                </table>
            </div>
            </body>
            </html>
        """.format(cn=cn,zongjia=zongjia,storeName=pcSign,pcPhone=pcPhone,pcAddress=pcAddress)

        html = header + body + content + foot
        # self.logger.info('add str end')
        if getHeight:
            return html,pageHeight
        else:
            return html

    @run_on_executor
    def ApiOrder(self,keyWord,getData):
        try:
            if self.request.method == 'POST':
                if keyWord == "add":
                   today = datetime.now()

                   orderNo = self.dbhelp.GetOrderNo(today)

                   getData["orderNo"] = orderNo
                   getData["createdTime"] = today

                   try:
                   # if True:
                       carUser = getData.get("carUser")
                       userId = getData.get("userId")
                       workerId = getData.get("workerId")
                       pcId = getData.get("pcId")
                       carPhone = getData.get("carPhone")
                       carModel = getData.get("carModel")
                       carId = getData.get("carId")
                       pcSign = getData.get("pcSign")
                       workerName = getData.get("workerName")
                       root = 'config.ini'
                       basicMsg = configparser.ConfigParser()
                       basicMsg.read(root)
                       orderCheckId = GetOrderId()
                       saveData = {
                            'createdTime' : getData.get("createdTime").strftime("%Y-%m-%d %H:%M:%S"),
                            'userId' : userId,
                            'pcId' : pcId,
                            'pcSign' : pcSign,
                            'carId' : carId,
                            'workerName' : workerName,
                            'workerId' : workerId,
                            'carUser' : carUser,
                            'carPhone' : carPhone,
                            'carModel' : carModel,
                            "orderNo":orderNo,
                            "orderCheckId":orderCheckId,
                            'code' : basicMsg.get("msg","code"),

                        }

                       parameter = getData.get("parameter",[])
                       if type(parameter) == str:
                           parameter = json.loads(parameter)

                       page = 0
                       for data in parameter:
                            page += 1
                            orderId = GetOrderId()
                            temp = {
                                    'project':data.get('project'),
                                     'id' : orderId,
                                     'attribute' : json.dumps(data.get('attribute'))
                            }
                            self.dbhelp.InsertXiaoFei(dict(temp, **saveData))
                            #回访设置
                            if data.get("callbackTime"):
                               dbname = "CallBack"
                               key = "{},{},{},{},{},{}".format("callbackTime","phone",'carId',"username",'createdTime','state')
                               value = "\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\'".format(data.get("callbackTime"),carPhone,carId,carUser,today,'0')
                               self.dbhelp.InsertData(dbname,key,value)
                   except:
                       raise ApiException(ErrorCode.ParameterMiss)

                   try:
                   # if True:
                       #打印
                       p = "defaultPrinter" #打印机名称
                       html,pageHeight = self.GetPreviewHtml(getData,True)
                       Printer.printing(p, html,pageHeight)
                   except:
                       # raise ApiException(ErrorCode.PrinterError)
                        pass

                   return Set_return_dicts({"orderNo":orderNo})

                elif keyWord == 'preview':
                    # self.logger.info('============begin-printer==============')
                    html = self.GetPreviewHtml(getData)
                    # self.logger.info('============end-printer==============')
                    return Set_return_dicts(html)

                else:
                   raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":

                if not self.storeId:
                    raise ApiException(ErrorCode.PCError)

                if keyWord == "detail":

                   checkOrderId = getData.get("checkOrderId")
                   if not checkOrderId:
                       raise ApiException(ErrorCode.ParameterMiss)

                   if self.connect:
                        resultDict = SocketServer("orderdetail {} {}".format(self.storeId,checkOrderId))

                   else:
                        result = self.dbhelp.GetXiaoFeiByKey("orderCheckId",checkOrderId)
                        resultList = list()

                        resultDict = {}
                        if result:
                            createdTime = ''
                            carId = ''
                            carUser = ''
                            carPhone = ''
                            carModel = ''
                            totalPrice = 0
                            pcId = ''
                            orderNo = ''
                            for data in result:
                                attribute = OrderedDict(json.loads(data[8]))
                                createdTime = data[0]
                                carId = data[2]
                                carUser = data[3]
                                carPhone = data[4]
                                carModel = data[5]
                                price = float(attribute.get("总价",0))
                                pcId = data[9]
                                orderNo = data[1]
                                if pcId:
                                    totalPrice += price
                                    attribute['project'] = data[7]
                                    attribute['totalPrice'] = price
                                    attribute['orderNo'] = orderNo
                                    resultList.append(attribute)

                            fp = open("pc.conf",'rb')
                            pcData = fp.readline().decode()
                            pcData = pcData.split(',')
                            fp.close()
                            try:
                                pcSign = pcData[3]
                            except:
                                pcSign = ""
                            resultDict = {
                                "msg" : resultList,
                                "totalPrice" : totalPrice,
                                "createdTime" : createdTime,
                                "carId" : carId,
                                "carUser" : carUser,
                                "carPhone" : carPhone,
                                "carModel" : carModel,
                                "orderNo" : orderNo,
                                "checkOrderId" : checkOrderId,
                                "pcSign" : pcSign,
                            }

                   if resultDict == 'restart':
                       raise ApiException(ErrorCode.ReStartPC)
                       # resultDict = {}
                   return Set_return_dicts(resultDict)


                else:
                   raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return Set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])

