from database.db_common_handler import get_all_record
from database.db_connection import execute

device_table_name = 'Device'


def get_all_device():
    return get_all_record(device_table_name, 'name', 'ASC')


def update_device_state(device_id, state):
    sql_text = "update {} set state = '{}' where id = {}".format(device_table_name, state, device_id)

    execute(sql_text)

