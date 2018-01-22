from database.db_common_handler import execute
from domain.buy import BuyInfo

buy_info_table_name = "buy_info"


def get_all_buy_info():
    sql_text = '''
                SELECT
                      bi.id,
                      bi.buy_date,                      
                      si.brand_name,
                      si.model_name,
                      bi.number,
                      si.unit,
                      bi.unit_price,
                      bi.total,
                      bi.supplier_id,
                      sl.supplier_name,
                      si.first_service_name || '-' || si.second_service_name,
                      bi.paid,
                      bi.unpaid,
                      di.value_desc,
                      bi.stock_id                
                 FROM buy_info bi, stock_info si, supplier sl, service sr, dictionary di
                WHERE bi.stock_id = si.id
                  AND bi.supplier_id = sl.id
                  AND sr.id = si.second_service_id
                  AND di.key_id = bi.buy_type
                  AND di.group_name = 'buy_type'
                  AND bi.buy_type in({},{})
                ORDER BY buy_date DESC'''.format(BuyInfo.bought(), BuyInfo.returned())

    result = execute(sql_text)

    return result


def add_buy_info(buy_info: BuyInfo) -> int:
    sql_text = '''
                INSERT INTO buy_info( 
                                STOCK_ID,
                                SUPPLIER_ID,
                                UNIT_PRICE,
                                NUMBER,
                                BUY_DATE,
                                CREATE_TIME,
                                CREATE_OP,
                                UNPAID,
                                PAID,
                                TOTAL,
                                BUY_TYPE,
                                note,
                                left_number,
                                state
                               )
              VALUES (
                      {},
                      {},
                      {:.2f},
                      {},
                      '{}',
                      '{}',
                      {},
                      {:.2f},
                      {:.2f},
                      {:.2f},
                      {},
                      '{}',
                      {},
                      {}
              )''' \
        .format(buy_info.stock_id(), buy_info.supplier_id(),
                buy_info.unit_price(), buy_info.number(), buy_info.buy_date(), buy_info.create_time(),
                buy_info.create_op(), buy_info.unpaid(), buy_info.paid(), buy_info.total(),
                buy_info.buy_type(), buy_info.note(), buy_info.left(), buy_info.state())
    new_buy_id = execute(sql_text)

    return new_buy_id


def get_history_buy_info_by_model_id(model_id: int):
    sql_text = '''
                SELECT
                       sts.brand_id,
                       sts.model_id,
                       sts.brand_name,
                       sts.model_name,
                       min_price,
                       avg_price,
                       lbi.unit_price
                  FROM (
                       SELECT
                              si.brand_id,
                              si.model_id,
                              si.brand_name,
                              si.model_name,
                              min(bi.unit_price) min_price,
                              avg(bi.unit_price) avg_price,
                              max(bi.id)         max_id
                         FROM buy_info bi,
                              stock_info si
                        WHERE bi.stock_id = si.id
                          AND si.model_id = {}
                          AND bi.buy_type = {}
                        GROUP BY si.brand_name, si.model_name
                     ) sts,
                       buy_info lbi
                 WHERE lbi.id = max_id''' \
        .format(model_id, BuyInfo.bought())

    result = execute(sql_text)

    return result


def get_history_buy_info_by_model_name_and_brand_id(brand_id: int, model_name: str):
    sql_text = '''
                SELECT
                       sts.brand_id,
                       sts.model_id,
                       sts.brand_name,
                       sts.model_name,
                       min_price,
                       avg_price,
                       lbi.unit_price
                  FROM (
                       SELECT
                              si.brand_id,
                              si.model_id,
                              si.brand_name,
                              si.model_name,
                              min(bi.unit_price) min_price,
                              avg(bi.unit_price) avg_price,
                              max(bi.id)         max_id
                         FROM buy_info bi,
                              stock_info si
                        WHERE bi.stock_id = si.id
                          AND si.model_name like '%{}%'
                          AND si.brand_id = {}
                          AND bi.buy_type = {}
                        GROUP BY si.brand_name, si.model_name
                     ) sts,
                       buy_info lbi
                 WHERE lbi.id = max_id''' \
        .format(model_name, brand_id, BuyInfo.bought())

    result = execute(sql_text)

    return result


def get_history_buy_info_by_model_name_and_brand_name(brand_name: str, model_name: str):
    sql_text = '''
                SELECT
                       sts.brand_id,
                       sts.model_id,
                       sts.brand_name,
                       sts.model_name,
                       min_price,
                       avg_price,
                       lbi.unit_price
                  FROM (
                       SELECT
                              si.brand_id,
                              si.model_id,
                              si.brand_name,
                              si.model_name,
                              min(bi.unit_price) min_price,
                              avg(bi.unit_price) avg_price,
                              max(bi.id)         max_id
                         FROM buy_info bi,
                              stock_info si
                        WHERE bi.stock_id = si.id
                          AND si.model_name like \'%{}%\'
                          AND si.brand_name like \'%{}%\'
                          AND bi.buy_type = {}
                        GROUP BY si.brand_name, si.model_name
                     ) sts,
                       buy_info lbi
                 WHERE lbi.id = max_id''' \
        .format(model_name, brand_name, BuyInfo.bought())

    result = execute(sql_text)

    return result


