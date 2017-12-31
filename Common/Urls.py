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
from Controller.Api import ApiWorkerHandler, ApiUserHandler, ApiOrderHandler, ApiServiceHandler

route = [
    ("/worker/check/(code|ip|list)/", ApiWorkerHandler.ApiWorker_Handler),
    ("/worker/get/(list)/", ApiWorkerHandler.ApiWorker_Handler),
    ("/user/get/(find|order)/", ApiUserHandler.ApiUser_Handler),
    ("/user/post/(add)/", ApiUserHandler.ApiUser_Handler),
    ("/order/get/(detail)/", ApiOrderHandler.ApiOrder_Handler),
    ("/order/post/(add|preview)/", ApiOrderHandler.ApiOrder_Handler),
    ("/service/get/(one|two)/", ApiServiceHandler.ApiService_Handler),
]
