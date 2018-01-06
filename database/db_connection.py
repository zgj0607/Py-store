import sqlite3

# 数据库游标
cursor = None

# 数据库连接
connection = None

# 事物是否开启
is_transaction = False


def get_connection():
    global connection
    if connection:
        return connection

    if is_transaction:
        connection = sqlite3.connect('MYDATA.db', isolation_level=None)
    else:
        connection = sqlite3.connect('MYDATA.db')
    return connection


def get_cursor():
    global cursor
    if cursor:
        return cursor
    cursor = get_connection().cursor()
    return cursor


def release_connection(conn):
    conn.close()
    global connection
    connection = None
    global cursor
    cursor = None


def execute(sql_text: str):
    conn = get_connection()
    cur = get_cursor()

    print("执行脚本：", sql_text)

    cur.execute(sql_text)
    if sql_text.upper().lstrip().lstrip('\s').startswith('INSERT'):
        result = cur.lastrowid
    else:
        result = cur.fetchall()

    print("执行结果数据：", result)

    if not is_transaction:
        conn.commit()
        release_connection(conn)

    return result
