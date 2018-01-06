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

    result = execute(sql_text)

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
                                        total_cost
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
                        {:.2f}                      
                )''' \
        .format(stock.unit(), stock.first_service_name(), stock.first_service_id(), stock.model_id(),
                stock.model_name(), stock.brand_id(), stock.brand_name(), stock.name(), stock.second_service_id(),
                stock.second_service_name(), stock.balance(), stock.total_cost())
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


def update_model_name(stock_id: int, model_name: str):
    sql_text = '''
                      UPDATE stock_info
                         SET name = brand_name || '-' || '{}',
                             model_name = '{}'
                       WHERE ID = {}''' \
        .format(model_name, model_name, stock_id)
    execute(sql_text)
