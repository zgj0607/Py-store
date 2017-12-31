# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/14'
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
from datetime import datetime
from Controller import DbHandler
from Common.StaticFunc import md5

dbhelp = DbHandler.DB_Handler()


def AddAdmin(username, pwd):
    key = "username,pwd,createdTime"
    repwd = md5(pwd)
    value = "'{}','{}','{}'".format(username, repwd, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    dbhelp.InsertData("Admin", key, value)


def UpdateAdmin(id, pwd):
    repwd = md5(pwd)
    search = "id={}".format(id)
    updateData = "pwd=\'{}\'".format(repwd)
    dbhelp.UpdateData("Admin", updateData, search)
