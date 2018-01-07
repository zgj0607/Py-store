from Common import Common
from Common.time_utils import get_now
from database.db_connection import execute

payment_table_name = 'PAYMENT_DETAIL'


def add_payment_detail(payment):
    sql_text = '''
                INSERT INTO PAYMENT_DETAIL(
                                BUY_ID,
                                PAYMENT_METHOD,
                                PAID,
                                UNPAID,
                                CREATE_TIME,
                                CREATE_OP,
                                refund_type
                               )
                VALUES (
                         {},
                         {},
                        {:.2f},
                        {:.2f},
                        '{}',
                         {},
                         {}
                       )''' \
        .format(payment.buy_id(), payment.payment_method(), payment.paid(), payment.unpaid(),
                get_now(), Common.config.login_user_info[0], payment.refund_type())

    result = execute(sql_text)

    return result


def get_all_arrears_info():
    sql_text = '''
                SELECT buy_id, suppler_id, suppler_name, sum(unpaid)
                  FROM buy_info bi, supplier sp
                 WHERE sp.id = bi.supplier_id
                   AND bi.unpaid > 0
                GROUP BY  buy_id, suppler_id, suppler_name
                 ORDER BY supplier_name'''
    result = execute(sql_text)

    return result
