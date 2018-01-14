from Common.time_utils import get_now
from database.db_connection import execute
from domain.service_item import ServiceItem

service_table_name = 'service'


def get_all_first_level_service():
    sql_text = "SELECT id, name FROM service WHERE level = 1 ORDER BY createdTime".format(service_table_name)

    return execute(sql_text)


def get_all_second_level_service():
    sql_text = '''SELECT
                      one.id   AS father_id,
                      one.name AS father_name,
                      two.id,
                      two.name,
                      two.attribute,
                      two.attributeState
                    FROM service one, service two
                    WHERE two.father = one.id
                      AND two.level = 2
                    ORDER BY one.name, two.name'''

    return execute(sql_text)


def add_first_level_service(service_name):
    time_now = get_now()
    sql_text = '''INSERT INTO service(name, createdTime, father, level) VALUES('{}','{}',{},{})''' \
        .format(service_name, time_now, -1, 1)

    return execute(sql_text)


def add_second_level_service(service_name, father_id):
    time_now = get_now()
    sql_text = '''INSERT INTO service(name, createdTime, father, level) 
                VALUES('{}','{}',{},{})''' \
        .format(service_name, time_now, father_id, 2)

    return execute(sql_text)


def update_service(service_id, service_name):
    sql_text = '''UPDATE service SET name = '{}' where id = {}'''.format(service_name, service_id)

    execute(sql_text)


def delete_service(service_id):
    sql_text = '''DELETE FROM service where id = {}'''.format(service_id)

    execute(sql_text)


def delete_service_all_attribute(service_id):
    sql_text = '''DELETE FROM service_item where service_id = {}'''.format(service_id)
    execute(sql_text)


def get_second_service_by_father(father_id):
    sql_text = '''SELECT
                      one.id   AS father_id,
                      one.name AS father_name,
                      two.id,
                      two.name,
                      two.attribute,
                      two.attributeState
                    FROM service one, service two
                    WHERE two.father = one.id
                      AND one.id = {}
                      AND two.level = 2
                    ORDER BY one.name, two.name''' \
        .format(father_id)
    return execute(sql_text)


def get_second_service_count_by_father(father_id):
    if father_id == -1:
        return 0

    sql_text = '''select count(1) from service where father = {}'''.format(father_id)
    count = execute(sql_text)

    return count


def get_attribute_by_service(service_id: int):
    sql_text = '''
                SELECT attribute_id, attribute_name
                  FROM service_item
                 WHERE service_id = {}''' \
        .format(service_id)
    result = execute(sql_text)
    return result


def add_service_attribute(item: ServiceItem):
    sql_text = '''
                INSERT INTO service_item(service_id,attribute_id,attribute_name, create_time, create_op)
                VALUES ({},{},'{}','{}',{})''' \
        .format(item.service_id(), item.attribute_id(), item.attribute_name(), item.create_time(), item.create_op())

    return execute(sql_text)


def delete_service_attribute(service_id: int, attribute_id: int):
    sql_text = '''
                DELETE FROM service_item
                   WHERE service_id = {}
                     AND attribute_id = {}''' \
        .format(service_id, attribute_id)
    return execute(sql_text)


def get_count_by_attribute(attribute_id):
    sql_text = '''
                SELECT COUNT(1) FROM service_item where attribute_id = {}''' \
        .format(attribute_id)
    return execute(sql_text, True)


def get_service_id_by_name(name: str, father_id=-1):
    sql_text = '''select id, name 
                    from service
                    where name = '{}\'
                '''.format(name)
    if father_id and father_id != -1:
        sql_text += ''' and father = {}'''.format(father_id)
        sql_text += ''' and level = 2'''
    else:
        sql_text += ''' and father = -1'''
        sql_text += ''' and level = 1'''

    return execute(sql_text, True)
