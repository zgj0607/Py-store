# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/22/2016'

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
import sqlite3
from datetime import datetime


# 消费记录表
def CreateXiaofei():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE Sales
           (id VARCHAR(35) PRIMARY KEY,
           userId INTEGER NOT NULL ,
           code VARCHAR(100) NOT NULL,
           pcId VARCHAR(32) NOT NULL,
           pcSign VARCHAR(32) NOT NULL,
           project VARCHAR(50) NOT NULL,
           workerId INTEGER NOT NULL,
           workerName VARCHAR(20) NOT NULL,
           carId VARCHAR(10)  NOT NULL,
           carUser VARCHAR(50),
           carPhone  VARCHAR(50),
           carModel VARCHAR(30),
           attribute TEXT,
           createdTime DATETIME NOT NULL,
           orderNo VARCHAR(32) NOT NULL,
           orderCheckId VARCHAR(32) NOT NULL
           );''')

    conn.execute('''
          CREATE INDEX userId
              ON Sales (userId);
          ''')
    conn.execute('''
          CREATE INDEX createdTime
              ON Sales (createdTime);
          ''')
    conn.close()


# 用户表
def CreateUser():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE User
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           userName VARCHAR(20) NOT NULL,
           carModel VARCHAR (30) NOT NULL ,
           carPhone VARCHAR (15) NOT NULL,
           carId VARCHAR (10) NOT NULL,
           createdTime DATETIME NOT NULL
           );''')

    conn.execute('''
          CREATE UNIQUE INDEX carid
              ON User (carId);
          ''')
    conn.close()


# 员工表
def CreateWorker():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE Worker
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           workerName VARCHAR(20) NOT NULL,
           sex VARCHAR (4) NOT NULL ,
           idCard VARCHAR (20) NOT NULL ,
           createdTime DATETIME NOT NULL
           );''')
    conn.close()


# 管理员（系统人员）表
def CreateAdmin():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE Admin
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           userName VARCHAR(20) NOT NULL,
           pwd VARCHAR (32) NOT NULL ,
           createdTime DATETIME NOT NULL
           );''')

    conn.execute('''
          CREATE UNIQUE INDEX userName
              ON Admin (userName);
          ''')

    sqlStr = "INSERT INTO Admin (userName,pwd,createdTime) " \
             "VALUES ('{}','{}','{}')".format('admin', 'e93a9a6047903bd088bd4ffee28fdee8', datetime.now())
    conn.execute(sqlStr)
    conn.commit()

    conn.close()


# 门店服务的一级菜单
def CreateOneMenu():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE OneMenu
      (id INTEGER PRIMARY KEY AUTOINCREMENT,
      createdTime DATETIME NOT NULL ,
       name VARCHAR (20) NOT NULL
      );
    ''')

    conn.close()


# 门店服务的二级菜单
def CreateTwoMenu():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE TwoMenu
      (id INTEGER PRIMARY KEY AUTOINCREMENT,
       createdTime DATETIME NOT NULL ,
       name VARCHAR (20) NOT NULL ,
       father INTEGER NOT NULL ,
       attribute VARCHAR (1000) NOT NULL,
       attributeState VARCHAR (1000) NOT NULL
      );
    ''')

    conn.execute('''
          CREATE UNIQUE INDEX father
              ON service (father,name);
          ''')

    conn.close()


# 设备表
def CreateDevice():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE Device
      (id INTEGER PRIMARY KEY AUTOINCREMENT,
       createdTime DATETIME NOT NULL ,
       name VARCHAR (20) NOT NULL ,
       ip VARCHAR (20) NOT NULL ,
       state VARCHAR (2) NOT NULL
      );
    ''')

    conn.execute('''
          CREATE UNIQUE INDEX ip
              ON Device (ip);
          ''')

    conn.close()


# 回访表
def CreateCallBack():
    conn = sqlite3.connect('MYDATA.db')
    conn.execute('''CREATE TABLE CallBack
      (id INTEGER PRIMARY KEY AUTOINCREMENT,
       createdTime DATETIME NOT NULL ,
       callbackTime DATETIME NOT NULL ,
       phone VARCHAR(50) NOT NULL ,
       carId VARCHAR(10) NOT NULL ,
       username VARCHAR(50) NOT NULL ,
       state VARCHAR (2) NOT NULL
      );
    ''')

    conn.close()


# 创建所有表
def CreateAllDb():
    print("Opened database successfully")
    try:
        CreateXiaofei()
    except:
        pass

    try:
        CreateDevice()
    except:
        pass

    try:
        CreateOneMenu()
    except:
        pass

    try:
        CreateTwoMenu()
    except:
        pass

    try:
        CreateUser()
    except:
        pass

    try:
        CreateWorker()
    except:
        pass

    try:
        CreateAdmin()
    except:
        pass

    try:
        CreateCallBack()
    except:
        pass

    print("Table created successfully")
