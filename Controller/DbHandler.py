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
from datetime import datetime

from Common import Common
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
            sqlStr = 'SELECT orderNo,createdTime,pcSign,carId,carUser,carPhone,carModel,workerName,project,attribute,orderCheckId' \
                     ' FROM Sales WHERE createdTime BETWEEN \'{}\' and \'{}\' ORDER BY createdTime DESC '.format(
                startTime, endTime)
        else:
            sqlStr = 'SELECT orderCheckId,orderNo,createdTime,pcSign,carId,carUser,carPhone,carModel,workerName,project,attribute' \
                     ' FROM Sales WHERE createdTime BETWEEN \'{}\' and \'{}\' ORDER BY createdTime DESC '.format(
                startTime, endTime)
        data = execute(sqlStr)
        return data

    # 插入消费信息
    def InsertXiaoFei(self, saveData):
        sqlStr = "INSERT INTO Sales (id,orderNo,carId,pcId,workerId,userId," \
                 "workerName,code,carUser,attribute,pcSign," \
                 "carPhone,carModel,project,createdTime,orderCheckId) " \
                 "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            saveData.get('id'), saveData.get('orderNo', ""), saveData.get('carId', ""), saveData.get('pcId', ""),
            saveData.get('workerId', ""), saveData.get('userId', ""), saveData.get('workerName', ""),
            saveData.get('code', ""),
            saveData.get('carUser', ""), saveData.get('attribute', ""), saveData.get('pcSign', ""),
            saveData.get('carPhone', ""),
            saveData.get('carModel', ""), saveData.get('project', ""), saveData.get('createdTime', ""),
            saveData.get('orderCheckId', "")
        )
        execute(sqlStr)

    # 获取门店服务器二级菜单
    def getTwoMenu(self, father):
        sqlStr = 'SELECT id,name,attribute,attributeState FROM service WHERE father=\'{}\'ORDER BY createdTime DESC '.format(
            father)

        data = execute(sqlStr)
        return data

    # 插入二级菜单
    def InsertTwoMenu(self, saveData):
        sqlStr = "INSERT INTO service (name,father,attribute,attributeState,createdTime) " \
                 "VALUES ('{}','{}','{}','{}','{}')".format(saveData.get('name', ""),
                                                            saveData.get("father", ""), saveData.get("attribute", ""),
                                                            saveData.get("attributeState", ""),
                                                            saveData.get("createdTime", ""))
        execute(sqlStr)

    # 修改内容
    def UpdateData(self, dbname, updateData, search):
        sqlStr = "UPDATE {} SET {} WHERE {}".format(dbname, updateData, search)
        execute(sqlStr)


    # 插入
    def InsertData(self, dbname, key, value):
        sqlStr = "INSERT INTO {} ({}) " \
                 "VALUES ({})".format(dbname, key, value)
        return execute(sqlStr)


