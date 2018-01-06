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
import configparser
import decimal
import json
import os
import socket
import sys
import threading
from datetime import datetime, timedelta

import apscheduler
import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import *
from apscheduler.triggers.cron import CronTrigger

import CreateSqlite
from Common import Common
from Common import config
from Common.config import BUFSIZ
from View.customer.return_visit_setting import ReturnVisitSetting
from View.login.login import Login
from View.login.register import Register as Reg_Ui_MainWindow
from database.dao.customer.customer_handler import get_return_visit_info
from server.MySocket import myClient

decimal.__version__
apscheduler.__version__


# 运行之前要检查配置文件
def pre_check():
    result = False
    root = 'config.ini'

    basic_msg = configparser.ConfigParser()
    basic_msg.read(root)

    code = None
    try:
        code = basic_msg.get('msg', 'code')
    except Exception as check_exception:
        print(check_exception)
        pass

    if Common.CheckCodeLocal(code):
        result = True

    return result


# 回访设置
def return_visit():
    result_data = get_return_visit_info()
    for data in result_data:
        msg = "您于  <b>{}</b> 要回访用户 ： <b>{}</b><br>联系方式为 ： <b>{}</b><br>车牌号为 ： <b>{}</b>" \
            .format(data[0][:10], data[2], data[1], data[3])
        ui = ReturnVisitSetting(msg, record_id=data[4], car_phone=data[1], car_id=data[3], car_user=data[2])
        ui.exec_()


def run():
    translator = QTranslator()
    translator.load("qt_zh_CN.qm")
    app = QApplication(sys.argv)
    ui = None
    # 判断是否在试用期内
    # check = TryUse()
    check = True
    if check:
        # 判断注册码是否正确
        if pre_check():
            # 链接服务器
            if Common.config.connect:
                try:
                    myClient.send("connect {}".format(Common.GetStoreId()).encode())
                    data, addr = myClient.recvfrom(BUFSIZ)
                    Common.linkKey = data.decode()

                    def heart_beat():
                        try:
                            if config.heartbeatCheck:
                                myClient.send("heartbeat heartbeat".encode())
                            else:
                                config.heartbeatCheck = True
                        except Exception as run_exception:
                            print(run_exception)
                            try:
                                config.scheduler.shutdown()
                            except Exception as shutdown_exception:
                                print(shutdown_exception)
                                pass

                    def scheduler_start(scheduler):
                        try:
                            scheduler.start()
                        except (KeyboardInterrupt, SystemExit, Exception):
                            scheduler.shutdown()

                    trigger = CronTrigger(minute='*')
                    config.scheduler.add_job(heart_beat, trigger)
                    schedule = threading.Thread(target=scheduler_start, args=[config.scheduler])
                    if Common.config.connect:
                        schedule.start()

                except Exception as main_exception:
                    print(main_exception)
                    Common.config.connect = False

            try:
                ui = Login()

            except Exception as exception:
                print(exception)
                pass
        else:
            ui = Reg_Ui_MainWindow()
        Common.skin_change('qss/white.qss')
        return_visit()
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


def is_open(port=15775, ip='127.0.0.1'):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        c.connect((ip, port))
        c.shutdown(2)
        c.close()
        return True
    except Exception as socket_exception:
        print(socket_exception)
        return False


def try_use():
    # now = datetime.now()
    url = 'http://119.23.39.238:8500/store/api/time'
    try:
        req = requests.get(url)
    except Exception as try_use_exception:
        print(try_use_exception)
        return "online"
    json_data = json.loads(req.text)
    now = datetime.strptime(json_data.get("data"), "%Y-%m-%d %H:%M:%S")

    if os.path.isfile('secret.conf'):
        fp = open('secret.conf', 'rb')
        record = fp.readline()
        if not record:
            return False
        else:
            record = record.decode()
            record_time = datetime.strptime(record, "%Y-%m-%d %H:%M:%S")

            if now > (record_time + timedelta(days=30)):
                return False
            else:
                return True
    else:
        return False


if __name__ == '__main__':

    if not is_open():
        try:
            CreateSqlite.CreateAllDb()
            run()
        except Exception as e:
            print(e)
            pass
