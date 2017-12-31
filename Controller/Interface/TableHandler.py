# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/22/2016'

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
from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import DbHandler
from Common.Common import week_get, SocketServer, GetStoreId
import calendar
from datetime import datetime
from collections import defaultdict
import traceback
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
dbhelp = DbHandler.DB_Handler()


def xiaofeiTableSet(tableView, startTime, endTime, remote=False):
    # 添加表头：
    model = QtGui.QStandardItemModel()
    returnStr = True

    # 获取消费信息
    if remote:
        # 获取远程信息
        try:
            storeId = GetStoreId()
        except Exception as e:
            print(e)
            print('traceback.print_exc():{}'.format(traceback.print_exc()))
            print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            return False

        keyWord = "xiaofei {} {} {}".format(storeId, startTime, endTime)

        # python3传递的是bytes，所以要编码
        try:
            xiaoFei = SocketServer(keyWord)
        except Exception as e:
            print(e)
            print('traceback.print_exc():{}'.format(traceback.print_exc()))
            print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            return False
    else:
        xiaoFei = dbhelp.GetXiaoFeiTable(startTime, endTime)

    if xiaoFei == 'restart':
        return xiaoFei
    if xiaoFei:
        xiaoFei.sort(key=lambda obj: obj[1], reverse=True)
        # 设置表头
        titleList = ["ID", '订单号', u'消费时间', "消费门店", u"车牌号", u"车主姓名", u"联系电话", u"车型", u"操作人员",
                     u"消费项目"]

        tableLen = len(titleList)
        hearder = ['数量', '单价', '小计', '总价', '单位', '备注']
        for data in xiaoFei:
            try:
                attribute = json.loads(data[9])
                for k, v in attribute.items():
                    if k not in hearder:
                        hearder.append(k)
            except:
                continue
        titleList = titleList + hearder + ['操作']
        allTableLen = len(titleList)
        # 设置表格属性：
        model.setColumnCount(allTableLen)
        for i in range(allTableLen):
            model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))
            tableView.setColumnWidth(i, 120)
        tableView.setModel(model)

        # 插入信息
        i = 0
        orderCheckId = None
        hebing = list()
        temp = list()
        for data in xiaoFei:
            if orderCheckId:
                # 如果记录的订单号与当前数据的订单号不同，则进行录入并修改记录订单号
                if orderCheckId != data[10]:
                    orderCheckId = data[10]
                    # 如果已经缓存了2个数字，则代表有重复的订单号，所以此时进行记录并合并
                    if len(temp) >= 2:
                        hebing.append(temp)
                    # 因为订单号变了所以之前的缓存清空，换成这个订单号的索引
                    temp = [i]
                else:
                    # 若已经记录了2个索引则代表此订单号有>2个商品，所以更新第二个索引保留第一个索引
                    if len(temp) >= 2:
                        temp[1] = i
                    else:
                        temp.append(i)
            else:
                # 若第一次进来，此时订单号是None，进行录入
                # hebing.append(i)
                orderCheckId = data[10]
                temp.append(i)

            lastj = 0
            for j in range(tableLen):
                if j == 0:
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[10]))))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j - 1]))))
                if j == tableLen - 1:
                    # model.setItem(i,j,QtGui.QStandardItem(_fromUtf8(str(data[10]))))
                    # 最后一个的时候遍历填入数据
                    try:
                        j += 1
                        attribute = json.loads(data[9])
                        for k in hearder:
                            model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(attribute.get(k, "")))))
                            j += 1
                        lastj = j
                    except:
                        continue
            model.setItem(i, lastj, QtGui.QStandardItem(_fromUtf8("打印单据")))
            model.item(i, 0).setForeground(QtGui.QBrush(QtGui.QColor(70, 70, 70)))
            i += 1

        if len(temp) >= 2:
            hebing.append(temp)

        for hb in hebing:
            num = hb[1] - hb[0] + 1
            tableView.setSpan(hb[0], 0, num, 1)
            tableView.setSpan(hb[0], 1, num, 1)
            tableView.setSpan(hb[0], 2, num, 1)
            tableView.setSpan(hb[0], 3, num, 1)
            tableView.setSpan(hb[0], 4, num, 1)
            tableView.setSpan(hb[0], 5, num, 1)
            tableView.setSpan(hb[0], 6, num, 1)
            tableView.setSpan(hb[0], 7, num, 1)
            tableView.setSpan(hb[0], allTableLen - 1, num, 1)

    else:
        if returnStr:
            returnStr = None

    tableView.setModel(model)
    return returnStr


