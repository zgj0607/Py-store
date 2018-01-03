from Common.time_utils import get_now
from database.db_common_handler import delete_by_int_column, get_all_record, execute

staff_table_name = "worker"
sys_user_table_name = 'Admin'


def delete_staff_by_id(staff_id: int):
    delete_by_int_column(staff_table_name, 'id', staff_id)


def get_all_staff():
    return get_all_record(staff_table_name, 'workername', 'ASC')


def update_staff_info(name, sex, id_card_no, staff_id):
    sql_text = "update {} set workerName='{}', sex='{}', idcard='{}' where id = {}".format(staff_table_name, name, sex,
                                                                                           id_card_no, staff_id, )
    execute(sql_text)


def insert_staff_info(name, sex, id_card_no):
    time_now = get_now()
    sql_text = "INSERT INTO {}(workerName, sex, idcard, createdTime) VALUES ('{}','{}','{}','{}')".format(
        staff_table_name, name, sex,
        id_card_no, time_now)
    execute(sql_text)


def submit_staff_info(name, sex, id_card_no, staff_id):
    if staff_id:
        update_staff_info(name, sex, id_card_no, staff_id)
    else:
        insert_staff_info(name, sex, id_card_no)


def get_all_sys_user():
    return get_all_record(sys_user_table_name, 'username', 'ASC')


def insert_sys_user_info(username, password):
    time_now = get_now()
    sql_text = "INSERT INTO {}(username, pwd, createdTime) VALUES ('{}','{}','{}')".format(sys_user_table_name,
                                                                                           username, password, time_now)
    execute(sql_text)


def update_sys_user_pwd(sys_user_id, new_pwd):
    sql_text = "update {} set pwd = '{}' where id = {}".format(sys_user_table_name, new_pwd, sys_user_id)
    execute(sql_text)


def delete_sys_user_by_id(user_id: int):
    delete_by_int_column(sys_user_table_name, 'id', user_id)


def update_super_user_pwd(new_pwd, old_pwd):
    if old_pwd != get_super_user_pwd():
        return False

    update_sys_user_pwd(get_super_user_id(), new_pwd)


def get_super_user_id():
    sql_text = "select id from {} where username = 'admin'".format(sys_user_table_name)
    return execute(sql_text)[0][0]


def get_super_user_pwd():
    sql_text = "select pwd from {} where username = 'admin'".format(sys_user_table_name)
    pwd = execute(sql_text)[0][0]
    return pwd
