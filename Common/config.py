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
import configparser
import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from domain.store import Store


# 配置文件信息父级目录
def get_config_file_parent():
    return 'config/'


# 店面信息文件路径
def get_store_info_file():
    return get_config_file_parent() + 'pc.conf'


# 注册信息文件路径
def get_register_info_file():
    return get_config_file_parent() + 'config.ini'


# 打印字体设置信息保存文件
def get_printer_font_file():
    return get_config_file_parent() + 'printer.txt'


# 秘密文件信息
def get_secret_info_file():
    return get_config_file_parent() + 'secret.conf'


def initialization_config():
    register_file = get_register_info_file()
    attribute_root = 'attribute.txt'
    pc_root = get_store_info_file()
    printer_root = get_printer_font_file()
    secret_root = get_secret_info_file()
    host = ""
    basic_msg = configparser.ConfigParser()
    basic_msg.read(register_file)
    # 初始化内容
    if not os.path.exists(register_file):
        basic_msg.add_section("msg")
        basic_msg.set("msg", "code", "")
        basic_msg.set("msg", "storeId", "")
        basic_msg.set("msg", "ip", "")
        basic_msg.write(open(register_file, "w"))
    else:
        try:
            temp_host = basic_msg.get('msg', 'ip')
            if temp_host and temp_host != "":
                host = temp_host
        except Exception as e:
            print(e)
            pass

    if not os.path.exists(attribute_root):
        fp = open(attribute_root, 'wb')
        fp.close()

    if not os.path.exists(pc_root):
        fp = open(pc_root, 'wb')
        fp.close()

    if not os.path.exists(printer_root):
        fp = open(printer_root, 'wb')
        fp.write("7".encode())
        fp.close()

    if not os.path.exists(secret_root):
        fp = open(secret_root, 'wb')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fp.write(now.encode())
        fp.close()

    return host, basic_msg.get('msg', 'code')


def get_local_store_info():
    file = open("pc.conf", 'rb')

    local_info = file.readline().decode()
    file.close()
    local_info = local_info.split(',')
    store = Store()
    store.id(local_info[0])
    if not len(local_info) < 4:
        store.phone(local_info[1])
        store.address(local_info[2])
        store.name(local_info[3])

    return store


def get_store_name():
    store = get_local_store_info()
    return store.name()


def get_print_font_size():
    fp = open(get_printer_font_file(), 'rb')
    data = fp.readline().decode().replace("\n", "").replace("\r", "").replace("\ufeff", "")
    fp.close()
    font_size = 7
    if data:
        try:
            font_size = int(data)
        except Exception as e:
            print(e)

    return font_size


PORT = 8555
PORT2 = 8556

tempHost, code = initialization_config()
if tempHost and tempHost != "":
    HOST = tempHost
else:
    # HOST='127.0.0.1' #本地测试
    # HOST='119.23.66.37'  #新服务器
    HOST = '119.23.39.238'  # 门店服务器

# webHOST='127.0.0.1' #本地测试
# webHOST='119.23.66.37'  #新服务器
webHOST = '119.23.39.238'  # 门店服务器

# 记录主窗口的引用，实现线程间的共享调用
ui = None

BUFSIZ = 1024
# 这个是长连接端口，用于终端长链接服务器通讯
ADDR = (HOST, PORT)
# 这个是短链接，用户终端请求服务器获取数据
TempADDR = (HOST, PORT2)

domain = "http://{}:8500/".format(webHOST)

savePath = "消费报表/"
menuSavePath = "菜单/"

connect = False

heartbeatCheck = True

scheduler = BlockingScheduler()

login_user_info = []
