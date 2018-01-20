# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/10'
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
import codecs
import json
import logging
import time
import traceback
from datetime import timedelta
from socket import *

import tornado.ioloop
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import qApp

from common import config
from common.static_func import md5
from server.MySocket import ADDR, myClient, code, linkKey

logger = logging.getLogger(__name__)


def get_pc_mac():
    try:
        import uuid
        node = uuid.getnode()
        serial_number = uuid.UUID(int=node).hex[-12:]
    except Exception as e:
        logger.error(e.__str__())
        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
        serial_number = "读取失败"
    return serial_number.upper()


def compare_local_code_with_remote_register(remote_code):
    result = False
    pc_mac = get_pc_mac()
    if md5(pc_mac)[8:-8].upper() == remote_code:
        result = True
    return result


def format_time(time_str, today=False):
    time_list = time_str.split('/')
    # XP上的时间是以-分割的
    if len(time_list) < 3:
        time_list = time_str.split("-")
    # 有时候年份会在以后一个,如：03-25-2016，此时查询数据将出错，因此要判断一下
    if len(time_list[2]) == 4:
        mon = time_list[0]
        day = time_list[1]
        time_list[0] = time_list[2]
        time_list[1] = mon
        time_list[2] = day

    time_str = ""
    for t in time_list:
        if len(t) < 2:
            t = "0" + t
        time_str += t + "-"
    time_str = time_str[:-1]
    if today:
        time_str += " 23:59:59"
    else:
        time_str += " 00:00:00"
    return time_str


# 获取本周信息
def week_get(vdate):
    dayscount = timedelta(days=vdate.isoweekday())
    dayfrom = vdate - dayscount + timedelta(days=1)
    dayto = vdate - dayscount + timedelta(days=7)
    week7 = []
    i = 0
    while (i <= 6):
        week7.append(str(dayfrom + timedelta(days=i)))
        i += 1
    return week7


def SocketServer(keyWord):
    client = socket(AF_INET, SOCK_STREAM)
    client.settimeout(60)
    client.connect(ADDR)
    client.send(keyWord.encode())
    try:
        # if True:
        config.heartbeatCheck = False
        file_size = client.recv(1024).decode()
        file_size = int(file_size)
        time.sleep(1)
        BUFFER_SIZE = 1024
        jsonData = ''
        recv_size = 0
        while (recv_size < file_size):

            if (file_size - recv_size < BUFFER_SIZE):
                file_data = client.recv(file_size - recv_size)

            else:
                file_data = client.recv(BUFFER_SIZE)

            if file_data != b"heartbeat heartbeat":
                tempSize = len(file_data.decode())
                jsonData += file_data.decode()
                recv_size += tempSize

        # jsonData = client.recv(size).decode()
        data = json.loads(jsonData)
        client.close()

    except Exception as e:
        logger.error(e.__str__())
        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
        data = []
    return data


def ClientClose():
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(ADDR)
        client.send("close {} {}".format(code, linkKey).encode())
    except Exception as e1:
        logger.error(e1.__str__())
        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
        pass
    try:
        myClient.close()
    except Exception as e2:
        logger.error(e2.__str__())
        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
        pass
    try:
        config.scheduler.shutdown()
    except Exception as e3:
        logger.error(e3.__str__())
        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
        pass
    tornado.ioloop.IOLoop.instance().stop()


import warnings

from decimal import Decimal


