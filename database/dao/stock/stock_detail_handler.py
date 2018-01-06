from database.db_connection import execute
from domain.stock_detail import StockDetail


def add_stock_detail(stock_detail: StockDetail):
    sql_text = '''
                INSERT INTO stock_detail(stock_id,buy_id,buy_price,sale_id,sale_price,state,type,update_op,update_time)
                VALUES(
                        {},
                        {},
                        {:.2f},
                        {},
                        {:.2f},
                        {},
                        {},
                        {},
                        '{}'
                        
                )'''.format(stock_detail.stock_id(), stock_detail.buy_id(), stock_detail.buy_price(),
                            stock_detail.sale_id(), stock_detail.sale_price(), stock_detail.state(),
                            stock_detail.type(), stock_detail.update_op(), stock_detail.update_time())

    result = execute(sql_text)
    return result


def get_detail_by_buy_id(buy_id: int, stock_state=0):
    sql_text = '''
                SELECT ID,
                       STOCK_ID,
                       BUY_ID,
                       BUY_PRICE,
                       SALE_ID,
                       SALE_PRICE,
                       STATE,
                       TYPE,
                       UPDATE_TIME,
                       UPDATE_OP
                  FROM stock_detail
                 WHERE buy_id = {}
                   AND STATE = {}
                 order by id
                ''' \
        .format(buy_id, stock_state)

    result = execute(sql_text)

    return result


def get_in_store_count_by_buy_id(buy_id: int) -> int:
    sql_text = '''
                SELECT COUNT(1)
                  FROM stock_detail
                 WHERE buy_id = {}
                   AND STATE = {}''' \
        .format(buy_id, StockDetail.in_store())
    result = execute(sql_text)

    return result


def update_detail_state(detail_id: int, state: int):
    sql_text = '''UPDATE stock_detail
                     SET STATE = {}
                   WHERE ID = {}'''.format(state, detail_id)
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
                       si.second_service_id                   
                  FROM stock_info si,
                       Sales s,
                       stock_detail sd
                 WHERE sd.sale_id = s.id
                   AND sd.state = {}
                   AND sd.stock_id = si.id
                GROUP BY s.id,s.sale_date,si.brand_name, si.model_name, s.number, si.balance, si.unit''' \
        .format(StockDetail.under_write_off())

    result = execute(sql_text)
    return result


def write_off_negative_on_hand(stock_id: int, buy_id: int, buy_price: float, sale_id: int):
    sql_text = '''
                UPDATE stock_detail
                   SET buy_id = {},
                       buy_price = {},
                       type = {},
                       state = {}
                 WHERE stock_id = {}
                   and state = {}
                   and sale_id = {} 
                ''' \
        .format(buy_id, buy_price, StockDetail.by_write_off(), StockDetail.sold(), stock_id,
                StockDetail.under_write_off(), sale_id)
    result = execute(sql_text)
    return result
