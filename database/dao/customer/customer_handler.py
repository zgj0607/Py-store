from Common.time_utils import get_now, format_time
from database.db_connection import execute

return_visit_table = 'CallBack'


def get_return_visit_info():
    now = get_now()
    time_str = "/".join(now.split(' ')[0].split("-"))
    time_str = format_time(time_str, True)

    sql_text = '''SELECT callbackTime,phone,username,carId,id 
                    FROM CallBack
                   WHERE state='0'
                     AND callbackTime <= '{}' 
                  ORDER BY createdTime DESC ''' \
        .format(time_str)
    data = execute(sql_text)
    return data


def update_return_visit_state(return_visit_id, state):
    sql_str = "UPDATE CallBack SET state = '{}' WHERE id = {}".format(state, return_visit_id)
    execute(sql_str)


def add_return_visit_data(time_str, car_phone, car_id, car_user, today):

    sql_text = '''
              INSERT INTO {}(callbackTime, phone, carId, username, createdTime, state) 
              VALUES('{}', '{}', '{}', '{}', '{}', '{}')''' \
        .format(return_visit_table, time_str, car_phone, car_id, car_user, today, '0')
    result = execute(sql_text)

    return result
