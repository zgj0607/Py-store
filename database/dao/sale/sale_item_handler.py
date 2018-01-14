from database.db_connection import execute


def update_item_id(old_attr_id, new_attr_id):
    sql_text = '''
                UPDATE sales_item
                   SET attribute_id = {}
                 WHERE attribute_id = {}''' \
        .format(new_attr_id, old_attr_id)
    execute(sql_text)
