from database.db_connection import execute
from domain.stock_detail import StockDetail


def add_stock_detail(stock_detail: StockDetail):
    sql_text = '''
                INSERT INTO stock_detail(stock_id,changed_id,changed_money,changed_number,type,update_op,update_time)
                VALUES(
                        {},
                        {},
                        {:.2f},
                        {},
                        {},
                        {},
                        '{}'
                        
                )'''.format(stock_detail.stock_id(), stock_detail.changed_id(), stock_detail.changed_money(),
                            stock_detail.changed_number(), stock_detail.type(), stock_detail.update_op(),
                            stock_detail.update_time())

    result = execute(sql_text)
    return result


def get_detail_by_buy_id(buy_id: int, stock_type=0):
    sql_text = '''
                SELECT ID,
                       STOCK_ID,
                       changed_id,
                       changed_money,
                       changed_number,
                       TYPE,
                       UPDATE_TIME,
                       UPDATE_OP
                  FROM stock_detail
                 WHERE changed_id = {}
                   AND type = {}
                 order by id
                ''' \
        .format(buy_id, stock_type)

    result = execute(sql_text)

    return result


def get_in_store_count_by_buy_id(buy_id: int) -> int:
    sql_text = '''
                SELECT COUNT(1)
                  FROM stock_detail
                 WHERE changed_id = {}
                   AND type = {}''' \
        .format(buy_id, StockDetail.by_bought())
    result = execute(sql_text)

    return result


def update_detail_type(detail_id: int, detail_type: int):
    sql_text = '''UPDATE stock_detail
                     SET type = {}
                   WHERE ID = {}'''.format(detail_type, detail_id)
    return execute(sql_text)


def update_negative_type(sale_id: int):
    sql_text = '''UPDATE stock_detail
                         SET type = {}
                       WHERE type = {}
                         AND changed_id = {}''' \
        .format(StockDetail.by_write_off(), StockDetail.by_negative(), sale_id)
    return execute(sql_text)


def get_negative_on_hand():
    sql_text = '''
                SELECT
                       s.id,
                       s.sale_date,
                       si.brand_name,
                       si.model_name,
                       s.number,
                       si.balance,
                       si.unit,
                       si.brand_id,
                       si.model_id,
                       si.id,
                       si.first_service_name,
                       si.first_service_id,
                       si.second_service_name,
                       si.second_service_id,
                       '点击销负'                  
                  FROM stock_info si,
                       Sales s,
                       stock_detail sd
                 WHERE sd.changed_id = s.id
                   AND sd.type = {}
                   AND sd.stock_id = si.id
                GROUP BY s.id,s.sale_date,si.brand_name, si.model_name, s.number, si.balance, si.unit''' \
        .format(StockDetail.by_negative())

    result = execute(sql_text)
    return result


def write_off_negative_on_hand(stock_id: int, buy_id: int, buy_price: float, sale_id: int):
    sql_text = '''
                UPDATE stock_detail
                   SET changed_id = {},
                       changed_money = {},
                       type = {}
                 WHERE stock_id = {}
                   and changed_id = {} 
                ''' \
        .format(buy_id, buy_price, StockDetail.by_write_off(), StockDetail.sold(), stock_id,
                StockDetail.by_negative(), sale_id)
    result = execute(sql_text)
    return result
