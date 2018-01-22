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
import json
import logging
import traceback

from PyQt5 import QtCore, QtGui

from common.common import SocketServer
from common.config import get_store_id
from controller import DbHandler

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
dbhelp = DbHandler.DB_Handler()

logger = logging.getLogger(__name__)


def xiaofeiTableSet(table, start_time, end_time, remote=False):
    # 添加表头：
    model = QtGui.QStandardItemModel()
    return_str = True

    # 获取消费信息
    if remote:
        # 获取远程信息
        try:
            store_id = get_store_id()
        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            return False

        keyword = "xiaofei {} {} {}".format(store_id, start_time, end_time)

        # python3传递的是bytes，所以要编码
        try:
            xiaoFei = SocketServer(keyword)
        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            return False
    else:
        xiaoFei = dbhelp.GetXiaoFeiTable(start_time, end_time)

    if xiaoFei == 'restart':
        return xiaoFei
    if xiaoFei:
        xiaoFei.sort(key=lambda obj: obj[1], reverse=True)
        # 设置表头
        title_list = ["ID", '订单号', u'消费时间', "消费门店", u"车牌号", u"车主姓名", u"联系电话", u"车型", u"操作人员",
                      u"消费项目"]

        table_len = len(title_list)
        header = ['数量', '单价', '小计', '总价', '单位', '备注']
        for data in xiaoFei:
            try:
                attribute = json.loads(data[9])
                for k, v in attribute.items():
                    if k not in header:
                        header.append(k)
            except Exception as e:
                logger.error(e.__str__())
                logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                continue
        title_list = title_list + header + ['操作']
        all_table_len = len(title_list)
        # 设置表格属性：
        model.setColumnCount(all_table_len)
        for i in range(all_table_len):
            model.setHeaderData(i, QtCore.Qt.Horizontal, _fromUtf8(title_list[i]))
            table.setColumnWidth(i, 120)
        table.setModel(model)

        # 插入信息
        i = 0
        order_check_id = None
        hebing = list()
        temp = list()
        for data in xiaoFei:
            if order_check_id:
                # 如果记录的订单号与当前数据的订单号不同，则进行录入并修改记录订单号
                if order_check_id != data[10]:
                    order_check_id = data[10]
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
                order_check_id = data[10]
                temp.append(i)

            lastj = 0
            for j in range(table_len):
                if j == 0:
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[10]))))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(data[j - 1]))))
                if j == table_len - 1:
                    # model.setItem(i,j,QtGui.QStandardItem(_fromUtf8(str(data[10]))))
                    # 最后一个的时候遍历填入数据
                    try:
                        j += 1
                        attribute = json.loads(data[9])
                        for k in header:
                            model.setItem(i, j, QtGui.QStandardItem(_fromUtf8(str(attribute.get(k, "")))))
                            j += 1
                        lastj = j
                    except Exception as e:
                        logger.error(e.__str__())
                        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                        continue
            model.setItem(i, lastj, QtGui.QStandardItem(_fromUtf8("打印单据")))
            model.item(i, 0).setForeground(QtGui.QBrush(QtGui.QColor(70, 70, 70)))
            i += 1

        if len(temp) >= 2:
            hebing.append(temp)

        for hb in hebing:
            num = hb[1] - hb[0] + 1
            table.setSpan(hb[0], 0, num, 1)
            table.setSpan(hb[0], 1, num, 1)
            table.setSpan(hb[0], 2, num, 1)
            table.setSpan(hb[0], 3, num, 1)
            table.setSpan(hb[0], 4, num, 1)
            table.setSpan(hb[0], 5, num, 1)
            table.setSpan(hb[0], 6, num, 1)
            table.setSpan(hb[0], 7, num, 1)
            table.setSpan(hb[0], all_table_len - 1, num, 1)

    else:
        if return_str:
            return_str = None

    table.setModel(model)
    return return_str
