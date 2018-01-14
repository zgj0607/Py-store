from database.db_connection import execute


def update_item_id(old_attr_id, new_attr_id):
    sql_text = '''
                UPDATE sales_item
                   SET attribute_id = {}
                 WHERE attribute_id = {}''' \
        .format(new_attr_id, old_attr_id)
    execute(sql_text)


def get_item_info_buy_sale_id(sale_id):
    sql_text = '''
                select sale_id,
                       si.attribute_id,
                       attr.name,
                       si.attribute_value
                  from sales_item si, attributes attr
                where sale_id = '{}'
                and attr.id = si.attribute_id''' \
        .format(sale_id)
    return execute(sql_text)


def add_sale_item(sale_id, attr_id, attr_value):
    sql_text = '''INSERT INTO sales_item(sale_id, attribute_id, attribute_value)
                  VALUES ('{}', {}, '{}')
                ''' \
        .format(sale_id, attr_id, attr_value)
    return execute(sql_text)
