from database.db_common_handler import execute
from domain.buy import BuyInfo

buy_info_table_name = "buy_info"


def get_all_buy_info():
    sql_text = '''
                SELECT
                      bi.id,
                      bi.buy_date,
                      si.model_name,
                      si.brand_name,
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
                      (case when bi.rela_buy_id=0 then '-' else rela_buy_id end) as rela_buy,
                      bi.stock_id                
                 FROM buy_info bi, stock_info si, supplier sl, service sr, dictionary di
                WHERE bi.stock_id = si.id
                  AND bi.supplier_id = sl.id
                  AND sr.id = si.second_service_id
                  AND di.key_id = bi.buy_type
                  AND di.group_name = 'buy_type'
                ORDER BY buy_date DESC'''

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
                                rela_buy_id,
                                BUY_TYPE,
                                NOTES
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
                      {},
                      '{}'                                       
              )''' \
        .format(buy_info.stock_id(), buy_info.supplier_id(),
                buy_info.unit_price(), buy_info.number(), buy_info.buy_date(), buy_info.create_time(),
                buy_info.create_op(), buy_info.unpaid(), buy_info.paid(), buy_info.total(), buy_info.rela_buy_id(),
                buy_info.buy_type(), buy_info.notes())
    new_buy_id = execute(sql_text)

    return new_buy_id