def get_compare_info(model_id: int):
    sql_text = '''
                SELECT
                       sp.supplier_name,
                       si.brand_name,
                       si.model_name,
                       avg(bi.unit_price) avg_price,
                       count(1)           buy_times,
                       sum(bi.number)     total_number
                  FROM buy_info bi,
                       stock_info si,
                       supplier sp
                 WHERE bi.stock_id = si.id
                   AND si.model_id = {}
                   AND bi.buy_type = {}
                   AND bi.supplier_id = sp.id
                 GROUP BY sp.supplier_name,
                          si.brand_name,
                          si.model_name
                 ORDER BY sp.supplier_name,
                          si.brand_name,
                          si.model_name
               ''' \
        .format(model_id, BuyInfo.bought())

    result = execute(sql_text)
    return result


def get_buy_info_summary_by_time(start_date: str, end_date: str):
    sql_text = '''
                SELECT
                       si.first_service_id,
                       si.second_service_id,
                       si.first_service_name,
                       si.second_service_name,
                       sum(bi.number)    total_number,
                       sum(bi.total)     total_price
                  FROM buy_info bi,
                       stock_info si
                 WHERE bi.stock_id = si.id
                   AND bi.buy_type = {}
                   AND bi.buy_date BETWEEN '{}' AND '{}'
                 GROUP BY si.first_service_id,
                          si.first_service_name,
                          si.second_service_id,
                          si.second_service_name
                 ORDER BY si.first_service_id,
                          si.first_service_name,
                          si.second_service_id,
                          si.second_service_name''' \
        .format(BuyInfo.bought(), start_date, end_date)
    result = execute(sql_text)

    return result


def get_buy_info_detail_by_time(start_time: str, end_time: str):
    sql_text = '''
                        SELECT 
                          bi.buy_date,                      
                          si.brand_name,
                          si.model_name,
                          bi.number,
                          si.unit,
                          bi.unit_price,
                          bi.total,
                          sl.supplier_name,
                          si.first_service_name || '-' || si.second_service_name,
                          bi.paid,
                          bi.unpaid,
                          di.value_desc
                          FROM buy_info bi, stock_info si, dictionary di, supplier sl
                         WHERE bi.stock_id = si.id
                           and di.key_id = bi.buy_type
                           and di.group_name = 'buy_type'
                           and sl.id = bi.supplier_id
                           and bi.buy_date BETWEEN '{}' and '{}'
                           and bi.buy_type in ({},{})
                    '''.format(start_time, end_time, BuyInfo.bought(), BuyInfo.returned())

    result = execute(sql_text)

    return result


def get_detail_info(second_srv_id: int, start_time: str, end_time: str):
    sql_text = '''
                    SELECT bi.id,
                      bi.buy_date,                      
                      si.brand_name,
                      si.model_name,
                      bi.number,
                      si.unit,
                      bi.unit_price,
                      bi.total,
                      bi.supplier_id,
                      sl.supplier_name,
                      si.first_service_name || '-' || si.second_service_name,
                      bi.paid,
                      bi.unpaid,
                      di.value_desc,
                      bi.stock_id     
                      FROM buy_info bi, stock_info si, dictionary di, supplier sl
                     WHERE si.second_service_id = {}
                       and bi.stock_id = si.id
                       and bi.buy_type = {}
                       and di.key_id = bi.buy_type
                       and di.group_name = 'buy_type'
                       and sl.id = bi.supplier_id
                       and bi.buy_date BETWEEN '{}' and '{}'
                     ORDER BY si.brand_name, si.model_name, bi.buy_date''' \
        .format(second_srv_id, BuyInfo.bought(), start_time, end_time)

    result = execute(sql_text)

    return result


def update_paid_info(buy_id, unpaid: float, paid: float, notes=''):
    sql_text = '''
                UPDATE buy_info
                   SET paid = {:.2f},
                       unpaid = {:.2f},
                       note = '{}'
                 WHERE id = {}''' \
        .format(paid, unpaid, notes, buy_id)
    result = execute(sql_text)

    return result


def get_left_gt_zero(stock_id: int):
    sql_text = '''SELECT ID, number, left_number
                    FROM buy_info 
                   WHERE stock_id = {}
                     AND left_number > 0
                     AND buy_type = {}
                   order by create_time''' \
        .format(stock_id, BuyInfo.bought())
    return execute(sql_text)


def update_left_info(buy_id: int, left_number: int):
    sql_text = '''UPDATE buy_info SET left_number = {} WHERE id = {}'''.format(left_number, buy_id)
    return execute(sql_text)


def get_unpaid_gt_zero(stock_id: int, supplier_id: int):
    sql_text = '''SELECT ID, unpaid, paid
                    FROM buy_info
                   WHERE stock_id = {}
                     AND unpaid > 0.0 
                     AND buy_type = {}
                     AND supplier_id = {}
                    order by create_time''' \
        .format(stock_id, BuyInfo.bought(), supplier_id)
    return execute(sql_text)


def update_buy_state(buy_id, state):
    sql_text = '''update buy_info set state = {} where id = {}''' \
        .format(state, buy_id)
    execute(sql_text)
