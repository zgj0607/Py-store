# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/3/1'
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
from socket import *
from Common.config import ADDR, code

linkKey = None

try:
    myClient = socket(AF_INET, SOCK_STREAM)
    myClient.connect(ADDR)
except:
    myClient = None
