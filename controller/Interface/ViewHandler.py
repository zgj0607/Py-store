# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/13'
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
import logging
import re
from collections import OrderedDict
from collections import defaultdict
from datetime import datetime

import requests
import xlrd
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import *

from common import config
from common.common import cncurrency
from common.exception import ApiException
from common.static_func import get_order_id, ErrorCode
from common.config import domain, connect as myconnect
from common.time_utils import get_now
from controller import DbHandler
from database.dao.customer.customer_handler import check_customer
from database.dao.sale.sale_handler import get_sale_info_by_one_key

dbhelp = DbHandler.DB_Handler()
selectOrderNo = None

logger = logging.getLogger(__name__)


def do_printer(mainWin, orderNo):
    try:
        printer = QPrinter(QPrinter.HighResolution)
        # /* 打印预览 */
        preview = QPrintPreviewDialog(printer, mainWin)
        preview.paintRequested.connect(print_html)
        global selectOrderNo
        selectOrderNo = orderNo
        preview.exec_()
        return True

    except Exception as print_exception:
        print(print_exception)
        return False


def print_html(printer):
    try:
        if not myconnect:
            raise ApiException(ErrorCode.ErrorRequest)
        code = config.get_local_register_code()
        url = domain + "store/api/detail?code={}".format(code)
        req = requests.get(url=url)
        result_data = json.loads(req.text)
    except Exception as e:
        logger.error(e.__str__())

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
    mustSet = ['数量', '单价', '小计', '总价', '单位', '备注']

    if result_data.get("code") != 200:
        storeName = ""
        pcAddress = ""
        pcPhone = ""
    else:
        storeName = result_data.get("data").get("pcSign", "")
        pcAddress = result_data.get("data").get("pcAddress", "")
        pcPhone = result_data.get("data").get("pcPhone", "")
    result = get_sale_info_by_one_key("orderCheckId", selectOrderNo)

    font_size = config.get_print_font_size()

    # *{font-size:65px;}
    if result:
        header = """<html>
            <style>
            table{
                background-color:#000000;
            }

            .linetd{
                text-align: center;
                width: 820px;
                color: red;
                height: 30px;
            }

            .halftd{
                width: 410px;
            }

            #content{
                text-align: center;
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
        # *{font-size:50px;}
        tdWidth = 19
        body = """
            <body style="text-align: center;">
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

                    """.format(storeName=storeName, carId=result[0][2], createdTime=result[0][0], carPhone=result[0][4],
                               orderNo=result[0][1])

        content = ""
        xuhao = 1
        zongjia = 0
        page = 0
        pageHeight = 100
        for order in result:
            page += 1
            attribute = json.loads(order[8])
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
                if k not in mustSet + ["品牌", "型号", "工时费", "更换里程"] and v != "-" and v != "" and k != "检索ID":
                    tempKeyList.append(k)
            tempKeyList.sort()
            noMustSet = OrderedDict()
            for k in tempKeyList:
                noMustSet[k] = attribute.get(k)
            # 总长度要减去备注和名称，因为名称长度另外设置，备注不打印
            td = ""
            keyDict = dict()
            i = 0
            j = 0
            tdList = list()
            keyList = list()
            pageHeight += int(len(noMustSet.keys()) / 5 + 1) * 60 + baseHeight
            for k, v in noMustSet.items():
                # if k not in mustSet and v != "-"  and v != "" and k!="检索ID" :
                td += "<td colspan=\"{tdWidth}\" align=\"center\"><b>{key}</b></td>".format(tdWidth=tdWidth, key=k)
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

            # 补齐
            if keyList:
                if len(keyList) < 5:
                    num = len(keyList)
                    for i in range(5 - num):
                        keyList.append("")
                        td += "<td colspan=\"{tdWidth}\" align=\"center\"></td>".format(tdWidth=tdWidth)
                tdList.append(td)
                keyDict[j] = keyList
            # 序号合并列数
            xuNum = len(tdList) * 2 + 2
            # createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,brand," \
            # "model,huawen,number,unitPrice,xiaoji,gongshi,ghlc,remark,totalPrice,pcId,unit
            content += """
                <tr>
                        <td colspan="5" align="center"><b>序</b></td>
                        <td colspan="{tdWidth}" align="center"><b>名称</b></td>
                        <td colspan="{tdWidth}" align="center"><b>单位</b></td>
                        <td colspan="{tdWidth}" align="center"><b>数量</b></td>
                        <td colspan="{tdWidth}" align="center"><b>单价</b></td>
                        <td colspan="{tdWidth}" align="center"><b>小计</b></td>
                    </tr>
                <tr>
                    <td rowspan="{xuNum}" colspan="5" align="center"><br/>{xuhao}</td>
                    <td colspan="{tdWidth}" align="center">{project}</td>
                    <td colspan="{tdWidth}" align="center">{unit}</td>
                    <td colspan="{tdWidth}" align="center">{number}</td>
                    <td colspan="{tdWidth}" align="center">{unitPrice}</td>
                    <td colspan="{tdWidth}" align="center">{xiaoji}</td>
                </tr>

            """.format(xuNum=xuNum, xuhao=xuhao, unit=attribute.get("单位", ""), number=attribute.get("数量", ""),
                       unitPrice=attribute.get("单价", ""),
                       xiaoji=attribute.get('小计', ""), project=order[7], tdWidth=tdWidth)

            moreContent = ""
            ii = 0
            for td in tdList:
                # 先放入表头
                moreContent += "<tr>" + td + "</tr>"
                # 再放入内容
                moreContent += """
                    <tr>
                    <td colspan="{tdWidth}" align="center">{one}</td>
                    <td colspan="{tdWidth}" align="center">{two}</td>
                    <td colspan="{tdWidth}" align="center">{three}</td>
                    <td colspan="{tdWidth}" align="center">{four}</td>
                    <td colspan="{tdWidth}" align="center">{five}</td>
                    </tr>
                """.format(tdWidth=tdWidth, one=attribute.get(keyDict[ii][0], ""),
                           two=attribute.get(keyDict[ii][1], ""),
                           three=attribute.get(keyDict[ii][2], ""), four=attribute.get(keyDict[ii][3], ""),
                           five=attribute.get(keyDict[ii][4], ""))

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
            xuhao += 1
            try:
                zongjia += float(attribute.get('总价', 0))
            except:
                zongjia = 0

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
        </body>
        </html>
        """.format(cn=cn, zongjia=zongjia, storeName=storeName, pcPhone=pcPhone, pcAddress=pcAddress)

        html = header + body + content + foot
        textDocument = QTextDocument()
        textDocument.setHtml(html)
        textDocument.setDocumentMargin(35)
        printer.setPageSize(QPrinter.Custom)
        # height = baseHeight+((page-1)*150)
        # printer.setPaperSize(QSizeF(printer.logicalDpiX()*(86/25.4),height),QPrinter.Point)
        # textDocument.setPageSize(QSizeF(printer.logicalDpiX()*(86/25.4),height))
        printer.setPaperSize(QSizeF(581, pageHeight), QPrinter.Point)
        textDocument.setPageSize(QSizeF(581, pageHeight))
        textOp = QTextOption()
        textOp.setWrapMode(QTextOption.WrapAnywhere)
        textOp.setAlignment(Qt.AlignCenter)
        textDocument.setDefaultTextOption(textOp)
        printer.setOutputFormat(QPrinter.NativeFormat)
        textDocument.print(printer)


