# -*- coding: utf-8 -*-
import logging

from common import time_utils
from database.db_connection import execute


# 消费记录表
def create_sale():
    execute('''
          CREATE TABLE Sales
            (
              id           VARCHAR(35),
              userId       INTEGER      NOT NULL,
              code         VARCHAR(100) NOT NULL,
              pcId         VARCHAR(32)  NOT NULL,
              pcSign       VARCHAR(32)  NOT NULL,
              service_id   INTEGER,
              project      VARCHAR(50)  NOT NULL,
              workerId     INTEGER      NOT NULL,
              workerName   VARCHAR(20)  NOT NULL,
              carId        VARCHAR(10)  NOT NULL,
              carUser      VARCHAR(50),
              carPhone     VARCHAR(50),
              carModel     VARCHAR(30),
              createdTime  DATETIME     NOT NULL,
              orderNo      VARCHAR(32)  NOT NULL,
              orderCheckId VARCHAR(32)  NOT NULL,
              unit         VARCHAR(20),
              unit_price   VARCHAR(30),
              number       INTEGER,
              subtotal     INTEGER,
              total        INTEGER,
              note         TEXT,
              sale_date    VARCHAR(50),
              attribute    TEXT,
              sale_id      INTEGER PRIMARY KEY AUTOINCREMENT
            )
            ''')

    execute('''CREATE INDEX userId ON Sales (userId)''')

    execute('''CREATE    INDEX    sales_service_ID    ON Sales(service_id)''')

    execute('''CREATE INDEX sales_card_id ON Sales(carId)''')

    execute('''CREATE INDEX createdTime ON Sales (createdTime);''')


# 客户信息表
def create_customer():
    execute('''
        CREATE TABLE User
        (
          id          INTEGER PRIMARY KEY AUTOINCREMENT,
          userName    VARCHAR(20),
          carModel    VARCHAR(30),
          carPhone    VARCHAR(15),
          carId       VARCHAR(10),
          createdTime DATETIME
        )'''
            )
    execute('''CREATE UNIQUE INDEX carid ON User (carId)''')


# 门店职工表
def create_worker():
    execute('''CREATE TABLE Worker
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           workerName VARCHAR(20) NOT NULL,
           sex VARCHAR (4) NOT NULL ,
           idCard VARCHAR (20) NOT NULL ,
           createdTime DATETIME NOT NULL
           );''')


# PC系统用户表
def create_user():
    execute('''CREATE TABLE Admin
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           userName VARCHAR(20) NOT NULL,
           pwd VARCHAR (32) NOT NULL ,
           createdTime DATETIME NOT NULL
           );''')

    execute('''
          CREATE UNIQUE INDEX userName
              ON Admin (userName);
          ''')

    # 写入初始管理员账号admin
    execute("INSERT INTO Admin (userName,pwd,createdTime) " \
            "VALUES ('{}','{}','{}')".format('admin', 'e93a9a6047903bd088bd4ffee28fdee8', time_utils.get_now()))


# 门店服务项目表
def create_service():
    execute('''
        CREATE TABLE service
        (
          id             INTEGER     PRIMARY KEY
          AUTOINCREMENT,
          createdTime    DATETIME    NOT NULL,
          name           VARCHAR(20) NOT NULL,
          father         INTEGER     NOT NULL,
          level          INT,
          attribute      VARCHAR(1000),
          attributeState VARCHAR(1000)
        )
    ''')

    execute('''CREATE UNIQUE INDEX father ON service (father, name)''')


# 创建服务项目扩展属性表
def create_service_item():
    execute('''
        CREATE TABLE service_item
        (
          id             INTEGER     PRIMARY KEY AUTOINCREMENT,
          service_id     INTEGER,
          attribute_id   INTEGER,
          attribute_name VARCHAR(20),
          create_time    VARCHAR(50),
          create_op      INTEGER
        )
    ''')
    execute('''CREATE UNIQUE INDEX service_item_id_uindex ON service_item (id)''')


