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
from Common.StaticFunc import ErrorCode

class ApiException(Exception):
    '''全局错误码exception，搭配ErrorCode使用'''
    @staticmethod
    def get_forWorker(errorCode):
        return ErrorCode.ERROR_MESSAGE.get(errorCode, 2000)['forWorker']

    @staticmethod
    def get_forUser(errorCode):
        return ErrorCode.ERROR_MESSAGE.get(errorCode, 2000)['forUser']

    @staticmethod
    def get_error_result(errorCode):
        return {
            "forWorker": ApiException.get_forWorker(errorCode),
            "errorCode": str(errorCode),
            'forUser' : ApiException.get_forUser(errorCode)
        }

    @property
    def error_result(self):
        return self.get_error_result(self.errorCode)

    def __init__(self, errorCode=None):
        self.errorCode = errorCode
        self.message = self.get_forWorker(self.errorCode)
        self.forUser = self.get_forUser(self.errorCode)
