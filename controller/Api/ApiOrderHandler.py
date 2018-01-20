# -*- coding: utf-8 -*-

import json
import logging
from collections import OrderedDict
from datetime import datetime

import requests
from tornado.concurrent import run_on_executor

from common import config
from common.common import SocketServer, cncurrency
from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts, get_order_id
from common.config import domain
from controller.Api.BaseHandler import BaseHandler
from controller.Interface.PrinterHandler import Printer
from database.dao.customer import customer_handler
from database.dao.sale import sale_handler, sale_item_handler
from database.dao.sale.sale_handler import get_sale_info_by_one_key, get_sale_order_no
from database.dao.service import service_handler, attribute_handler


class ApiOrder_Handler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ApiOrder_Handler, self).__init__(application, request, **kwargs)
        self.func = self.ApiOrder
        self.fh = logging.FileHandler('test.log')
        self.fh.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)

        # 给logger添加handler
        # self.logger.addHandler(self.fh)

    def preview_html(self, get_data, get_height=False):
        must_set = ['数量', '单价', '小计', '总价', '单位', '备注']
        if get_data.get("createdTime"):
            today = get_data.get("createdTime")
        else:
            today = datetime.now()

        if get_data.get("orderNo"):
            order_no = get_data.get("orderNo")
        else:
            order_no = sale_handler.get_sale_order_no(today)

        parameter = get_data.get("parameter", [])
        if type(parameter) == str:
            parameter = json.loads(parameter)

        carUser = get_data.pop("carUser", "1")
        carId = get_data.pop("carId", "1")
        carPhone = get_data.pop("carPhone", "1")
        pcSign = get_data.pop("pcSign", "1")
        pcId = get_data.pop("pcId", "1")

        try:
            if not self.connect:
                raise ApiException(ErrorCode.ErrorRequest)
            code = config.get_local_register_code()
            url = domain + "store/api/detail?code={}".format(code)
            req = requests.get(url=url)
            result_data = json.loads(req.text)
        except Exception as exception:
            print(exception)
            store = config.get_local_store_info()

            result_data = {
                'data': {
                    "pcId": store.id(),
                    "pcPhone": store.phone(),
                    "pcAddress": store.address(),
                    "pcSign": store.name(),
                },
                'code': 200
            }
        if result_data.get("code") != 200:
            storeName = ""
            pcAddress = ""
            pcPhone = ""
        else:
            storeName = result_data.get("data").get("pcSign", "")
            pcAddress = result_data.get("data").get("pcAddress", "")
            pcPhone = result_data.get("data").get("pcPhone", "")

        font_size = config.get_print_font_size()
        print("header")
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

                """ + "*{font-size:" + str(font_size) + "pt;}" + ".bigWord{font-size:" + str(
            font_size * 1.5) + "pt;}" + "</style><head></head>"

        # 总长度要减去备注和名称，因为名称长度另外设置，备注不打印
        try:
            if parameter:
                tempAttribute = parameter[0].get('attribute')
        except:
            raise ApiException(ErrorCode.PrinterError)

        td_width = 19
        print('begin body')
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

            """.format(storeName=pcSign, carId=carId, createdTime=today.strftime("%Y-%m-%d %H:%M:%S"),
                       carPhone=carPhone, orderNo=order_no)

        content = ""
        sequence = 1
        total_price = 0
        page_height = 100
        # self.logger.info('begin make attribute')
        for order in parameter:
            attribute = order.get("attribute")
            baseHeight = 180
            # 手动排序
            # mustSet = ['数量','单价','小计','总价','单位','备注']
            # 去除mustset后的必然顺序为："品牌","型号","工时费","更换里程"
            # 后面用字符串排序key来排序
            tempKeyList2 = ["品牌", "型号", "工时费", "更换里程"]
            tempKeyList = list()
            for t in tempKeyList2:
                if attribute.get(t) and attribute.get(t) != '-':
                    tempKeyList.append(t)

            for k, v in attribute.items():
                if k not in must_set + ["品牌", "型号", "工时费", "更换里程"] and v != "-" and v != "" and k != "检索ID":
                    tempKeyList.append(k)
            tempKeyList.sort()
            noMustSet = OrderedDict()
            keyListLen = 0
            for k in tempKeyList:
                noMustSet[k] = attribute.get(k)
                keyListLen += 1
            # 总长度要减去备注和名称，因为名称长度另外设置，备注不打印
            td = ""
            keyDict = dict()
            i = 0
            j = 0
            tdList = list()
            keyList = list()
            for k, v in noMustSet.items():
                # if k not in mustSet:
                td += "<td colspan=\"{tdWidth}\" align=\"center\">{key}</td>".format(tdWidth=td_width, key=k)
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
            page_height += int(keyListLen / 5 + 1) * 60 + baseHeight
            # 补齐
            if keyList:
                if len(keyList) < 5:
                    num = len(keyList)
                    for i in range(5 - num):
                        keyList.append("")
                        td += "<td colspan=\"{tdWidth}\" align=\"center\"></td>".format(tdWidth=td_width)
                tdList.append(td)
                keyDict[j] = keyList
            # 序号合并列数
            xuNum = len(tdList) * 2 + 2
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

            """.format(xuNum=xuNum, xuhao=sequence, unit=attribute.get("单位", ""), number=attribute.get("数量", ""),
                       unitPrice=attribute.get("单价", ""),
                       xiaoji=attribute.get('小计', ""), tdWidth=td_width, project=order.get("project"))

            moreContent = ""
            ii = 0
            for td in tdList:
                # 先放入表头
                moreContent += "<tr style=\"font-weight:800\">" + td + "</tr>"
                # 再放入内容
                moreContent += """
                                <tr>
                                    <td colspan="{tdWidth}" align="center">{one}</td>
                                    <td colspan="{tdWidth}" align="center">{two}</td>
                                    <td colspan="{tdWidth}" align="center">{three}</td>
                                    <td colspan="{tdWidth}" align="center">{four}</td>
                                    <td colspan="{tdWidth}" align="center">{five}</td>
                                </tr>
                            """.format(tdWidth=td_width,
                                       one=attribute.get(keyDict[ii][0], "-") if keyDict[ii][0] != '' else "",
                                       two=attribute.get(keyDict[ii][1], "-") if keyDict[ii][1] != '' else "",
                                       three=attribute.get(keyDict[ii][2], "-") if keyDict[ii][2] != '' else "",
                                       four=attribute.get(keyDict[ii][3], "-") if keyDict[ii][3] != '' else "",
                                       five=attribute.get(keyDict[ii][4], "-") if keyDict[ii][4] != '' else "")
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
                        """.format(zongjia=attribute.get('总价', ""))
            content += moreContent + zongjiaconetent + fenge
            sequence += 1
            total_price += float(attribute.get('总价', 0))

        # self.logger.info('end make attribute')
        total_price = str(total_price)
        cn = cncurrency(total_price)

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
        """.format(cn=cn, zongjia=total_price, storeName=pcSign, pcPhone=pcPhone, pcAddress=pcAddress)

        html = header + body + content + foot
        # self.logger.info('add str end')
        if get_height:
            return html, page_height
        else:
            return html

    @run_on_executor
    def ApiOrder(self, keyWord, getData):
        try:
            if self.request.method == 'POST':
                if keyWord == "add":
                    today = datetime.now()

                    orderNo = get_sale_order_no(today)

                    getData["orderNo"] = orderNo
                    getData["createdTime"] = today
                    print(keyWord)
                    try:
                        # if True:
                        carUser = getData.get("carUser")
                        userId = getData.get("userId")
                        workerId = getData.get("workerId")
                        pcId = getData.get("pcId")
                        carPhone = getData.get("carPhone")
                        carModel = getData.get("carModel")
                        carId = getData.get("carId")
                        pc_sign = getData.get("pcSign")
                        workerName = getData.get("workerName")
                        orderCheckId = get_order_id()
                        saveData = {
                            'createdTime': getData.get("createdTime").strftime("%Y-%m-%d %H:%M:%S"),
                            'userId': userId,
                            'pcId': pcId,
                            'pcSign': pc_sign,
                            'carId': carId,
                            'workerName': workerName,
                            'workerId': workerId,
                            'carUser': carUser,
                            'carPhone': carPhone,
                            'carModel': carModel,
                            "orderNo": orderNo,
                            "orderCheckId": orderCheckId,
                            'code': config.get_local_register_code(),

                        }

                        parameter = getData.get("parameter", [])
                        if type(parameter) == str:
                            parameter = json.loads(parameter)

                        page = 0
                        for data in parameter:
                            page += 1
                            order_id = get_order_id()

                            services = data.get('project')
                            services = services.split('-')
                            first_service_name = services[0]
                            second_service_name = services[1]

                            first_service_id = service_handler.get_service_id_by_name(first_service_name)[0]
                            second_service_id = service_handler.get_service_id_by_name(second_service_name,
                                                                                       first_service_id)[0]

                            attributes = data.get('attribute')
                            print(attributes)
                            try:
                                unit = attributes.get('单位', '')
                                unit_price = float(attributes.pop('单价', ''))
                                number = int(attributes.get('数量', ''))
                                subtotal = float(attributes.get('小计', ''))
                                total = float(attributes.get('总价', ''))
                                note = attributes.get('备注', '')
                            except Exception as attribute_deal_error:
                                print(attribute_deal_error)
                                unit = ''
                                unit_price = 0.0
                                number = 0
                                subtotal = 0.0
                                total = 0.0
                                note = ''

                            temp = {
                                'project': data.get('project'),
                                'id': order_id,
                                'attribute': json.dumps(data.get('attribute')),
                                'serviceId': second_service_id,
                                'unit': unit,
                                'unit_price': unit_price,
                                'number': number,
                                'subtotal': subtotal,
                                'total': total,
                                'note': note
                            }

                            sale_id = sale_handler.add_sale_info(dict(temp, **saveData))
                            service_attrs = service_handler.get_attribute_by_service(second_service_id)
                            print(service_attrs)
                            all_required_attr = attribute_handler.get_all_required_attributes()
                            required_attr_list = []
                            for attr in all_required_attr:
                                required_attr_list.append(attr[1])

                            for srv_attr in service_attrs:
                                attr_name = srv_attr[1]
                                if attr_name not in required_attr_list:
                                    attr_id = attribute_handler.get_attr_by_name(attr_name)[0]
                                    sale_item_handler.add_sale_item(order_id, attr_id, attributes.get(attr_name, ''))

                            # 回访设置
                            if data.get("callbackTime"):
                                dbname = "CallBack"
                                key = "{},{},{},{},{},{}".format("callbackTime", "phone", 'carId', "username",
                                                                 'createdTime', 'state')
                                value = "\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\'".format(data.get("callbackTime"),
                                                                                           carPhone, carId, carUser,
                                                                                           today, '0')
                                self.dbhelp.InsertData(dbname, key, value)
                                customer_handler.add_return_visit_data(data.get("callbackTime"), carPhone, carId,
                                                                       carUser, today)
                    except Exception as add_error:
                        print(add_error)
                        raise ApiException(ErrorCode.ParameterMiss)

                    try:
                        # if True:
                        # 打印
                        p = "defaultPrinter"  # 打印机名称
                        html, pageHeight = self.preview_html(getData, True)
                        Printer.printing(p, html, pageHeight)
                    except:
                        # raise ApiException(ErrorCode.PrinterError)
                        pass

                    return set_return_dicts({"orderNo": orderNo})

                elif keyWord == 'preview':
                    print('preview')
                    html = self.preview_html(getData)
                    print(html)
                    return set_return_dicts(html)

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
                        result_dict = SocketServer("orderdetail {} {}".format(self.storeId, checkOrderId))

                    else:
                        result = get_sale_info_by_one_key("orderCheckId", checkOrderId)
                        resultList = list()

                        result_dict = {}
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
                                price = data[16]
                                pcId = data[9]
                                orderNo = data[1]
                                if pcId:
                                    totalPrice += price
                                    attribute['project'] = data[7]
                                    attribute['totalPrice'] = price
                                    attribute['orderNo'] = orderNo
                                    resultList.append(attribute)

                            try:
                                pc_sign = config.get_store_name()
                            except:
                                pc_sign = ""
                            result_dict = {
                                "msg": resultList,
                                "totalPrice": totalPrice,
                                "createdTime": createdTime,
                                "carId": carId,
                                "carUser": carUser,
                                "carPhone": carPhone,
                                "carModel": carModel,
                                "orderNo": orderNo,
                                "checkOrderId": checkOrderId,
                                "pcSign": pc_sign,
                            }

                    if result_dict == 'restart':
                        raise ApiException(ErrorCode.ReStartPC)
                        # resultDict = {}
                    return set_return_dicts(result_dict)


                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])
