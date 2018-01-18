from database.db_connection import execute


def get_key_and_value_by_group_name(group_name: str):
    sql_text = '''
                SELECT key_id,
                       value_desc
                  FROM dictionary
                 WHERE group_name = '{}'
                 GROUP BY value_desc''' \
        .format(group_name)
    return execute(sql_text)


def add_dictionary(key_id: int, value_desc: str, group_name):
    sql_text = '''INSERT INTO dictionary(key_id,
                                         value_desc,
                                         group_name)
                  VALUES({},'{}', '{}')''' \
        .format(key_id, value_desc, group_name)
    return execute(sql_text)


def get_max_key_id_by_group_name(group_name: str):
    sql_text = '''SELECT ifnull(MAX(KEY_ID),0) as key_id FROM dictionary WHERE group_name = '{}\''''.format(group_name)
    return execute(sql_text, True)['key_id']


def get_count_by_group_and_value(group_name: str, value_desc: str):
    sql_text = '''SELECT count(1) as num
                    FROM dictionary 
                   WHERE value_desc = '{}'
                     and group_name = '{}\'''' \
        .format(value_desc, group_name)
    return execute(sql_text, True)['num']
