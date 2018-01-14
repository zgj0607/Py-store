from Common import Common
from Common.time_utils import get_now
from database.db_connection import execute

model_table_name = 'brand'


def get_all_brand():
    sql_text = '''SELECT ID, BRAND_NAME FROM brand WHERE DELETE_STATE = 0 ORDER BY BRAND_NAME'''

    result = execute(sql_text)
    return result

def get_all_staff():
    sql_text = '''SELECT ID, UserNAME FROM Admin ORDER BY UserNAME'''

    result = execute(sql_text)
    return result

def add_brand(brand_name: str):
    sql_text = '''INSERT INTO brand(
                                    BRAND_NAME,
                                    create_time,
                                    create_op
                                    )
                  VALUES(
                          '{}',
                          '{}',
                          {}
                  )''' \
        .format(brand_name, get_now(), Common.config.login_user_info[0])

    result = execute(sql_text)

    return result


def get_brand_by_name(brand_name: str):
    sql_text = '''SELECT ID, BRAND_NAME FROM brand WHERE DELETE_STATE = 0 and brand_name ='{}\'''' \
        .format(brand_name)

    result = execute(sql_text, True)

    return result


def update_brand(brand_id: int, brand_name: str):
    sql_text = '''UPDATE BRAND SET brand_name = '{}' WHERE ID = {}'''.format(brand_name, brand_id)

    result = execute(sql_text)

    return result
