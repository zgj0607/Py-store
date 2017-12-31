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
import sqlite3
from Common import Common
from datetime import datetime
from PyQt5 import QtWidgets
from View.userConnect import Ui_MainWindow_UserConnect
import Common.config as config


class DB_Handler():
    # 获取消费列表
    def GetXiaoFeiTable(self, startTime, endTime, YeJi=False, Table=True):
        self.conn = sqlite3.connect('MYDATA.db')
        today = False
        if startTime == endTime or YeJi == True:
            today = True
        startTime = Common.MakeTime(startTime)
        endTime = Common.MakeTime(endTime, True)
        if Table:
            sqlStr = 'SELECT orderNo,createdTime,pcSign,carId,carUser,carPhone,carModel,workerName,project,attribute,orderCheckId' \
                     ' FROM XiaoFei WHERE createdTime BETWEEN \'{}\' and \'{}\' ORDER BY createdTime DESC '.format(
                startTime, endTime)
        else:
            sqlStr = 'SELECT orderCheckId,orderNo,createdTime,pcSign,carId,carUser,carPhone,carModel,workerName,project,attribute' \
                     ' FROM XiaoFei WHERE createdTime BETWEEN \'{}\' and \'{}\' ORDER BY createdTime DESC '.format(
                startTime, endTime)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 插入消费信息
    def InsertXiaoFei(self, saveData):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "INSERT INTO XiaoFei (id,orderNo,carId,pcId,workerId,userId," \
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
        self.conn.execute(sqlStr)
        self.conn.commit()
        # try:
        # # print (sqlStr)
        #     self.conn.execute(sqlStr)
        #     self.conn.commit()
        # except:
        #     pass
        self.conn.close()

    # 获取门店服务器一级菜单
    def getOneMenu(self):
        self.conn = sqlite3.connect('MYDATA.db')

        sqlStr = 'SELECT id,name FROM OneMenu ORDER BY createdTime DESC '

        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 插入一级菜单
    def InsertOneMenu(self, saveData):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "INSERT INTO OneMenu (name,createdTime) VALUES ('{}','{}')".format(saveData.get('name', ""),
                                                                                    saveData.get("createdTime", ""))
        self.conn.execute(sqlStr)
        self.conn.commit()
        self.conn.close()

    # 获取门店服务器二级菜单
    def getTwoMenu(self, father):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT id,name,attribute,attributeState FROM TwoMenu WHERE father=\'{}\'ORDER BY createdTime DESC '.format(
            father)

        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 插入二级菜单
    def InsertTwoMenu(self, saveData):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "INSERT INTO TwoMenu (name,father,attribute,attributeState,createdTime) " \
                 "VALUES ('{}','{}','{}','{}','{}')".format(saveData.get('name', ""),
                                                            saveData.get("father", ""), saveData.get("attribute", ""),
                                                            saveData.get("attributeState", ""),
                                                            saveData.get("createdTime", ""))
        self.conn.execute(sqlStr)
        self.conn.commit()
        self.conn.close()

    # 获取单个信息
    def GetOneById(self, dbname, id):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT * FROM {} WHERE id={} ORDER BY createdTime DESC '.format(dbname, id)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchone()
        cursor.close()
        self.conn.close()
        return data

    # 修改内容
    def UpdateData(self, dbname, updateData, search):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "UPDATE {} SET {} WHERE {}".format(dbname, updateData, search)
        self.conn.execute(sqlStr)
        self.conn.commit()
        self.conn.close()

    # 删除
    def DeleteData(self, dbname, search):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "DELETE FROM {} WHERE {}".format(dbname, search)
        self.conn.execute(sqlStr)
        self.conn.commit()
        self.conn.close()

    # 插入
    def InsertData(self, dbname, key, value):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "INSERT INTO {} ({}) " \
                 "VALUES ({})".format(dbname, key, value)
        cursor = self.conn.cursor()
        cursor.execute(sqlStr)

        # self.conn.commit()
        id = cursor.lastrowid
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return id

    # 新增员工

    # 查询员工
    def GetWorker(self):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT id,workerName,sex,idCard FROM Worker ORDER BY createdTime DESC '
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        return data

    # 查询系统管理员
    def GetAdmin(self):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT id,username FROM Admin WHERE userName!=\'admin\' ORDER BY createdTime DESC '
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        return data

    # 根据用户名获取管理员
    def GetAdminByUsername(self, username):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT id,pwd FROM Admin WHERE userName=\'{}\' ORDER BY createdTime DESC '.format(username)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchone()
        cursor.close()
        self.conn.close()
        return data

    # 查询设备
    def GetSheBei(self):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = 'SELECT id,ip,state,name FROM Device ORDER BY createdTime DESC '
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        return data

    # 根据ip查询员工
    def GetWorkerByIp(self, ip):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "SELECT id FROM Worker WHERE ip='{}'".format(ip)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchone()
        cursor.close()
        return data

    # 根据ip判断员工
    def CheckWorker(self, ip):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "SELECT state FROM Worker WHERE ip='{}'".format(ip)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchone()
        cursor.close()
        result = False
        if data and data[0] == "1":
            result = True
        return result

    # 根据一个key检索用户
    def GetUserByKey(self, key, value):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "SELECT id,userName,carModel,carPhone,carId FROM User WHERE {}='{}' ORDER BY createdTime DESC ".format(
            key, value)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 检索用户是否存在
    def CheckUser(self, carPhone, carId):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "SELECT id FROM User WHERE carPhone='{}' and carId='{}' ORDER BY createdTime DESC ".format(carPhone,
                                                                                                            carId)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 检索用户的模糊查询
    def GetLikeUserByKey(self, key, value):
        self.conn = sqlite3.connect('MYDATA.db')
        sqlStr = "SELECT id,userName,carModel,carPhone,carId FROM User WHERE {} like '%{}%' ORDER BY createdTime DESC ".format(
            key, value)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 根据一个key检索消费信息
    def GetXiaoFeiByKey(self, key, value, remote=False):
        self.conn = sqlite3.connect('MYDATA.db')
        if remote:
            sqlStr = "SELECT createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,attribute,pcId,orderCheckId,pcSign" \
                     " FROM XiaoFei WHERE {}='{}' AND userId != '' AND userId IS NOT NULL ORDER BY createdTime DESC ".format(
                key, value)
        else:
            sqlStr = "SELECT createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,attribute,pcId,orderCheckId,pcSign" \
                     " FROM XiaoFei WHERE {}='{}' ORDER BY createdTime DESC ".format(key, value)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    # 根据2个key检索消费信息
    def GetXiaoFeiByTwoKey(self, carId, carPhone, remote=False):
        self.conn = sqlite3.connect('MYDATA.db')
        if remote:
            sqlStr = "SELECT createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,attribute,pcId,orderCheckId" \
                     " FROM XiaoFei WHERE carId='{}' and carPhone='{}' AND userId != '' AND userId IS NOT NULL ORDER BY createdTime DESC ".format(
                carId, carPhone)
        else:
            sqlStr = "SELECT createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,attribute,pcId,orderCheckId" \
                     " FROM XiaoFei WHERE carId='{}' and carPhone='{}' ORDER BY createdTime DESC ".format(carId,
                                                                                                          carPhone)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    def CheckSheBei(self, ip, deviceName):
        self.conn = sqlite3.connect('MYDATA.db')
        result = False
        if deviceName == "":
            return result

        sqlStr = "SELECT id,state FROM Device WHERE ip='{}'".format(ip)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchone()
        cursor.close()
        self.conn.close()
        if not data:
            key = "ip,state,name,createdTime"
            word = "员工：{}<br/>请求连接服务器，是否允许？".format(ip)

            try:
                myList = [word, key, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), deviceName, ip]
                config.ui.signal.emit(myList)
                # sqlStr = "SELECT id,state FROM Device WHERE ip='{}'".format(ip)
                # cursor = self.conn.execute(sqlStr)
                # data = cursor.fetchone()
                # cursor.close()
                # self.conn.close()
                # if data[1] == "1":
                result = 2
            except:
                pass
        else:
            if data[1] == "1":
                result = True
        return result

    def GetOrderNo(self, today):
        self.conn = sqlite3.connect('MYDATA.db')
        month = str(today.month)
        day = str(today.day)
        year = today.year
        if len(month) < 2:
            month = "0" + month
        if len(day) < 2:
            day = "0" + day

        startTime = '{}-{}-{} 00:00:00'.format(year, month, day)
        endTime = '{}-{}-{} 23:59:59'.format(year, month, day)

        sqlStr = "SELECT count(*) FROM XiaoFei WHERE createdTime BETWEEN \'{}\' and \'{}\' group by OrderNo".format(
            startTime, endTime)
        cursor = self.conn.execute(sqlStr)
        data = cursor.fetchall()
        number = str(len(data) + 1)
        self.conn.close()
        # number格式为百位数，如001，002，100，120
        if len(number) < 2:
            number = "00" + number
        elif len(number) < 3:
            number = "0" + number

        orderNo = "{}{}{}{}".format(year, month, day, number)
        return orderNo

    def GetCallBack(self):
        self.conn = sqlite3.connect('MYDATA.db')
        now = datetime.now()
        timeStr = "{}/{}/{}".format(now.year, now.month, now.day)
        timeStr = Common.MakeTime(timeStr, True)

        sqlStr = 'SELECT id,username,carId,phone,callbackTime FROM CallBack WHERE state=\'0\' AND callbackTime <= \'{}\' ORDER BY createdTime DESC '.format(
            timeStr)
        cursor = self.conn.execute(sqlStr)
        datas = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return datas