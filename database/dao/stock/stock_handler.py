from decimal import Decimal

from database.db_connection import execute
from domain.buy import BuyInfo
from domain.stock import Stock
from domain.stock_detail import StockDetail

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
                             total_cost = round(total_cost + {:.2f}, 2)
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


def get_brand_by_second_service(service_id):
    sql_text = '''SELECT BRAND_ID,
                         BRAND_NAME
                    FROM stock_info
                   WHERE second_service_id = {}
                   ORDER BY brand_name''' \
        .format(service_id)
    return execute(sql_text)


def get_model_by_second_service_and_brand(service_id, brand_id):
    sql_text = '''SELECT model_id,
                         model_name 
                    FROM stock_info
                   WHERE second_service_id = {}
                     and brand_id = {}
                  ORDER BY model_name''' \
        .format(service_id, brand_id)
    return execute(sql_text)


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
                       total_cost,
                       ifnull(sum(s.number), 0) AS sale_number
                  FROM stock_info si
                  LEFT JOIN stock_detail sd on sd.stock_id = si.id
                  LEFT JOIN Sales s on s.id = sd.changed_id and sd.type in ({}, {},{})''' \
        .format(StockDetail.by_write_off(), StockDetail.by_negative(), StockDetail.by_bought())
    if start_date != end_date:
        sql_text += ''' AND s.sale_date BETWEEN '{}' AND '{}\''''.format(start_date, end_date)
    sql_text += '\n                 WHERE 1=1'
    if stock.second_service_id():
        sql_text += '''\n                   AND si.second_service_id = {}'''.format(stock.second_service_id())
    if stock.first_service_id():
        sql_text += '''\n                   AND si.first_service_id = {}'''.format(stock.first_service_id())
    if stock.brand_name():
        sql_text += '''\n                   AND si.brand_name like '%{}%\''''.format(stock.brand_name())
    if stock.model_name():
        sql_text += '''\n                   AND si.model_name like '%{}%\''''.format(stock.model_name())

    sql_text += '''\n                  GROUP BY FIRST_SERVICE_NAME,
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
    sql_text = 'select count(1) as stock_num from stock_info where second_service_id = {}'.format(service_id)
    return execute(sql_text, True)


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


def get_calibration(state: int):
    sql_text = '''
                    SELECT
                           bi.id,
                           si.id as stock_id,
                           bi.buy_date,
                           BRAND_NAME,
                           MODEL_NAME,
                           di.value_desc,
                           si.balance,
                           bi.number,
                           si.total_cost,
                           bi.total,
                           ad.userName,
                           bi.note,
                           dic.value_desc
                      FROM stock_info si,buy_info bi, Admin ad, stock_detail sd, dictionary di,dictionary dic
                      WHERE si.id=bi.stock_id
                        AND bi.buy_type= {}
                        AND si.create_op = ad.id
                        AND sd.changed_id = bi.id
                        AND sd.stock_id = si.id
                        AND sd.type in ({},{})
                        AND dic.key_id = bi.state
                        AND dic.group_name = 'buy_state'
                        AND di.key_id = sd.type
                        AND bi.state = {}
                        AND di.group_name = 'stock_type\'''' \
        .format(BuyInfo.calibrated(), StockDetail.by_decreased(), StockDetail.by_increased(), state)
    result = execute(sql_text)
    return result


def get_all_calibration():
    sql_text = '''
                SELECT
                       bi.id,
                       si.id as stock_id,
                       bi.buy_date,
                       BRAND_NAME,
                       MODEL_NAME,
                       di.value_desc,
                       si.balance,
                       bi.number,
                       si.total_cost,
                       bi.total,
                       ad.userName,
                       bi.note,
                       dic.value_desc
                  FROM stock_info si,buy_info bi, Admin ad, stock_detail sd, dictionary di, dictionary dic
                  WHERE si.id=bi.stock_id
                    AND bi.buy_type= {}
                    AND si.create_op = ad.id
                    AND sd.changed_id = bi.id
                    AND sd.stock_id = si.id
                    AND sd.type in ({},{})
                    AND dic.key_id = bi.state
                    AND dic.group_name = 'buy_state'
                    AND di.key_id = sd.type
                    AND di.group_name = 'stock_type\'''' \
        .format(BuyInfo.calibrated(), StockDetail.by_decreased(), StockDetail.by_increased())
    result = execute(sql_text)
    return result
