# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '12/11/2016'

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
from controller.web import worker_handler, customer_handler, order_handler, service_handler

route = [
    ("/worker/check/(code|ip|list)/", worker_handler.WorkerHandler),
    ("/worker/get/(list)/", worker_handler.WorkerHandler),
    ("/user/get/(find|order)/", customer_handler.CustomerHandler),
    ("/user/post/(add)/", customer_handler.CustomerHandler),
    ("/order/get/(detail)/", order_handler.OrderHandler),
    ("/order/post/(add|preview)/", order_handler.OrderHandler),
    ("/service/get/(one|two|brand|model|balance)/", service_handler.ServiceHandler),
]
