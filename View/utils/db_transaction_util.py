import logging

from database import db_connection

logger = logging.getLogger(__name__)

def begin():
    print('开启事物')
    db_connection.is_transaction = True
    db_connection.commit_point = False
    db_connection.connection = db_connection.get_connection()
    cursor = db_connection.get_cursor()

    cursor.execute('BEGIN')
    logger.info('事物已开启')


def commit():
    cursor = db_connection.get_cursor()
    logger.info('提交事物')

    cursor.execute('COMMIT')
    logger.info('事物已提交')
    close()


def rollback():
    cursor = db_connection.get_cursor()
    logger.info('回滚事物')
    cursor.execute('ROLLBACK')
    logger.info('事物已回滚')

    close()


def close():
    cursor = db_connection.get_cursor()
    cursor.close()

    conn = db_connection.get_connection()
    db_connection.release_connection(conn)

    db_connection.is_transaction = False
