import logging
import sqlite3

from common import config

# 数据库游标

cursor = None

# 数据库连接
connection = None

# 事物是否开启
is_transaction = False


def get_connection():
    db_file = config.get_database_file()
    global connection
    if connection:
        return connection

    if is_transaction:
        connection = sqlite3.connect(db_file, isolation_level=None)
    else:
        connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
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


def execute(sql_text: str, fetch_one=False):
    conn = get_connection()
    cur = get_cursor()

    logger = logging.getLogger(__name__)

    logger.info("执行SQL：\n" + sql_text)

    cur.execute(sql_text)
    upper_text = sql_text.upper().lstrip().lstrip('\s')
    if upper_text.startswith('INSERT'):
        result = cur.lastrowid
    else:
        if upper_text.startswith('UPDATE') or upper_text.startswith('DELETE'):
            result = connection.total_changes
        else:
            if fetch_one:
                result = cur.fetchone()
            else:
                result = cur.fetchall()

    logger.info('SQL执行成功')

    if not is_transaction:
        conn.commit()
        release_connection(conn)

    return result
