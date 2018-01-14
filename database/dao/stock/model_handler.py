from Common import Common
from Common.time_utils import get_now
from database.db_connection import execute

model_table_name = 'model'


def get_all_model():
    sql_text = '''SELECT ID, MODEL_NAME, BRAND_ID FROM model WHERE DELETE_STATE = 0 ORDER BY MODEL_NAME'''
    result = execute(sql_text)

    return result


def get_model_by_id(model_id: int):
    sql_text = '''SELECT ID, MODEL_NAME FROM {} WHERE DELETE_STATE = 0 AND ID = {} ORDER BY MODEL_NAME'''.format(
        model_table_name, model_id)
    result = execute(sql_text)

    return result


def get_model_by_brand(brand_id: int):
    sql_text = '''SELECT ID, MODEL_NAME FROM {} WHERE DELETE_STATE = 0 AND brand_id = {} ORDER BY MODEL_NAME'''.format(
        model_table_name, brand_id)
    result = execute(sql_text)

    return result


def add_model(model_name: str, brand_id):
    sql_text = '''INSERT INTO model(
                                    model_name,
                                    brand_id,
                                    create_time,
                                    create_op)
                  VALUES('{}',{},'{}',{})''' \
        .format(model_name, brand_id, get_now(), Common.config.login_user_info[0])

    result = execute(sql_text)

    return result


def get_model_by_name(model_name: str, brand_id: int):
    sql_text = '''SELECT ID, MODEL_NAME FROM model WHERE DELETE_STATE = 0 AND brand_id = {} AND model_name = '{}\'''' \
        .format(brand_id, model_name)

    result = execute(sql_text, True)

    return result


def update_model(model_id: int, model_name):
    sql_text = '''UPDATE model
                     SET model_name = '{}'
                   WHERE id = {}''' \
        .format(model_name, model_id)

    return execute(sql_text)
