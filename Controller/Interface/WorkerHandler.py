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

dbhelp = DbHandler.DB_Handler()

def SubmitWorker(name,sex,idCard,id=None):
    if id:
       search = "id={}".format(id)
       updateData = "workerName=\'{}\',idCard=\'{}\',sex=\'{}\'".format(name,idCard,sex)
       dbhelp.UpdateData("Worker",updateData,search)
    else:
       key = "workerName,sex,idCard,createdTime"
       value = "'{}','{}','{}','{}'".format(name,sex,idCard,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       dbhelp.InsertData("Worker",key,value)