def ImportExcel(fileName, self):
    # 用于正则判断是否是用软件导出的excel文档
    pattern = re.compile(r"^门店系统:\d{4}[-/]\d{2}[/-]\d{2}至\d{4}[-/]\d{2}[/-]\d{2}$")
    # matchs = pattern.match()
    bk = xlrd.open_workbook(fileName)
    try:
        sh = bk.sheet_by_name("消费列表")
    except:
        sh = bk.sheet_by_name("Sheet1")
    nrows = sh.nrows
    temp = list()
    titleList = ['检索ID', 'orderNo', 'createdTime', "pcSign", "carId", "carUser", "carPhone", "carModel", "workerName",
                 "project"]
    userList = ["carId", "carUser", "carPhone", "carModel"]
    mustlen = len(titleList)
    check = str(sh.row_values(0)[0])
    matchs = pattern.match(check)
    title = sh.row_values(1)
    progressDialog = QProgressDialog(self)
    progressDialog.setWindowTitle("导入中")
    # progdialog.setWindowModality(Qt.ApplicationModal)
    progressDialog.setWindowModality(Qt.WindowModal)
    progressDialog.setMinimumDuration(4)
    progressDialog.setWindowTitle(self.tr("请等待"))
    progressDialog.setLabelText(self.tr("导入中..."))
    progressDialog.setCancelButtonText(self.tr("取消"))
    progressDialog.setRange(0, nrows - 3)
    progressDialog.show()
    if True:
        p = 0
        msgList = list()
        for i in range(2, nrows):
            # 用正则表达式判断第一行数据内容，从而判断是否用软件导出的EXCEL文档
            if matchs:
                # 若是用软件导出的则
                if progressDialog.wasCanceled():
                    break
                progressDialog.setValue(p)
                p += 1
                try:
                    # if True:
                    saveData = dict()
                    row_data = sh.row_values(i)
                    if i < nrows - 1:
                        temp2 = sh.row_values(i + 1)
                    else:
                        temp2 = None

                    if temp2 != None and temp2[0] == '':
                        # 合并了单元格则合并内容是空，将后面不是空的内容进行缓存，合并的内容会在最后一条信息中显示，
                        # 此时一并进行录入
                        temp.append(row_data)
                    else:

                        # if row_data[0] != '':
                        if temp:
                            orderCheckId = temp[0][0]
                        else:
                            orderCheckId = row_data[0]
                        checkOrder = get_sale_info_by_one_key("orderCheckId", orderCheckId)
                        # 有此订单的就不保存了
                        if not checkOrder:
                            if temp:
                                temp.append(row_data)
                                allMsg = temp[0]
                                # 接入信息后录入
                                for i in range(len(temp)):
                                    if i != 0:
                                        msg = temp[i]
                                        attribute = {}
                                        for ki in range(len(title)):

                                            allMsg[ki] = str(allMsg[ki])
                                            msg[ki] = str(msg[ki])
                                            if ki < mustlen:
                                                tempK = titleList[ki]
                                                if tempK in ['orderNo', 'carPhone']:
                                                    allMsg[ki] = allMsg[ki].replace('.0', "")
                                                    msg[ki] = msg[ki].replace('.0', "")
                                                if titleList[ki] in ["project"]:
                                                    saveData[tempK] = msg[ki]
                                                else:
                                                    if tempK == "检索ID":
                                                        tempK = "orderCheckId"
                                                    saveData[tempK] = allMsg[ki]
                                            else:
                                                if row_data[ki] == "" or row_data[ki] == "-":
                                                    continue
                                                attribute[title[ki]] = msg[ki]

                                        saveData['attribute'] = json.dumps(attribute)
                                        saveData['id'] = get_order_id()
                                        dbhelp.add_sale_info(saveData)

                                    row_data = allMsg
                            attribute = {}
                            userSave = {}
                            for ki in range(len(title)):
                                row_data[ki] = str(row_data[ki])
                                if ki < mustlen:
                                    if titleList[ki] in ['orderNo', 'carPhone']:
                                        row_data[ki] = row_data[ki].replace('.0', "")
                                    key = titleList[ki]
                                    if key == "检索ID":
                                        key = "orderCheckId"
                                    saveData[key] = row_data[ki]
                                    # 保存用户信息
                                    if key in userList:
                                        userSave[key] = row_data[ki]

                                else:
                                    if row_data[ki] == "" or row_data[ki] == "-":
                                        continue
                                    attribute[title[ki]] = row_data[ki]

                            user = check_customer(userSave.get("carPhone"), userSave.get("carId"))
                            if not user:
                                # 没有此用户则添加
                                key = "userName,carPhone,carModel,carId,createdTime"
                                value = "'{}','{}','{}','{}','{}'".format(userSave.get("carUser"),
                                                                          userSave.get("carPhone"),
                                                                          userSave.get("carModel"),
                                                                          userSave.get("carId"), get_now())
                                try:
                                    # pass
                                    dbhelp.InsertData("User", key, value)
                                except:
                                    pass

                            saveData['attribute'] = json.dumps(attribute)
                            saveData['id'] = get_order_id()
                            dbhelp.add_sale_info(saveData)

                        # 清空缓存
                        temp = list()
                        # if i == nrows - 1:
                    # 此时是最后一组，则要进行录入

                    # else:
                    #     #合并了单元格则合并内容是空，将后面不是空的内容进行缓存，合并的内容会在最后一条信息中显示，此时一并进行录入
                    #     temp.append(row_data)
                except:
                    continue
            else:
                # 若不是用软件导出的EXCEL文档则

                # for i in range(2,nrows):
                # 先整理参数，全部变成列表，列表里面是字典，字典的key就是title
                try:
                    row_data = sh.row_values(i)
                    tempData = dict()

                    for k in range(len(title)):
                        tempData[title[k]] = row_data[k]
                    msgList.append(tempData)
                except:
                    continue

        if not matchs:
            saveList = defaultdict(list)
            for msg in msgList:
                if not msg.get("消费时间") or not msg.get("车牌号"):
                    continue

                key = msg.get("消费时间") + msg.get("车牌号")
                saveList[key].append(msg)

            # 插入信息
            must = ["订单号", "接待门店", "车牌号", "车主姓名", "联系电话", "车型", "操作人员", "消费项目", "消费时间"]
            for k, v in saveList.items():
                if progressDialog.wasCanceled():
                    break
                progressDialog.setValue(p)
                p += 1
                orderCheckId = get_order_id()
                # 对同一个订单进行录入
                userSave = {}
                for tempDict in v:
                    orderNo = str(tempDict.pop("订单号")) if tempDict.get("订单号", "") != "" else "-"
                    pcSign = tempDict.pop("接待门店", "") if tempDict.get("接待门店", "") != "" else "-"
                    carId = tempDict.pop("车牌号") if tempDict.get("车牌号") != "" else "-"
                    carUser = tempDict.pop("车主姓名", "") if tempDict.get("车主姓名", "") != "" else "-"
                    carPhone = str(tempDict.pop("联系电话", "-")).replace(".0", "") if tempDict.get("联系电话",
                                                                                                "") != "" else "-"
                    carModel = tempDict.pop("车型", "") if tempDict.get("车型", "") != "" else "-"
                    workerName = tempDict.pop("操作人员", "") if tempDict.get("操作人员", "") != "" else "-"
                    project = tempDict.pop("消费项目", "") if tempDict.get("消费项目", "") != "" else "-"
                    createdTime = str(tempDict.pop("消费时间")).replace(".", "-")
                    # 保存用户信息
                    userSave["carId"] = carId if carId != '-' else ""
                    userSave["carUser"] = carUser if carUser != '-' else ""
                    userSave["carPhone"] = (carPhone if carPhone != '-' else "").replace(".0", "")
                    userSave['carModel'] = carModel if carModel != '-' else ""

                    if orderNo != "-":
                        checkOrder = get_sale_info_by_one_key("orderNo", orderNo)
                        if checkOrder:
                            break

                    saveData = {
                        "orderNo": orderNo.replace(".0", ""),
                        "createdTime": createdTime,
                        "pcSign": pcSign,
                        "carId": carId,
                        "carUser": carUser,
                        "carPhone": carPhone,
                        "carModel": carModel,
                        "workerName": workerName,
                        "project": project,
                        "orderCheckId": orderCheckId,
                        "id": get_order_id(),
                    }
                    tempAttribute = tempDict

                    attribute = dict()
                    for k, v in tempAttribute.items():
                        if k not in must:
                            if v == "":
                                # v = '-'
                                continue
                            attribute[k] = str(v)
                    try:
                        gsf = float(attribute.get("工时费")) if attribute.get("工时费") != "" else 0
                        sl = float(attribute.get("数量")) if attribute.get("数量") != "" else 0
                        dj = float(attribute.get("单价")) if attribute.get("单价") != "" else 0
                        attribute["总价"] = gsf + sl * dj
                    except:
                        pass
                    saveData["attribute"] = json.dumps(attribute)
                    dbhelp.add_sale_info(saveData)

                if userSave.get("carId") and userSave.get("carPhone"):
                    # 当有用户信息的时候判断是否需要自动添加
                    user = check_customer(userSave.get("carPhone"), userSave.get("carId"))
                    if not user:
                        # 没有此用户则添加
                        key = "userName,carPhone,carModel,carId,createdTime"
                        value = "'{}','{}','{}','{}','{}'".format(userSave.get("carUser"), userSave.get("carPhone"),
                                                                  userSave.get("carModel"), userSave.get("carId"),
                                                                  get_now())
                        try:
                            # pass
                            dbhelp.InsertData("User", key, value)
                        except:
                            pass
        # 最后全部导入
        progressDialog.setValue(nrows - 3)
        progressDialog.close()