# 扩展属性信息表
def create_attribute():
    execute('''
        CREATE TABLE Attributes
        (
          id           INTEGER     PRIMARY KEY AUTOINCREMENT,
          name         VARCHAR(20) NOT NULL,
          is_required  INT DEFAULT 0,
          create_time  VARCHAR(50) NOT NULL,
          create_op    INT         NOT NULL,
          delete_state INT DEFAULT 0 NOT NULL,
          display_order INT
        )
        ''')
    execute('''CREATE UNIQUE INDEX serviceAttribute_id_uindex ON attributes (id);''')
    execute('''CREATE UNIQUE INDEX serviceAttribute_name_uindex ON attributes (name)''')
    execute('''INSERT INTO attributes (id, name, is_required, create_time, create_op, delete_state, display_order)
               VALUES (1, '数量', 1, '2018-01-07 23:23:34', 1, 0, 1)''')
    execute('''INSERT INTO attributes (id, name, is_required, create_time, create_op, delete_state, display_order)
               VALUES (2, '单价', 1, '2018-01-07 23:24:02', 1, 0, 2)''')
    execute('''INSERT INTO attributes (id, name, is_required, create_time, create_op, delete_state, display_order)
               VALUES (3, '小计', 1, '2018-01-07 23:24:11', 1, 0, 3)''')
    execute('''INSERT INTO attributes (id, name, is_required, create_time, create_op, delete_state, display_order)
               VALUES (4, '总价', 1, '2018-01-07 23:24:18', 1, 0, 4)''')
    execute('''INSERT INTO attributes (id, name, is_required, create_time, create_op, delete_state, display_order)
               VALUES (5, '备注', 1, '2018-01-07 23:24:35', 1, 0, 5)''')


# PC设备IP管理表
def create_device():
    execute('''
        CREATE TABLE Device
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           createdTime DATETIME NOT NULL ,
           name VARCHAR (20) NOT NULL ,
           ip VARCHAR (20) NOT NULL ,
           state INT
          )
    ''')

    execute('''CREATE UNIQUE INDEX ip ON Device (ip)''')


# 客户回访信息表
def create_return_visit_info():
    execute('''
        CREATE TABLE return_visit
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           create_Time DATETIME NOT NULL ,
           next_visit_time DATETIME NOT NULL ,
           phone VARCHAR(50) NOT NULL ,
           carId VARCHAR(10) NOT NULL ,
           username VARCHAR(50) NOT NULL ,
           state VARCHAR (2) NOT NULL
          )
    ''')


