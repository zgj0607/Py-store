from Common.time_utils import get_now, format_time
from database.db_connection import execute
from domain.customer import Customer
from domain.return_visit import ReturnVisit

return_visit_table = 'CallBack'


def get_return_visit_info():
    now = get_now()
    time_str = "/".join(now.split(' ')[0].split("-"))
    time_str = format_time(time_str, True)

    sql_text = '''SELECT id,username,carId,phone,next_visit_time
                    FROM return_visit
                   WHERE state={}
                     AND next_visit_time <= '{}' 
                  ORDER BY create_time DESC ''' \
        .format(ReturnVisit.unvisited(), time_str)
    data = execute(sql_text)
    return data


def update_return_visit_state(return_visit_id, state):
    sql_str = "UPDATE return_visit SET state = {} WHERE id = {}".format(state, return_visit_id)
    execute(sql_str)


def add_return_visit_data(time_str, car_phone, car_id, car_user, today):
    sql_text = '''
              INSERT INTO return_visit(next_visit_time, phone, carId, username, create_time, state) 
              VALUES('{}', '{}', '{}', '{}', '{}', {})''' \
        .format(return_visit_table, time_str, car_phone, car_id, car_user, today, ReturnVisit.unvisited())
    result = execute(sql_text)

    return result


def get_customer_by_key(key, value):
    sql_text = "SELECT id,userName,carModel,carPhone,carId FROM User WHERE {}='{}' ORDER BY createdTime DESC " \
        .format(key, value)
    data = execute(sql_text)
    return data


def check_customer(phone, car_id):
    sql_text = "SELECT id FROM User WHERE carPhone='{}' and carId='{}' ORDER BY createdTime DESC ".format(phone,
                                                                                                          car_id)
    data = execute(sql_text)
    return data


def get_like_customer_by_key(key, value):
    sql_text = '''SELECT id,userName,carModel,carPhone,carId 
                    FROM User
                   WHERE {} like '%{}%'
                   ORDER BY createdTime DESC''' \
        .format(key, value)
    data = execute(sql_text)
    return data


def update_customer_by_car_id(customer: Customer):
    sql_text = '''UPDATE user
                     set carModel = '{}',
                         carPhone = '{',
                         userName = '{}'
                    WHERE carId = '{}\'''' \
        .format(customer.car_model(), customer.phone(), customer.username(), customer.car_id())

    execute(sql_text)


def add_customer(customer: Customer):
    sql_text = '''
                INSERT INTO User(userName, carId, carModel, carPhone, createdTime)
                VALUES ('{}', '{}', '{}', '{}', '{}')''' \
        .format(customer.username(), customer.car_id(), customer.car_model(), customer.phone(), customer.create_time())
    return execute(sql_text)
