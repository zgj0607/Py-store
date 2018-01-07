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