# 字典信息表
def create_dictionary():
    execute('''
        CREATE TABLE dictionary
        (
          id         INTEGER PRIMARY KEY AUTOINCREMENT,
          key_id     INT,
          value_desc VARCHAR(50),
          group_name VARCHAR(50)
        )
        ''')
    execute('''CREATE UNIQUE INDEX dictionary_id_uindex ON dictionary (id)''')

    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (1, 1, '进货', 'buy_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (2, 2, '退货', 'buy_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (3, 0, '进货库存', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (4, 1, '退货库存', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (5, 2, '核增库存', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (6, 3, '核减库存', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (7, 4, '正库存销售', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (8, 0, '已禁用', 'device_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (9, 1, '已启用', 'device_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (10, 0, '选填', 'is_required')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (11, 1, '必填', 'is_required')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (12, 8, '库存校准', 'buy_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (13, 5, '负库存销售', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (14, 6, '已销负销售', 'stock_type')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (15, 0, '正常', 'buy_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (16, 1, '待审核', 'buy_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (17, 2, '已作废', 'buy_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (18, 0, '待回访', 'visit_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (19, 1, '已回访', 'visit_state')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (20, 1, '一级服务项目', 'service_level')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (21, 2, '二级服务项目', 'service_level')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (22, 1, '现金/转账', 'payment')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (23, 2, '信用卡', 'payment')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (24, 3, '微信', 'payment')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (25, 4, '支付宝', 'payment')''')
    execute('''INSERT INTO dictionary (id, key_id, value_desc, group_name) VALUES (26, 5, '支票', 'payment')''')


# 商品品牌表
def create_brand():
    execute('''
        CREATE TABLE brand
        (
          id           INTEGER NOT NULL   PRIMARY KEY    AUTOINCREMENT,
          brand_name   VARCHAR(50),
          create_time  VARCHAR(30),
          create_op    VARCHAR(30),
          delete_state INT DEFAULT 0 NOT NULL
        )
        ''')


# 商品型号表
def create_model():
    execute('''
            CREATE TABLE model
            (
              id           INTEGER NOT NULL   PRIMARY KEY       AUTOINCREMENT,
              model_name   VARCHAR(50),
              brand_id     INT,
              create_time  VARCHAR(30),
              create_op    VARCHAR(30),
              delete_state INT DEFAULT 0 NOT NULL
            )
            ''')


# 创建库存信息表
def create_stock_info():
    execute('''
                CREATE TABLE stock_info
                (
                  id                  INTEGER NOT NULL  PRIMARY KEY  AUTOINCREMENT,
                  unit                VARCHAR(10),
                  first_service_name  VARCHAR(30),
                  first_service_id    INTEGER,
                  model_id            INTEGER,
                  model_name          VARCHAR(100),
                  brand_id            INTEGER,
                  brand_name          VARCHAR(100),
                  name                VARCHAR(150),
                  second_service_id   INTEGER,
                  second_service_name VARCHAR(50),
                  balance             INT,
                  total_cost          INT(18, 2),
                  create_time         VARCHAR(50),
                  create_op           INTEGER
                )
                ''')


# 库存明细表
def create_stock_detail():
    execute('''
            CREATE TABLE stock_detail
            (
              Id          INTEGER NOT NULL  PRIMARY KEY  AUTOINCREMENT,
              stock_id    INTEGER,
              changed_id      INTEGER NOT NULL,
              changed_money   INT(10, 2),
              changed_number  INTEGER,
              type        INT(2),
              update_time VARCHAR(50),
              update_op   INTEGER
            )
            ''')


# 供应商表
def create_supplier():
    execute('''
        CREATE TABLE supplier
        (
          id            INTEGER PRIMARY KEY AUTOINCREMENT,
          supplier_name VARCHAR NOT NULL,
          unpaid        INT(18,2) DEFAULT 0.0,
          create_time   VARCHAR(50),
          create_op     INTEGER,
          delete_state  INT DEFAULT 0 NOT NULL
        )
        ''')
    execute('''CREATE UNIQUE INDEX supplier_id_uindex ON supplier (id)''')
    execute('''CREATE UNIQUE INDEX supplier_supplier_name_uindex ON supplier (supplier_name)''')


# 进货信息表
def create_buy_info():
    execute('''
        CREATE TABLE buy_info
        (
          id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          stock_id    VARCHAR(30),
          supplier_id INTEGER,
          unit_price  INT(10,2),
          number      INTEGER,
          buy_date    VARCHAR(50),
          create_time VARCHAR(50),
          create_op   INTEGER,
          unpaid      INT(10,2),
          paid        INT(10,2),
          total       INT(10,2),
          buy_type    INT(2),
          left_number INTEGER DEFAULT 0,
          state       INT(2)     DEFAULT 0,
          note        VARCHAR(200)
        )
        ''')


# 付款明细表
def create_payment_detail():
    execute('''
        CREATE TABLE payment_detail
        (
          id             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          buy_id         INTEGER,
          payment_method INT,
          paid           INT(18, 2),
          unpaid         INT(18, 2),
          create_time    VARCHAR(50),
          create_op      VARCHAR(50),
          refund_type    INTEGER,
          supplier_id    INTEGER,
          note           VARCHAR(200)
        )
        ''')

    execute('''CREATE UNIQUE INDEX payment_detail_id_uindex ON payment_detail (id)''')


# 创建所有表
def create_all_table():
    logger = logging.getLogger(__name__)
    logger.info("Opened database successfully")
    try:
        create_user()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_customer()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_device()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_worker()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_dictionary()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_brand()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_model()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_attribute()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_service()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_service_item()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_stock_info()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_stock_detail()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_buy_info()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_payment_detail()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_sale()
    except Exception as e:
        logger.error(e)
        pass

    try:
        create_return_visit_info()
    except Exception as e:
        logger.error(e)
        pass
    try:
        create_supplier()
    except Exception as e:
        logger.error(e)
        pass

    logger.info("Table created successfully")
