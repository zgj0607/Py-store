from common import common, time_utils
from database.dao.buy import payment_handler
from database.dao.supplier import supplier_handler
from domain.payment import Payment


def get_all_supplier():
    suppliers = []
    for supplier in supplier_handler.get_all_supplier():
        suppliers.append(supplier[1])
    return suppliers


def get_supplier_by_name(name):
    supplier_in_db = supplier_handler.get_supplier_by_name(name)
    if supplier_in_db:
        return supplier_in_db[0]
    else:
        return supplier_handler.add_supplier(name)


def add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment_method, is_return=False, note=''):
    payment = Payment()
    payment.buy_id(buy_id)
    payment.supplier_id(supplier_id)
    payment.payment_method(payment_method)
    payment.paid(paid)
    payment.unpaid(unpaid)
    payment.create_op(common.config.login_user_info[0])
    payment.create_time(time_utils.get_now())
    payment.note(note)

    if is_return:
        payment.refund_type(Payment.returned())
    else:
        payment.refund_type(Payment.payoff())

    payment_handler.add_payment_detail(payment)

    if unpaid:
        supplier_handler.update_supplier_unpaid(supplier_id, unpaid)