def cncurrency(value, capital=True, prefix=False, classical=True):
    '''

    人民币数字转汉字表示 Ver 0.02

    参数:

    capital:    True   大写汉字金额

                False  一般汉字金额

    classical:  True   圆

                False  元

    prefix:     True   以'人民币'开头

                False, 无开头

    '''

    if not isinstance(value, (Decimal, str, int)):
        msg = '''

        由于浮点数精度问题，请使用考虑使用字符串，或者 decimal.Decimal 类。

        因使用浮点数造成误差而带来的可能风险和损失作者概不负责。

        '''

        warnings.warn(msg, UserWarning)

    # 默认大写金额用圆，一般汉字金额用元

    if classical is None:
        classical = True if capital else False

    # 汉字金额前缀

    if prefix is True:

        prefix = '人民币'

    else:

        prefix = ''

    # 汉字金额字符定义

    dunit = ('角', '分')

    if capital:

        num = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')

        iunit = [None, '拾', '佰', '仟', '万', '拾', '佰', '仟',

                 '亿', '拾', '佰', '仟', '万', '拾', '佰', '仟']

    else:

        num = ('〇', '一', '二', '三', '四', '五', '六', '七', '八', '九')

        iunit = [None, '十', '百', '千', '万', '十', '百', '千',

                 '亿', '十', '百', '千', '万', '十', '百', '千']

    if classical:
        iunit[0] = '元' if classical else '元'

    # 转换为Decimal，并截断多余小数

    if not isinstance(value, Decimal):
        value = Decimal(value).quantize(Decimal('0.01'))

    # 处理负数

    if value < 0:
        prefix += '负'  # 输出前缀，加负

        value = - value  # 取正数部分，无须过多考虑正负数舍入

        # assert - value + value == 0

    # 转化为字符串

    s = str(value)

    if len(s) > 19:
        raise ValueError('金额太大了，不知道该怎么表达。')

    istr, dstr = s.split('.')  # 小数部分和整数部分分别处理

    istr = istr[::-1]  # 翻转整数部分字符串

    so = []  # 用于记录转换结果

    # 零

    if value == 0:
        return prefix + num[0] + iunit[0]

    haszero = False  # 用于标记零的使用

    if dstr == '00':
        haszero = True  # 如果无小数部分，则标记加过零，避免出现“圆零整”

    # 处理小数部分

    # 分

    if dstr[1] != '0':

        so.append(dunit[1])

        so.append(num[int(dstr[1])])

    else:

        so.append('整')  # 无分，则加“整”

    # 角

    if dstr[0] != '0':

        so.append(dunit[0])

        so.append(num[int(dstr[0])])

    elif dstr[1] != '0':

        so.append(num[0])  # 无角有分，添加“零”

        haszero = True  # 标记加过零了

    # 无整数部分

    if istr == '0':

        if haszero:  # 既然无整数部分，那么去掉角位置上的零

            so.pop()

        so.append(prefix)  # 加前缀

        so.reverse()  # 翻转

        return ''.join(so)

    # 处理整数部分

    for i, n in enumerate(istr):

        n = int(n)

        if i % 4 == 0:  # 在圆、万、亿等位上，即使是零，也必须有单位

            if i == 8 and so[-1] == iunit[4]:  # 亿和万之间全部为零的情况

                so.pop()  # 去掉万

            so.append(iunit[i])

            if n == 0:  # 处理这些位上为零的情况

                if not haszero:  # 如果以前没有加过零

                    so.insert(-1, num[0])  # 则在单位后面加零

                    haszero = True  # 标记加过零了

            else:  # 处理不为零的情况

                so.append(num[n])

                haszero = False  # 重新开始标记加零的情况

        else:  # 在其他位置上

            if n != 0:  # 不为零的情况

                so.append(iunit[i])

                so.append(num[n])

                haszero = False  # 重新开始标记加零的情况

            else:  # 处理为零的情况

                if not haszero:  # 如果以前没有加过零

                    so.append(num[0])

                    haszero = True

    # 最终结果

    so.append(prefix)

    so.reverse()

    return ''.join(so)


def skin_change(qss_file_name):
    qss_file = QFile(qss_file_name)
    qss_file.open(QFile.ReadOnly)

    # 转换成UTF-8编码格式
    style_file = codecs.decode(qss_file.readAll(), 'utf-8')
    qApp.setStyleSheet(style_file)

    qss_file.close()
