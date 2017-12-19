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
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def initializationConfig():
    root = 'config.ini'
    attributeRoot = 'attribute.txt'
    pcRoot = 'pc.conf'
    printerRoot = 'printer.txt'
    secretRoot = 'secret.conf'
    HOST = ""
    basicMsg = configparser.ConfigParser()
    basicMsg.read(root)
    # 初始化内容
    if not os.path.exists(root):
        basicMsg.add_section("msg")
        basicMsg.set("msg", "code", "")
        basicMsg.set("msg", "storeId", "")
        basicMsg.set("msg", "ip", "")
        basicMsg.write(open(root, "w"))
    else:
        try:
            tempHOST = basicMsg.get('msg', 'ip')
            if tempHOST and tempHOST != "":
                HOST = tempHOST
        except:
            pass
    code = basicMsg.get('msg', 'code')

    if not os.path.exists(attributeRoot):
        fp = open(attributeRoot, 'wb')
        fp.close()

    if not os.path.exists(pcRoot):
        fp = open(pcRoot, 'wb')
        fp.close()

    if not os.path.exists(printerRoot):
        fp = open(printerRoot, 'wb')
        fp.write("7".encode())
        fp.close()

    if not os.path.exists(secretRoot):
        fp = open(secretRoot, 'wb')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fp.write(now.encode())
        fp.close()

    return HOST, code


PORT = 8555
PORT2 = 8556

tempHost, code = initializationConfig()
if tempHost and tempHost != "":
    HOST = tempHost
else:
    # HOST='127.0.0.1' #本地测试
    # HOST='120.76.161.36' #旧服务器
    # HOST='119.23.66.37'  #新服务器
    HOST = '119.23.39.238'  # 门店服务器

# webHOST='127.0.0.1' #本地测试
# webHOST='120.76.161.36' #旧服务器
# webHOST='119.23.66.37'  #新服务器
webHOST = '119.23.39.238'  # 门店服务器

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