def MenuTableSet(tableView, level=None):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    if level == None:
        titleList = [u"ID", u'一级分类']
    else:
        titleList = [u"ID", u'二级分类']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))
    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    # 获取信息
    if level == None:
        menu = dbhelp.getOneMenu()
    else:
        menu = dbhelp.getTwoMenu(father=level)
    if menu:
        # 插入信息
        i = 0
        for data in menu:
            model.setItem(i, 0, QtGui.QStandardItem(_fromUtf8(str(data[0]))))
            model.setItem(i, 1, QtGui.QStandardItem(_fromUtf8(str(data[1]))))
            model.item(i, 0).setForeground(QtGui.QBrush(QtGui.QColor(70, 70, 70)))
            i += 1

    tableView.setModel(model)


def AttributeTableSet(tableView, nameList=None):
    # 添加表头：
    model = QtGui.QStandardItemModel()
    if nameList:
        # 插入信息
        i = 0
        for data in nameList:
            item = QtGui.QStandardItem(str(data))
            model.setItem(i, 0, item)
            model.item(i, 0).setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
            model.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            i += 1

    tableView.setModel(model)


def WorkerTableSet(tableView):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    titleList = ["ID", '姓名', '性别', '身份证号码']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    # 获取信息
    worker = dbhelp.GetWorker()

    if worker:
        # 插入信息
        i = 0
        for data in worker:
            for j in range(tableLen):
                model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j]))))
            i += 1
    tableView.setModel(model)


def AdminTableSet(tableView):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    titleList = ["ID", '用户名']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    # 获取信息
    worker = dbhelp.GetAdmin()

    if worker:
        # 插入信息
        i = 0
        for data in worker:
            for j in range(tableLen):
                model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j]))))
            i += 1
    tableView.setModel(model)


