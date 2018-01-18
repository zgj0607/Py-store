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
import decimal
import logging
import socket
import sys
import threading
from datetime import timedelta

import apscheduler
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import *
from apscheduler.triggers.cron import CronTrigger

import init_database
from Common import Common
from Common import config
from Common.config import BUFSIZ
from View.customer.return_visit_setting import ReturnVisitSetting
from View.login.login import Login
from View.login.register import Register as Reg_Ui_MainWindow
from database.dao.customer.customer_handler import get_return_visit_info
from remote import store_pc_info
from server.MySocket import myClient

decimal.__version__
apscheduler.__version__


# 运行之前要检查配置文件
def pre_check():
    result = False
    local_code = config.get_local_register_code()

    if Common.compare_local_code_with_remote_register(local_code):
        result = True

    return result


# 回访设置
def return_visit():
    result_data = get_return_visit_info()
    for data in result_data:
        ui = ReturnVisitSetting(data['next_visit_time'], record_id=data['id'], car_phone=data['phone'],
                                car_id=data['carId'], car_user=data['username'])
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
                    myClient.send("connect {}".format(Common.get_store_id()).encode())
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
    now = store_pc_info.get_try_time()
    if now == 'online':
        return now

    local_start_use_time = config.get_local_start_use_time()

    if not local_start_use_time:
        return False
    else:
        if now > (local_start_use_time + timedelta(days=30)):
            return False
        else:
            return True


if __name__ == '__main__':
    my_format = '%(asctime)s  %(filename)s.%(module)s.%(funcName)s: %(lineno)s : %(levelname)s  %(message)s'  # 定义输出log的格式
    my_date_format = '%Y-%m-%d %A %H:%M:%S'
    logging.basicConfig(filename=config.get_log_file_name(),
                        filemode="a",
                        level=logging.DEBUG,
                        format=my_format,
                        datefmt=my_date_format)
    logger = logging.getLogger(__name__)

    if not is_open():
        try:
            init_database.create_all_table()
            run()
        except Exception as e:
            logger.error(e)
            pass
