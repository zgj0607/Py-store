import sqlite3


def get_connection():
    return sqlite3.connect('MYDATA.db')


def release_connection(conn):
    conn.close()


def execute(sql_text):
    conn = get_connection()
    print("执行脚本：", sql_text)
    cursor = conn.execute(sql_text)
    result = cursor.fetchall()
    print("执行结果数据：", result)
    conn.commit()
    release_connection(conn)

    return result
