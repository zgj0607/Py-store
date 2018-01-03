from database.db_connection import execute

model_table_name = 'model'


def get_all_model():
    sql_text = '''SELECT ID, MODEL_NAME FROM {} WHERE DELETE_STATE = 0 ORDER BY MODEL_NAME'''.format(model_table_name)
    result = execute(sql_text)

    return result


def get_model_by_id(model_id: int):
    sql_text = '''SELECT ID, MODEL_NAME FROM {} WHERE DELETE_STATE = 0 AND ID = {} ORDER BY MODEL_NAME'''.format(model_table_name, model_id)
    result = execute(sql_text)

    return result


def get_model_by_brand(brand_id: int):
    sql_text = '''SELECT ID, MODEL_NAME FROM {} WHERE DELETE_STATE = 0 AND brand_id = {} ORDER BY MODEL_NAME'''.format(model_table_name, brand_id)
    result = execute(sql_text)

    return result