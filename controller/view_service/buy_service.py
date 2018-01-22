from decimal import Decimal

from common import time_utils, common
from controller.view_service import supplier_service
from database.dao.buy import buy_handler
from domain.buy import BuyInfo


def decrease_buy_left(stock_id, number):
    buy_of_left_gt_zero = buy_handler.get_left_gt_zero(stock_id)
    if not buy_of_left_gt_zero:
        return

    number = abs(number)
    for left_info in buy_of_left_gt_zero:
        left_in_db = left_info['left_number']
        if number >= left_in_db:
            new_left = 0
            number -= left_in_db
        else:
            new_left = left_in_db - number
            number = 0
        buy_handler.update_left_info(left_info['id'], new_left)

        if not number:
            return


def increase_buy_left(stock_id, number):
    buy_of_left_gt_zero = buy_handler.get_left_gt_zero(stock_id)
    if not buy_of_left_gt_zero:
        return

    number = abs(number)
    for left_info in buy_of_left_gt_zero:
        left_in_db = left_info['left_number']
        number_in_db = left_info['number']

        can_increased_number = number_in_db - left_in_db
        if not can_increased_number:
            continue

        if number >= can_increased_number:
            new_left = number_in_db
            number -= can_increased_number
        else:
            new_left = left_in_db + number
            number = 0
        buy_handler.update_left_info(left_info['id'], new_left)

        if not number:
            return


def update_buy_unpaid(stock_id: int, total: Decimal, supplier_id: int, payment: int):
    total = abs(total)

    for unpaid_info in buy_handler.get_unpaid_gt_zero(stock_id, supplier_id):
        unpaid_in_db = Decimal(unpaid_info['unpaid'])
        if total >= unpaid_in_db:
            new_unpaid = 0.0
            now_paid = unpaid_in_db
            total -= unpaid_in_db
        else:
            new_unpaid = unpaid_in_db - total
            now_paid = total
            total = 0.0
        total_paid = Decimal(unpaid_info['paid']) + now_paid

        buy_id = unpaid_info['id']
        buy_handler.update_paid_info(buy_id, new_unpaid, total_paid)
        supplier_service.add_supplier_payment_detail(buy_id, supplier_id, now_paid, new_unpaid, payment, True, '退货抵销')

        if not total:
            return


def add_buy_info(stock_id, supplier_id, price, number, buy_date, unpaid, paid, total, payment, note, left_number,
                 op=None, buy_type=None, state=0):
    buy_info = BuyInfo()
    buy_info.buy_date(buy_date)
    buy_info.stock_id(stock_id)
    buy_info.supplier_id(supplier_id)
    buy_info.unit_price(price)
    buy_info.payment_method(payment)

    if buy_type == BuyInfo.calibrated():
        buy_info.number(number)
        buy_info.total(total)
    else:
        buy_info.number(abs(number))
        buy_info.total(abs(total))

    create_time = time_utils.get_now()
    buy_info.create_time(create_time)
    if not op:
        create_op = common.config.login_user_info[0]
    else:
        create_op = op
    buy_info.create_op(create_op)

    buy_info.paid(abs(paid))
    buy_info.unpaid(abs(unpaid))

    buy_info.note(note)
    # 判断是进货还是退货
    if not buy_type:
        if number < 0:
            buy_info.buy_type(BuyInfo.returned())
            left_number = 0
        else:
            buy_info.buy_type(BuyInfo.bought())
    else:
        buy_info.buy_type(buy_type)

    if state:
        buy_info.state(state)

    buy_info.left(left_number)

    return buy_handler.add_buy_info(buy_info)
