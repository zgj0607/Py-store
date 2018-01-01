from database.db_connection import execute


def delete_by_str_column(table_name: str, column_name: str, column_value: str):
    sql_text = "DELETE FROM {} WHERE {} = '{}'".format(table_name, column_name, column_value)

    execute(sql_text)


def delete_by_int_column(table_name: str, column_name: str, column_value: int):
    sql_text = "DELETE FROM {} WHERE {} = '{}'".format(table_name, column_name, column_value)
    execute(sql_text)


def get_all_record(table_name, order_by_column, order_by_type):
    sql_text = 'SELECT * FROM {} ORDER BY {} {}'.format(table_name, order_by_column, order_by_type)
    return execute(sql_text)