def YeJiTableSet(tableView, scope, jiaoyiPrice):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    titleList = ["一级分类", '二级分类', '成交单数', '成交金额']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if scope == 'year':
        # 查询年业绩
        startTime = '{}/{}/{}'.format(year, "01", "01")
        endTime = '{}/{}/{}'.format(year, "12", "31")

    elif scope == 'month':
        # 查询月业绩
        monthLast = calendar.monthrange(year, month)
        startTime = '{}/{}/{}'.format(year, month, "01")
        endTime = '{}/{}/{}'.format(year, month, monthLast[1])

    elif scope == 'today':
        # 查询本日业绩
        startTime = '{}/{}/{}'.format(year, month, day)
        endTime = '{}/{}/{}'.format(year, month, day)

    else:
        # 查询本周业绩
        # 获取本周信息
        weekList = week_get(now)
        startTime = weekList[0].replace("-", "/").split(" ")[0]
        endTime = weekList[-1].replace("-", "/").split(" ")[0]

    # 获取信息
    yeJi = dbhelp.GetXiaoFeiTable(startTime, endTime, True)
    resultList = list()
    oneMenuList = list()
    oneMenuDict = defaultdict(list)
    totalMoney = 0
    totalNum = 0
    if yeJi:
        # 插入信息
        for data in yeJi:
            try:
                oneMenu, twoMenu = data[8].split('-')
                if oneMenu == "":
                    oneMenu = "-"
                if twoMenu == "":
                    twoMenu = "--"

                if oneMenu == twoMenu:
                    twoMenu += "-"

                attribute = json.loads(data[9])
                zj = float(attribute.get("总价", 0))
                # 整理一级菜单信息
                if oneMenu not in oneMenuDict.keys():
                    # 如果没有存过该一级菜单
                    oneMenuList.append(oneMenu)
                    # 创建二级菜单
                    twoMenuDict = defaultdict(list)
                    twoMenuDict[twoMenu] = {
                        "name": twoMenu,
                        "num": 1,
                        "totalPrice": zj,
                    }
                    oneMenuDict[oneMenu] = {
                        "oneMenu": oneMenu,
                        "twoMenu": twoMenuDict
                    }
                    totalNum += 1
                    totalMoney += zj

                else:
                    twoMenuDict = oneMenuDict[oneMenu]['twoMenu']
                    # 判断二级菜单是否有被录入
                    if twoMenu not in twoMenuDict.keys():
                        # 若没有直接创建新的
                        temp = {
                            "name": twoMenu,
                            "num": 1,
                            "totalPrice": zj
                        }
                    else:
                        # 否则用旧的
                        temp = twoMenuDict[twoMenu]
                        temp["num"] += 1
                        temp["totalPrice"] += zj

                    twoMenuDict[twoMenu] = temp
                    oneMenuDict[twoMenu] = twoMenuDict
                    totalNum += 1
                    totalMoney += zj
            except:
                continue

        i = 0
        for name in oneMenuList:
            twoMenuTemp = list()
            if oneMenuDict.get(name):
                for k, v in oneMenuDict[name]["twoMenu"].items():
                    twoMenuTemp.append(v)
                resultList.append({
                    "oneMenu": name,
                    "twoMenu": twoMenuTemp
                })
                twoLen = len(twoMenuTemp)
                for two in twoMenuTemp:
                    model.setItem(i, 0, QtGui.QStandardItem(_fromUtf8(str(name))))
                    model.setItem(i, 1, QtGui.QStandardItem(_fromUtf8(str(two['name']))))
                    model.setItem(i, 2, QtGui.QStandardItem(_fromUtf8(str(two['num']))))
                    model.setItem(i, 3, QtGui.QStandardItem(_fromUtf8("￥" + str(two['totalPrice']))))
                    i += 1

                if twoLen > 1:
                    # 其参数为： 要改变单元格的   1行数  2列数     要合并的  3行数  4列数
                    tableView.setSpan(i - twoLen, 0, twoLen, 1)

    jiaoyiPrice.setText("总交易单数：{}单\n\n总交易金额：￥{}".format(totalNum, totalMoney))
    tableView.setModel(model)


def SheBeiTableSet(tableView):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    titleList = ["ID", '设备IP', '设备状态', '设备名称']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    # 获取信息
    shebei = dbhelp.GetSheBei()

    if shebei:
        # 插入信息
        i = 0
        for data in shebei:
            for j in range(tableLen):
                if j == 2:
                    state = "禁用中"
                    if data[j] == "1":
                        state = "启动中"
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(state))))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j]))))
            i += 1
    tableView.setModel(model)


def StoreTableSet(tableView, tableList):
    # 添加表头：
    model = QtGui.QStandardItemModel()
    # 设置表头
    titleList = ['门店标识', '联系方式', '门店地址']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 120)

    if tableList:
        # 插入信息
        i = 0
        for data in tableList:
            model.setItem(i, 0, QtGui.QStandardItem(_fromUtf8(str(data.get("pcSign", "")))))
            model.setItem(i, 1, QtGui.QStandardItem(_fromUtf8(str(data.get("pcPhone", "")))))
            model.setItem(i, 2, QtGui.QStandardItem(_fromUtf8(str(data.get("pcAddress", "")))))
            i += 1
    tableView.setModel(model)


