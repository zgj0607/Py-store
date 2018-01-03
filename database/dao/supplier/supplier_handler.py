from database.db_connection import execute

supplier_table_name = 'supplier'


def get_all_supplier():
    sql_text = '''SELECT ID, SUPPLIER_NAME FROM {} WHERE DELETE_STATE = 0 ORDER BY SUPPLIER_NAME''' \
        .format(supplier_table_name)

    result = execute(sql_text)

    return result
