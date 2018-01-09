from database.db_common_handler import get_all_record
from database.db_connection import execute
from domain.device import Device

device_table_name = 'Device'


def get_all_device():
    return get_all_record(device_table_name, 'name', 'ASC')


def update_device_state(device_id, state):
    sql_text = "update {} set state = '{}' where id = {}".format(device_table_name, state, device_id)

    execute(sql_text)


def add_new_device(device: Device):
    sql_text = '''
                INSERT INTO Device(name, ip, createdTime, state)
                VALUES ('{}', '{}', '{}', '{}')''' \
        .format(device.name(), device.ip(), device.create_time(), device.state())
    return execute(sql_text)


def get_device_info_by_ip(ip: str):
    sql_text = '''SELECT ID, STATE FROM Device WHERE IP = '{}\''''.format(ip)
    return execute(sql_text, True)
