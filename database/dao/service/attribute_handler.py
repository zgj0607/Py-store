from database.db_connection import execute
from domain.attribute import Attribute


def get_all_attributes():
    sql_text = '''SELECT id, name,(CASE WHEN is_required = 0 THEN '选填' ELSE '必填' END)
                    FROM Attributes
                   WHERE delete_state = 0
                    ORDER BY name
                   '''
    return execute(sql_text)


def get_all_required_attributes():
    sql_text = '''SELECT id, name
                        FROM Attributes
                       WHERE delete_state = 0
                         and is_required = {}
                        ORDER BY name
                       ''' \
        .format(Attribute.required())
    return execute(sql_text)


def get_count_by_name(name):
    sql_text = '''select count(1) from Attributes where name = '{}\''''.format(name)
    return execute(sql_text)[0][0]


def get_all_option_attributes():
    sql_text = '''SELECT id, name
                            FROM Attributes
                           WHERE delete_state = 0
                             and is_required = {}
                            ORDER BY name
                           ''' \
        .format(Attribute.option())
    return execute(sql_text)


def add_attribute(attribute: Attribute):
    sql_text = '''
                INSERT INTO Attributes(name,is_required,create_time,create_op,delete_state)
                VALUES ('{}', {}, '{}', {}, {})''' \
        .format(attribute.name(), attribute.is_required(), attribute.create_time(), attribute.create_op(),
                attribute.delete_state())
    return execute(sql_text)


def delete_attribute(attribute_id: int):
    sql_text = '''
                UPDATE ATTRIBUTES
                   SET delete_state = 1
                 WHERE ID = {}''' \
        .format(attribute_id)
    return execute(sql_text)
