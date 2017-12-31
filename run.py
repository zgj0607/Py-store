# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/21/2016'

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
import sys
from View.login.register import Register as Reg_Ui_MainWindow
from View.login.login import Login
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTranslator
from PyQt5 import QtWidgets
import decimal
import configparser
import socket
import json
from Common.config import BUFSIZ
from Common import config
from server.MySocket import myClient
from Common import Common
import threading
import CreateSqlite
import sqlite3
from datetime import datetime, timedelta
import requests
from View.main.callback import CallBack_Ui_MainWindow
import apscheduler
from apscheduler.triggers.cron import CronTrigger
import os

decimal.__version__
apscheduler.__version__


# 运行之前要检查配置文件
def beforeRun():
    result = False
    root = 'config.ini'

    basicMsg = configparser.ConfigParser()
    basicMsg.read(root)

    code = None
    try:
        code = basicMsg.get('msg', 'code')
    except:
        pass

    if Common.CheckCodeLocal(code):
        result = True

    return result


def CheckCallBack():
    conn = sqlite3.connect('MYDATA.db')
    now = datetime.now()
    timeStr = "{}/{}/{}".format(now.year, now.month, now.day)
    timeStr = Common.MakeTime(timeStr, True)

    sqlStr = 'SELECT callbackTime,phone,username,carId,id FROM CallBack WHERE state=\'0\' AND callbackTime <= \'{}\' ORDER BY createdTime DESC '.format(
        timeStr)
    cursor = conn.execute(sqlStr)
    datas = cursor.fetchall()
    cursor.close()
    conn.close()
    return datas


# 回访设置
def CallBack(ui):
    datas = CheckCallBack()
    for data in datas:
        msg = "您于  <b>{}</b> 要回访用户 ： <b>{}</b><br>联系方式为 ： <b>{}</b><br>车牌号为 ： <b>{}</b>".format(data[0][:10], data[2],
                                                                                                data[1], data[3])
        ui = CallBack_Ui_MainWindow(msg, data[4], data[1], data[3], data[2])
        ui.exec_()


def runView():
    translator = QTranslator()
    translator.load("qt_zh_CN.qm")
    app = QApplication(sys.argv)
    ui = None
    # 判断是否在试用期内
    # check = TryUse()
    check = True
    if check:
        # 判断注册码是否正确
        if beforeRun():
            # 链接服务器
            if Common.config.connect:
                try:
                    myClient.send("connect {}".format(Common.GetStoreId()).encode())
                    data, addr = myClient.recvfrom(BUFSIZ)
                    Common.linkKey = data.decode()

                    def HeartBeat():
                        try:
                            if config.heartbeatCheck:
                                myClient.send("heartbeat heartbeat".encode())
                            else:
                                config.heartbeatCheck = True
                        except:
                            try:
                                config.scheduler.shutdown()
                            except:
                                pass

                    def SchedulerStart(scheduler):
                        try:
                            scheduler.start()
                        except (KeyboardInterrupt, SystemExit, Exception):
                            scheduler.shutdown()

                    trigger = CronTrigger(minute='*')
                    config.scheduler.add_job(HeartBeat, trigger)
                    schedule = threading.Thread(target=SchedulerStart, args=[config.scheduler])
                    if Common.config.connect:
                        schedule.start()

                except Exception as main_exception:
                    print(main_exception)
                    Common.config.connect = False

            try:
                # ui = SheZhi_Ui_MainWindow()
                ui = Login()

            except Exception as e:
                print(e)
                pass
        else:
            ui = Reg_Ui_MainWindow()
        # Common.skin_change('Common/qss/white.qss')
        CallBack(ui)
        ui.show()
        sys.exit(app.exec_())

    else:
        if check == "online":
            msg = "请链接网络"
        else:
            msg = "您的试用期已过，详情请联系官方。"
        ui = Reg_Ui_MainWindow()
        QtWidgets.QMessageBox.information(ui.pushButton, "提示", msg)
        ui.close()
        sys.exit(app.exec_())


def IsOpen(port=15775, ip='127.0.0.1'):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        c.connect((ip, port))
        c.shutdown(2)
        c.close()
        return True
    except:
        return False


def TryUse():
    # now = datetime.now()
    url = 'http://119.23.39.238:8500/store/api/time'
    try:
        req = requests.get(url)
    except:
        return "online"
    jsonData = json.loads(req.text)
    now = datetime.strptime(jsonData.get("data"), "%Y-%m-%d %H:%M:%S")
    if (os.path.isfile('secret.conf')):
        fp = open('secret.conf', 'rb')
        record = fp.readline()
        if not record:
            return False
        else:
            record = record.decode()
            recordTime = datetime.strptime(record, "%Y-%m-%d %H:%M:%S")

            if now > (recordTime + timedelta(days=30)):
                return False
            else:
                return True
    else:
        return False


if __name__ == '__main__':

    if not IsOpen():
        try:
            CreateSqlite.CreateAllDb()
            runView()
            # viewThread = threading.Thread(target=runView)
            # viewThread.start()
        except Exception as e:
            print(e)
            pass
