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
import sqlite3


def get_password(username: str) -> str:
    try:
        connection = sqlite3.connect('MYDATA.db')
        sql_string = "SELECT pwd FROM Admin WHERE userName=\'{}\'".format(username)
        cursor = connection.execute(sql_string)
        data = cursor.fetchone()
        cursor.close()
        connection.close()

        if data:
            return data[0]
        return ''
    except Exception as e:
        print(e)
        return ''