def SheZhiTableSet(tableView, tableView2, tableDict):
    model = QtGui.QStandardItemModel()
    model2 = QtGui.QStandardItemModel()

    # 设置表格属性：
    model.setColumnCount(2)
    model2.setColumnCount(2)

    if True:
        # 插入信息

        pcName = QtGui.QStandardItem("设置PC标识")
        pcPhone = QtGui.QStandardItem("联系方式")
        pcAddress = QtGui.QStandardItem("设置地址")
        pcName.setFlags(QtCore.Qt.NoItemFlags)
        pcPhone.setFlags(QtCore.Qt.NoItemFlags)
        pcAddress.setFlags(QtCore.Qt.NoItemFlags)
        pcName.setTextAlignment(QtCore.Qt.AlignCenter)
        pcPhone.setTextAlignment(QtCore.Qt.AlignCenter)
        pcAddress.setTextAlignment(QtCore.Qt.AlignCenter)

        model.setItem(0, 0, pcName)
        model.setItem(1, 0, pcPhone)
        model.setItem(2, 0, pcAddress)
        pcSign = tableDict.get("pcSign", "")
        pcPhone = tableDict.get("pcPhone", "")
        pcAddress = tableDict.get("pcAddress", "")
        pcId = tableDict.get("pcId", "")
        if pcId:
            root = 'pc.conf'
            fp = open(root, 'wb')
            fp.write("{},{},{},{}".format(pcId, pcPhone, pcAddress, pcSign).encode())
            fp.close()
        model.setItem(0, 1, QtGui.QStandardItem(_fromUtf8(str(pcSign))))
        model.setItem(1, 1, QtGui.QStandardItem(_fromUtf8(str(pcPhone))))
        model.setItem(2, 1, QtGui.QStandardItem(_fromUtf8(str(pcAddress))))

        oldPwd = QtGui.QStandardItem("原密码")
        newPwd = QtGui.QStandardItem("新密码")
        newPwd2 = QtGui.QStandardItem("确认密码")
        oldPwd.setFlags(QtCore.Qt.NoItemFlags)
        newPwd.setFlags(QtCore.Qt.NoItemFlags)
        newPwd2.setFlags(QtCore.Qt.NoItemFlags)

        oldPwd.setTextAlignment(QtCore.Qt.AlignCenter)
        newPwd.setTextAlignment(QtCore.Qt.AlignCenter)
        newPwd2.setTextAlignment(QtCore.Qt.AlignCenter)
        model2.setItem(0, 0, oldPwd)
        model2.setItem(1, 0, newPwd)
        model2.setItem(2, 0, newPwd2)
        model2.setItem(0, 1, QtGui.QStandardItem(""))
        model2.setItem(1, 1, QtGui.QStandardItem(""))
        model2.setItem(2, 1, QtGui.QStandardItem(""))

    tableView.setModel(model)
    tableView2.setModel(model2)

    tableView.setRowHeight(0, 59)
    tableView.setRowHeight(1, 59)
    tableView.setRowHeight(2, 59)
    tableView2.setRowHeight(0, 59)
    tableView2.setRowHeight(1, 59)
    tableView2.setRowHeight(2, 59)


def CallBackSet(tableView):
    # 添加表头：
    model = QtGui.QStandardItemModel()

    # 设置表头
    titleList = ["ID", '回访用户', '车牌号', '联系方式', '回访时间']
    tableLen = len(titleList)
    # 设置表格属性：
    model.setColumnCount(tableLen)

    for i in range(tableLen):
        model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(titleList[i]))

    tableView.setModel(model)
    tableView.setColumnWidth(0, 200)

    # 获取信息
    callback = dbhelp.GetCallBack()

    if callback:
        # 插入信息
        i = 0
        for data in callback:
            for j in range(tableLen):
                model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j]))))
            i += 1
    tableView.setModel(model)
