from decimal import Decimal

from Common import Common
from Common.time_utils import get_now
from database.db_connection import execute

supplier_table_name = 'supplier'


def get_all_supplier():
    sql_text = '''SELECT ID, SUPPLIER_NAME FROM supplier WHERE DELETE_STATE = 0 ORDER BY SUPPLIER_NAME'''
    result = execute(sql_text)

    return result


def add_supplier(supplier_name: str):
    sql_text = '''INSERT INTO supplier(
                                        supplier_name,
                                        create_time,
                                        create_op)
                  VALUES(
                          '{}',
                          '{}',
                           {})''' \
        .format(supplier_name, get_now(), Common.config.login_user_info[0])

    result = execute(sql_text)

    return result


def get_supplier_by_name(name):
    sql_text = '''SELECT ID, supplier_name FROM supplier WHERE supplier_name = '{}\''''.format(name)
    return execute(sql_text, True)


def update_supplier_unpaid(supplier_id: int, unpaid: Decimal):
    sql_text = '''update supplier
                     set unpaid = unpaid + {:.2f}
                   where id = {}
                ''' \
        .format(unpaid, supplier_id)
    execute(sql_text)
