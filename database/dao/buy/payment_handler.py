from common import common
from common.time_utils import get_now
from database.db_connection import execute
from domain.buy import BuyInfo
from domain.payment import Payment

payment_table_name = 'PAYMENT_DETAIL'


def add_payment_detail(payment: Payment):
    sql_text = '''
                INSERT INTO PAYMENT_DETAIL(
                                BUY_ID,
                                PAYMENT_METHOD,
                                PAID,
                                UNPAID,
                                CREATE_TIME,
                                CREATE_OP,
                                refund_type,
                                supplier_id,
                                note
                               )
                VALUES (
                         {},
                         {},
                        {:.2f},
                        {:.2f},
                        '{}',
                         {},
                         {},
                         {},
                        '{}'
                       )''' \
        .format(payment.buy_id(), payment.payment_method(), payment.paid(), payment.unpaid(),
                get_now(), common.config.login_user_info[0], payment.refund_type(), payment.supplier_id(),
                payment.note())

    result = execute(sql_text)

    return result


def get_all_arrears_info():
    sql_text = '''
                SELECT
                       id,
                       supplier_name,
                       sp.unpaid
                  FROM supplier sp
                 WHERE sp.unpaid > 0.0
                 GROUP BY id, supplier_name
                 ORDER BY supplier_name'''
    result = execute(sql_text)

    return result


def get_arrears_info_buy(supplier_id: int):
    sql_text = '''
               SELECT
                      bi.buy_date,                      
                      si.brand_name,
                      si.model_name,
                      bi.number,
                      si.unit,
                      bi.unit_price,
                      bi.total,
                      bi.paid,
                      bi.unpaid,
                      bi.id
                 FROM buy_info bi, stock_info si, supplier sl
                WHERE bi.stock_id = si.id
                  AND bi.supplier_id = sl.id
                  AND bi.unpaid > 0.0
                  AND sl.id = {}
                  AND bi.buy_type = {}
                ORDER BY buy_date''' \
        .format(supplier_id, BuyInfo.bought())
    result = execute(sql_text)

    return result
