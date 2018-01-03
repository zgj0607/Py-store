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
import configparser
import hashlib
import json
import os
import re
from collections import OrderedDict
from collections import defaultdict
from datetime import datetime

import requests
import xlrd
import xlwt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import *

from Common.Common import SocketServer, cncurrency, format_time
from Common.StaticFunc import GetOrderId
from Common.time_utils import get_now
from Common.config import domain, savePath, menuSavePath, connect as myconnect
from Controller import DbHandler

dbhelp = DbHandler.DB_Handler()
selectOrderNo = None


def GetTwoMenu(id):
    data = dbhelp.GetOneById("TwoMenu", id)
    if data:
        return data
    else:
        return []


def GetOneMenu(id):
    data = dbhelp.GetOneById("OneMenu", id)
    if data:
        return data
    else:
        return []


def RemoveById(id, dbname):
    search = "id={}".format(id)
    dbhelp.DeleteData(dbname, search)


def UpdateById(id, dbname, updateData):
    search = "id={}".format(id)
    dbhelp.UpdateData(dbname, updateData, search)


# 获取表单选中行的信息
def GetTableMsg(table, num):
    row = table.currentIndex().row()
    model = table.model()
    index = model.index(row, num)
    return model.data(index)


# 获取表单中某单元格的信息
def GetCellMsg(table, row, num):
    model = table.model()
    index = model.index(row, num)
    return model.data(index)


def UpdatePwd(newPwd, oldPwd):
    oldPwd += "udontknowwhy"
    m = hashlib.md5()
    m.update(oldPwd.encode())
    oldPwd = m.hexdigest()
    data = dbhelp.GetAdminByUsername("admin")
    pwd = data[1]
    if oldPwd != pwd:
        return False
    newPwd = newPwd + "udontknowwhy"
    m = hashlib.md5()
    m.update(newPwd.encode())
    newPwd = m.hexdigest()
    search = "id={}".format(data[0])
    updateData = "pwd=\'{}\'".format(newPwd)
    dbhelp.UpdateData("Admin", updateData, search)
    return True


def UpdatePcName(pcSign, pcAddress, pcPhone, code):
    url = domain + 'store/api/update'
    data = {
        "pcAddress": pcAddress,
        "pcSign": pcSign,
        "pcPhone": pcPhone,
        "code": code
    }
    req = requests.post(url, data=data)
    req = json.loads(req.text)
    if req.get("code") == 200:
        return True
    else:
        return False