def ImportMenuExcel(fileName, mustSet):
    bk = xlrd.open_workbook(fileName)
    sh = bk.sheet_by_name("菜单列表")
    nrows = sh.nrows
    temp = defaultdict(list)
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        menu1 = row_data[0]
        menu2 = row_data[1]
        if menu1 not in temp:
            temp[menu1] = [menu2]
        else:
            temp[menu1].append(menu2)

    menu = dbhelp.getOneMenu()
    menuList = list()
    menuOneKey = dict()
    for data in menu:
        menuList.append(data[1])
        menuOneKey[data[1]] = data[0]
    key = "name,createdTime"
    now = datetime.now()
    attribute = ""
    attributeState = ""
    for t in mustSet:
        attribute += "{},".format(t)
        attributeState += "1,"

    attribute = attribute[:-1]
    attributeState = attributeState[:-1]
    for k in temp:
        if k not in menuList:
            value = "\'{}\',\'{}\'".format(k, now)
            menuId = dbhelp.InsertData("OneMenu", key, value)
            for menu2 in temp[k]:
                saveData = {
                    "father": menuId,
                    "name": menu2,
                    "attribute": attribute,
                    "attributeState": attributeState,
                    "createdTime": now
                }
                dbhelp.InsertTwoMenu(saveData)
        else:
            if menuOneKey.get(k):
                menuId = menuOneKey.get(k)
                for menu2 in temp[k]:
                    saveData = {
                        "father": menuId,
                        "name": menu2,
                        "attribute": attribute,
                        "attributeState": attributeState,
                        "createdTime": now
                    }
                    try:
                        dbhelp.InsertTwoMenu(saveData)
                    except:
                        pass


def Insert():
    return dbhelp.InsertData
