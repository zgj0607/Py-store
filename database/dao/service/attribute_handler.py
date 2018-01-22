from database.db_connection import execute
from domain.attribute import Attribute


def get_all_attributes():
    sql_text = '''SELECT att.id,
                         name,
                         di.value_desc required_desc,
                         display_order,
                         (CASE WHEN att.print_order = -1 THEN '不打印' ELSE att.print_order END) print_order,
                         is_required
                    FROM attributes att, dictionary di
                   WHERE delete_state = 0
                     AND att.is_required = di.key_id
                     AND di.group_name = 'is_required'
                    ORDER BY required_desc, display_order, name
                   '''
    return execute(sql_text)


def get_all_required_attributes():
    sql_text = '''SELECT id, name
                        FROM attributes
                       WHERE delete_state = 0
                         and is_required = {}
                        ORDER BY display_order, name
                       ''' \
        .format(Attribute.required())
    return execute(sql_text)


def get_count_by_name(name):
    sql_text = '''select count(1), sum(delete_state), id from attributes where name = '{}' GROUP BY id'''.format(name)
    return execute(sql_text, True)


def get_all_option_attributes():
    sql_text = '''SELECT id, name
                            FROM attributes
                           WHERE delete_state = 0
                             and is_required = {}
                            ORDER BY display_order, name
                           ''' \
        .format(Attribute.option())
    return execute(sql_text)


def add_attribute(attribute: Attribute):
    sql_text = '''
                INSERT INTO attributes(name,is_required,create_time,create_op,delete_state)
                VALUES ('{}', {}, '{}', {}, {})''' \
        .format(attribute.name(), attribute.is_required(), attribute.create_time(), attribute.create_op(),
                attribute.delete_state())
    return execute(sql_text)


def delete_attribute_logical(attribute_id: int):
    sql_text = '''
                UPDATE attributes
                   SET delete_state = 1
                 WHERE ID = {}''' \
        .format(attribute_id)
    return execute(sql_text)


def undo_delete_attribute_logical(attribute_id: int):
    sql_text = '''
                UPDATE attributes
                   SET delete_state = 0
                 WHERE ID = {}''' \
        .format(attribute_id)
    return execute(sql_text)


def delete_attribute_physical(attribute_id):
    sql_text = '''DELETE FROM attributes WHERE ID = {}'''.format(attribute_id)
    return execute(sql_text)


def update_attribute(attribute_id, name):
    sql_text = '''
                UPDATE attributes
                   SET name = '{}'
                 WHERE ID = {}''' \
        .format(name, attribute_id)
    execute(sql_text)


def get_attr_by_name(attr_name):
    sql_text = '''select id, name from attributes where name = '{}' and delete_state = 0 and is_required = {}''' \
        .format(attr_name, Attribute.option())
    return execute(sql_text, True)


def get_all_need_print_attr():
    sql_text = '''SELECT id,
                         name,
                         print_order,
                         is_required
                    FROM attributes
                   WHERE print_order > 0
                     AND delete_state = 0
                   ORDER BY print_order'''
    return execute(sql_text)