def set_style(name, height, bold=False, center=False, upDown=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    alignment = xlwt.Alignment()
    # 左右居中
    if center:
        alignment.horz = xlwt.Alignment.HORZ_CENTER
    # 上下居中
    if upDown:
        alignment.vert = xlwt.Alignment.VERT_CENTER

    style.alignment = alignment
    return style


def CreateXls(startTime, endTime, remote=False):
    returnStr = True
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    fileName = now + ".xls"
    # 设置内容标题
    # titleList = ['订单号',u'消费时间','消费门店',u"车牌号",u"车主姓名",u"联系电话",u"车型",u"操作人员",
    #              u"消费项目",u"品牌",u"型号",u"花纹",u"数量",u"单价",u"小计",u"工时费",
    #              u"更换里程",u"备注",u"总价"]
    # tableLen = len(titleList)

    # 获取消费信息
    xiaoFei = []
    if remote:
        # 获取远程信息
        root = 'config.ini'
        basicMsg = configparser.ConfigParser()
        basicMsg.read(root)
        code = basicMsg.get('msg', 'code')
        keyWord = "xiaofei {} {} {}".format(code, startTime, endTime)
        # python3传递的是bytes，所以要编码
        try:
            xiaoFei = SocketServer(keyWord)
        except:
            returnStr = False
    else:
        xiaoFei = dbhelp.GetXiaoFeiTable(startTime, endTime, Table=False)

    # 填入数据
    if xiaoFei:
        # 插入信息
        xiaoFei.sort(key=lambda obj: obj[2], reverse=True)
        orderCheckId = None
        hebing = list()
        tempMsg = dict()
        temp = list()
        # 设置表头
        titleList = ["检索ID", '订单号', u'消费时间', "消费门店", u"车牌号", u"车主姓名", u"联系电话", u"车型", u"操作人员",
                     u"消费项目"]

        tableLen = len(titleList)
        hearder = ['数量', '单价', '小计', '总价', '单位', '备注']
        for data in xiaoFei:
            try:
                attribute = json.loads(data[10])
                for k, v in attribute.items():
                    if k not in hearder:
                        hearder.append(k)
            except:
                continue
        titleList = titleList + hearder
        allTableLen = len(titleList)

        wb = xlwt.Workbook()
        ws = wb.add_sheet('消费列表', cell_overwrite_ok=True)
        title = set_style('Arial', 250, True, True)
        default = set_style('SimSun', 180, True, True, True)
        top = set_style('Times New Roman', 350, True, True)
        # 前两个参数表示需要合并的行范围，后两个参数表示需要合并的列范围
        # 合并单元格作为大标题，水平居中即可
        startTime = format_time(startTime)[:10]
        endTime = format_time(endTime)[:10]
        ws.write_merge(0, 0, 0, allTableLen - 1, '门店系统:{}至{}'.format(startTime, endTime), top)

        # 设置标题
        for i in range(allTableLen):
            # 设置单元格宽度
            ws.col(i).width = 265 * 20
            # 插入标题
            ws.write(1, i, titleList[i], title)

        # 从第二行开始插
        row = 2

        for data in xiaoFei:
            if orderCheckId:
                # 如果记录的订单号与当前数据的订单号不同，则进行录入并修改记录订单号
                if orderCheckId != data[0]:
                    orderCheckId = data[0]

                    # 因为订单号变了所以之前的缓存清空，换成这个订单号的索引
                    temp = [row]
                else:
                    # 若已经缓存了2个索引则代表此订单号有>2个商品，所以更新第二个索引保留第一个索引
                    if len(temp) >= 2:
                        temp[1] = row
                    else:
                        temp.append(row)
            else:
                # 若第一次进来，此时订单号是None，进行录入
                orderCheckId = data[0]
                temp.append(row)

            # 插入信息
            for j in range(tableLen):
                ws.write(row, j, data[j], default)
                if j == tableLen - 1:
                    # 最后一个的时候遍历填入数据
                    try:
                        j += 1
                        attribute = json.loads(data[j])
                        for k in hearder:
                            ws.write(row, j, attribute.get(k, ""), default)
                            j += 1
                    except:
                        continue
            row += 1
            # 如果已经缓存了2个数字，则代表有重复的订单号，所以此时进行记录并合并
            if len(temp) >= 2:
                tempMsg[temp[0]] = MakeTempMsg(data)
                hebing.append(temp)

        if len(temp) >= 2:
            hebing.append(temp)
            tempMsg[temp[0]] = MakeTempMsg(data)
        for hb in hebing:
            ws.write_merge(hb[0], hb[1], 0, 0, tempMsg[hb[0]].get("checkOrderId"), default)
            ws.write_merge(hb[0], hb[1], 1, 1, tempMsg[hb[0]].get("orderNo"), default)
            ws.write_merge(hb[0], hb[1], 2, 2, tempMsg[hb[0]].get("createdTime"), default)
            ws.write_merge(hb[0], hb[1], 3, 3, tempMsg[hb[0]].get("pcSign"), default)
            ws.write_merge(hb[0], hb[1], 4, 4, tempMsg[hb[0]].get("carId"), default)
            ws.write_merge(hb[0], hb[1], 5, 5, tempMsg[hb[0]].get("carUser"), default)
            ws.write_merge(hb[0], hb[1], 6, 6, tempMsg[hb[0]].get("carPhone"), default)
            ws.write_merge(hb[0], hb[1], 7, 7, tempMsg[hb[0]].get("carModel"), default)
            ws.write_merge(hb[0], hb[1], 8, 8, tempMsg[hb[0]].get("workerName"), default)

        if not os.path.exists(savePath):
            os.mkdir(savePath)
        wb.save(savePath + fileName)

        return fileName
    else:
        return False


def CreateMenuExcel():
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    fileName = now + ".xls"
    titleList = ["一级菜单", "二级菜单"]
    allTableLen = len(titleList)

    # 整理参数
    menu1s = dbhelp.getOneMenu()
    menu2s = defaultdict(list)
    for menu in menu1s:
        menu2s[menu[0]] = dbhelp.getTwoMenu(menu[0])
    if menu1s and menu2s:
        wb = xlwt.Workbook()
        ws = wb.add_sheet('菜单列表', cell_overwrite_ok=True)

        for i in range(allTableLen):
            # 设置单元格宽度
            ws.col(i).width = 265 * 20
            # 插入标题
            ws.write(0, i, titleList[i], set_style('Arial', 250, True, True))

        row = 1
        for menu in menu1s:
            menu2 = menu2s[menu[0]]
            for data in menu2:
                # 插入信息
                ws.write(row, 0, menu[1], set_style('SimSun', 180, True, True, True))
                ws.write(row, 1, data[1], set_style('SimSun', 180, True, True, True))
                row += 1

        if not os.path.exists(menuSavePath):
            os.mkdir(menuSavePath)
        wb.save(menuSavePath + fileName)
        return fileName
    else:
        return False


def MakeTempMsg(data):
    tempMsg = {
        "checkOrderId": data[0],
        "orderNo": data[1],
        "createdTime": data[2],
        "pcSign": data[3],
        "carId": data[4],
        "carUser": data[5],
        "carPhone": data[6],
        "carModel": data[7],
        "workerName": data[8],
    }
    return tempMsg


def DoPrinter(mainWin, orderNo):
    try:
        printer = QPrinter(QPrinter.HighResolution)
        # /* 打印预览 */
        preview = QPrintPreviewDialog(printer, mainWin)
        preview.paintRequested.connect(printHtml)
        global selectOrderNo
        selectOrderNo = orderNo
        preview.exec_()
        return True

    except:
        return False


def printHtml(printer):
    root = 'config.ini'
    basicMsg = configparser.ConfigParser()
    basicMsg.read(root)
    try:
        if not myconnect:
            raise
        code = basicMsg.get("msg", 'code')
        url = domain + "store/api/detail?code={}".format(code)
        req = requests.get(url=url)
        resultData = json.loads(req.text)
    except:

        fp = open("pc.conf", 'rb')
        pcData = fp.readline().decode()
        fp.close()
        pcData = pcData.split(',')

        if len(pcData) < 4:
            pcData = [pcData[0], "", "", ""]

        resultData = {
            'data': {
                "pcId": pcData[0],
                "pcPhone": pcData[1],
                "pcAddress": pcData[2],
                "pcSign": pcData[3],
            },
            'code': 200
        }
    mustSet = ['数量', '单价', '小计', '总价', '单位', '备注']

    if resultData.get("code") != 200:
        storeName = ""
        pcAddress = ""
        pcPhone = ""
    else:
        storeName = resultData.get("data").get("pcSign", "")
        pcAddress = resultData.get("data").get("pcAddress", "")
        pcPhone = resultData.get("data").get("pcPhone", "")
    result = dbhelp.GetXiaoFeiByKey("orderCheckId", selectOrderNo)

    fp = open("printer.txt", 'rb')
    data = fp.readline().decode().replace("\n", "").replace("\r", "").replace("\ufeff", "")
    fp.close()
    fontSize = 7
    if data:
        try:
            fontSize = int(data)
        except:
            fontSize = 7

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

        """ + "*{font-size:" + str(fontSize) + "pt;}" + ".bigWord{font-size:" + str(
            fontSize * 1.5) + "pt;}" + "</style><head></head>"
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
                        checkOrder = dbhelp.GetXiaoFeiByKey("orderCheckId", orderCheckId)
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
                                        saveData['id'] = GetOrderId()
                                        dbhelp.InsertXiaoFei(saveData)

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

                            user = dbhelp.CheckUser(userSave.get("carPhone"), userSave.get("carId"))
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
                            saveData['id'] = GetOrderId()
                            dbhelp.InsertXiaoFei(saveData)

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
                orderCheckId = GetOrderId()
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
                        checkOrder = dbhelp.GetXiaoFeiByKey("orderNo", orderNo)
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
                        "id": GetOrderId(),
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
                    dbhelp.InsertXiaoFei(saveData)

                if userSave.get("carId") and userSave.get("carPhone"):
                    # 当有用户信息的时候判断是否需要自动添加
                    user = dbhelp.CheckUser(userSave.get("carPhone"), userSave.get("carId"))
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
