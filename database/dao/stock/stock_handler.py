from decimal import Decimal

from database.db_connection import execute
from domain.stock import Stock

stock_table_name = 'STOCK_INFO'


def get_stock_by_model(model_id: int):
    sql_text = '''
                SELECT ID, 
                       NAME,
                       UNIT,
                       FIRST_SERVICE_ID,
                       FIRST_SERVICE_NAME,
                       SECOND_SERVICE_ID,
                       SECOND_SERVICE_NAME,
                       BRAND_ID,
                       BRAND_NAME,
                       MODEL_ID,
                       MODEL_NAME,
                       BALANCE,
                       TOTAL_COST
                  FROM stock_info
                 WHERE MODEL_ID = {}
                ''' \
        .format(model_id)

    result = execute(sql_text, True)

    return result


def add_stock_info(stock: Stock):
    sql_text = '''
                INSERT INTO stock_info(
                                        UNIT,
                                        first_service_name,
                                        first_service_id,
                                        model_id,
                                        model_name,
                                        brand_id,
                                        brand_name,
                                        name,
                                        second_service_id,
                                        second_service_name,
                                        balance,
                                        total_cost,
                                        create_time,
                                        create_op
                                        )
                VALUES(
                        '{}',
                        '{}',
                         {},
                         {},
                        '{}',
                         {},
                        '{}',
                        '{}',
                         {},
                        '{}',
                         {},
                        {:.2f},
                        '{}',
                        {}                    
                )''' \
        .format(stock.unit(), stock.first_service_name(), stock.first_service_id(), stock.model_id(),
                stock.model_name(), stock.brand_id(), stock.brand_name(), stock.name(), stock.second_service_id(),
                stock.second_service_name(), stock.balance(), stock.total_cost(), stock.create_time(),
                stock.create_op())
    new_stock_id = execute(sql_text)

    return new_stock_id


def update_stock_balance(stock_id: int, balance: int, total: Decimal):
    if stock_id:
        sql_text = '''
                      UPDATE stock_info
                         SET balance = balance + {},
                             total_cost = total_cost + {:.2f}
                       WHERE ID = {}'''.format(balance, total, stock_id)
        execute(sql_text)


def update_brand_name(stock_id: int, brand_name: str):
    sql_text = '''
                  UPDATE stock_info
                     SET name = '{}' || '-' || model_name,
                         brand_name = '{}'
                   WHERE ID = {}''' \
        .format(brand_name, brand_name, stock_id)
    execute(sql_text)


def update_brand_id(stock_id: int, brand_id: int):
    sql_text = '''
                  UPDATE stock_info
                     SET brand_id = {}
                   WHERE ID = {}''' \
        .format(brand_id, stock_id)
    execute(sql_text)


def update_model_name(stock_id: int, model_name: str):
    sql_text = '''
                      UPDATE stock_info
                         SET name = brand_name || '-' || '{}',
                             model_name = '{}'
                       WHERE ID = {}''' \
        .format(model_name, model_name, stock_id)
    execute(sql_text)


def update_model_id(stock_id: int, model_id: int):
    sql_text = '''
                  UPDATE stock_info
                     SET model_id = {}
                   WHERE ID = {}''' \
        .format(model_id, stock_id)
    execute(sql_text)


def get_stock_buy_info(stock: Stock, start_date: str, end_date: str):
    sql_text = '''
                SELECT 
                       FIRST_SERVICE_NAME,
                       SECOND_SERVICE_NAME,
                       BRAND_NAME,
                       MODEL_NAME,
                       BALANCE,
                       sum(s.number) AS sale_number
                  FROM stock_info si, Sales s, stock_detail sd
                 WHERE s.id = sd.sale_id
                   AND sd.stock_id = si.id'''
    if start_date != end_date:
        sql_text += ''' AND s.sale_date BETWEEN '{}' AND '{}\''''.format(start_date, end_date)

    if stock.second_service_id():
        sql_text += ''' AND si.second_service_id = {}'''.format(stock.second_service_id())
    if stock.first_service_id():
        sql_text += ''' AND si.first_service_id = {}'''.format(stock.first_service_id())
    if stock.brand_id():
        sql_text += ''' AND si.brand_id = {}'''.format(stock.brand_id())
    if stock.model_id():
        sql_text += ''' AND si.model_id = {}'''.format(stock.model_id())

    sql_text += ''' GROUP BY FIRST_SERVICE_NAME,
                       SECOND_SERVICE_NAME,
                       BRAND_NAME,
                       MODEL_NAME,
                       BALANCE '''
    result = execute(sql_text)
    return result


def get_stock_money():
    sql_text = '''
                SELECT
                       si.first_service_name,
                       si.second_service_name,
                       sum(CASE WHEN si.balance > 0
                                THEN si.balance
                                ELSE 0
                                END) AS balance,
                       sum(CASE WHEN si.balance > 0
                                THEN si.total_cost
                                ELSE si.total_cost
                                END) AS cost
                  FROM stock_info si
                 GROUP BY si.first_service_name, si.second_service_name'''
    result = execute(sql_text)
    return result


def get_count_by_service(service_id):
    sql_text = 'select count(1) from stock_info where second_service_id = {}'.format(service_id)
    execute(sql_text, True)


def update_first_service_name(service_id, service_name):
    sql_text = '''
                UPDATE STOCK_INFO
                   SET first_service_name = '{}'
                 WHERE first_service_id = {}''' \
        .format(service_name, service_id)
    execute(sql_text)


def update_second_service_name(service_id, service_name):
    sql_text = '''
                UPDATE STOCK_INFO
                   SET second_service_name = '{}'
                 WHERE second_service_id = {}''' \
        .format(service_name, service_id)
    execute(sql_text)
