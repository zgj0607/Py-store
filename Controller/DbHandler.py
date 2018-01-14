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

from Common.time_utils import format_time
from database.db_connection import execute


class DB_Handler():
    # 获取消费列表
    def GetXiaoFeiTable(self, startTime, endTime, YeJi=False, Table=True):
        today = False
        if startTime == endTime or YeJi == True:
            today = True
        startTime = format_time(startTime)
        endTime = format_time(endTime, True)
        if Table:
            sqlStr = '''SELECT orderNo,
                               createdTime,
                               pcSign,
                               carId,
                               carUser,
                               carPhone,
                               carModel,
                               workerName,
                               project,
                               attribute,
                               orderCheckId,
                               id
                          FROM Sales
                         WHERE createdTime BETWEEN \'{}\' and \'{}\'
                         ORDER BY createdTime DESC ''' \
                .format(startTime, endTime)
        else:
            sqlStr = '''SELECT orderCheckId,
                               orderNo,
                               createdTime,
                               pcSign,
                               carId,
                               carUser,
                               carPhone,
                               carModel,
                               workerName,
                               project,
                               attribute
                          FROM Sales
                         WHERE createdTime BETWEEN \'{}\' and \'{}\'
                         ORDER BY createdTime DESC ''' \
                .format(startTime, endTime)
        data = execute(sqlStr)
        return data

    # 插入
    def InsertData(self, dbname, key, value):
        sqlStr = "INSERT INTO {} ({}) " \
                 "VALUES ({})".format(dbname, key, value)
        return execute(sqlStr)
