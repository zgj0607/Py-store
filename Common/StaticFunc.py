# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '12/11/2016'

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
import hashlib
import random
import uuid

import xlwt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QLineEdit


class ErrorCode:
    QueryLangFormatError = 1000  # 接口查询语言语法出错
    NoneData = 1002  # 没有数据
    DataUnSave = 1003  # 数据无法保存
    JsonError = 1004  # 接收的JSON格式出错
    TokenSessionError = 1005  # TokenSession失效
    MethodError = 1006  # 错误的请求方式
    PrinterError = 1007  # 打印出错

    ParameterError = 1100  # 参数错误
    ParameterMiss = 1101  # 参数缺失
    ErrorRequest = 1102  # 错误的请求

    UserError = 1200  # 无此用户
    UserPasswordError = 1201  # 密码错误
    UserMore = 1202  # 已有此用户
    UserStateError = 1204  # 用户被禁用
    UserStateWaitError = 1206  # 用户待审核
    UsernameError = 1205  # 没有填写用户名

    CodeError = 1300  # 注册码输入错误
    PCError = 1301  # PC码出错

    ErrorFindCode = 2000  # 未识别错误码

    ReStartPC = 1602  # 微信下订单失败

    ERROR_MESSAGE = {
        QueryLangFormatError: {'forWorker': u"查询语言语法出错,请检查语法",
                               'forUser': u"查询语言语法出错,请检查语法"},
        NoneData: {'forWorker': u"没有数据",
                   'forUser': u"没有数据"},
        DataUnSave: {'forWorker': u"数据无法保存",
                     'forUser': u"数据无法保存"},
        JsonError: {'forWorker': u"接收的JSON格式出错",
                    'forUser': u"请求错误"},
        TokenSessionError: {'forWorker': u"TokenSession失效",
                            'forUser': u"请求错误"},
        MethodError: {'forWorker': u"请求方式出错",
                      'forUser': u"请求错误"},

        UserError: {'forWorker': u'无此用户',
                    'forUser': u"无此用户"},
        UserMore: {'forWorker': u"已有此用户",
                   'forUser': u"已有此用户"},
        UserPasswordError: {'forWorker': u"密码错误",
                            'forUser': u"密码错误"},

        UserStateError: {'forWorker': u"该用户在后台被禁用",
                         'forUser': u"您的设备已被禁用"},

        UserStateWaitError: {'forWorker': u"该用户待审核",
                             'forUser': u"您的设备正在进行审核，请耐心等候。"},

        ParameterError: {'forWorker': u"不合法的参数",
                         'forUser': u"请求错误"},
        ParameterMiss: {'forWorker': u"参数缺失",
                        'forUser': u"请输入完整后提交"},
        ErrorRequest: {'forWorker': u"请求错误",
                       'forUser': u"请求错误"},

        ErrorFindCode: {'forWorker': u"未识别错误码",
                        'forUser': u"请求错误"},

        UsernameError: {'forWorker': u"请输入姓名",
                        'forUser': u"请输入姓名"},

        ReStartPC: {'forWorker': u"服务器重启，所以socket长链接断开",
                    'forUser': u"请重启电脑终端"},

        CodeError: {'forWorker': u"注册码输入有误",
                    'forUser': u"注册码输入有误"},

        PCError: {'forWorker': u"PC码文件（pc.conf）被删",
                  'forUser': u"您删除了部分有效文件，导致请求失效"},

        PrinterError: {'forWorker': u"打印出错",
                       'forUser': u"打印失败"},
    }


# 设置返回值
# forUser是显示给用户看的文字，forWorker是显示提供给后台程序员看的字段
# ret代表成功或者失败，data代表返回值，result代表错误代码
def Set_return_dicts(data=None, forUser='', code=200, ret=True, forWorker=''):
    if data == None:
        ret = False
        # logger.error('API: FORUSER:{}  CODE:{}  FORWORKER:{} '.format(forUser.encode(),code,forWorker.encode()))
        # logger.error('API:CODE:{}'.format(code))

    return_dicts = {
        'data': data,
        'forUser': forUser,
        'code': code,
        'ret': ret,
        'version': '1.0',
        'forWorker': forWorker
    }
    return return_dicts


# 生成订单号：日期+当日订单序号+随机数
def GetOrderId():
    return str(uuid.uuid1()).replace("-", '')


# 生成随机数
def GetDiscountCode(count=10):
    l1 = [chr(i) for i in range(97, 123)]
    l2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lists = l1 + l2
    slice = ''.join(random.sample(lists, count))
    return slice


# md5加密
def md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


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


def set_validator(edit: QLineEdit, type: str):
    validator = None
    if type == 'int':
        validator = QIntValidator()
    elif type == 'float':
        validator = QDoubleValidator()
    edit.setValidator(validator)
