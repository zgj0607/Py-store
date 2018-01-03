from database.db_connection import execute

model_table_name = 'brand'


def get_all_brand():
    sql_text = '''SELECT ID, BRAND_NAME FROM {} WHERE DELETE_STATE = 0 ORDER BY BRAND_NAME'''.format(model_table_name)

    result = execute(sql_text)
    return result


def get_brand_by_id(model_id: int):
    sql_text = '''SELECT ID, BRAND_NAME FROM {} WHERE DELETE_STATE = 0 AND ID = {} ORDER BY BRAND_NAME'''.format(model_table_name, model_id)

    result = execute(sql_text)

    return result
