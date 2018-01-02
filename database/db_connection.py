import sqlite3


def get_connection():
    return sqlite3.connect('MYDATA.db')


def release_connection(conn):
    conn.close()


def execute(sql_text: str):
    conn = get_connection()
    print("执行脚本：", sql_text)
    cursor = conn.execute(sql_text)
    if sql_text.upper().startswith('INSERT'):
        result = cursor.lastrowid
    else:
        result = cursor.fetchall()
    print("执行结果数据：", result)
    conn.commit()
    release_connection(conn)

    return result
