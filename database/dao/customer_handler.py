from Common.StaticFunc import get_now, format_time
from database.db_connection import execute


def check_return_visit_info():
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
