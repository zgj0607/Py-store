# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/13'
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

def SubmitMenu(name,id,oldName=None):
    if oldName:
        search = "id={}".format(id)
        updateData = "name=\'{}\'".format(name)
        dbhelp.UpdateData("OneMenu",updateData,search)
    else:
        saveData = {
            "name":name,
            "createdTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        dbhelp.InsertOneMenu(saveData)

def SubmitMenu2(name,checkDict,id,oldName=None):
    attribute = ""
    attributeState = ""
    for k,v in checkDict.items():
        if v.checkState() == 2:
            attributeState += "1,"
        else:
            attributeState += "0,"
        attribute += k+","

    attribute = attribute[:-1]
    attributeState = attributeState[:-1]

    if oldName:
        search = "id={}".format(id)
        updateData = "name=\'{}\',attribute=\'{}\',attributeState=\'{}\'".format(name,attribute,attributeState)
        dbhelp.UpdateData("TwoMenu",updateData,search)
    else:
        attributeState = "1,1,1,1,1,1," + attributeState
        attribute = "数量,单价,小计,总价,单位,备注," + attribute
        saveData = {
            "name":name,
            "attribute":attribute,
            "attributeState":attributeState,
            "father":id,
            "createdTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        dbhelp.InsertTwoMenu(saveData)