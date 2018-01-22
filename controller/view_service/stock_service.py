from decimal import Decimal

from common import time_utils, common, config
from controller.view_service import brand_and_model_service, buy_service
from database.dao.service import service_handler
from database.dao.stock import stock_handler, stock_detail_handler
from domain.stock import Stock
from domain.stock_detail import StockDetail


def update_stock_info(stock_id: int, balance: int, total: Decimal):
    stock_handler.update_stock_balance(stock_id, balance, total)


def add_stock_detail(stock_id: int, changed_id: int, changed_money: float, change_number: int, change_type: int):
    stock_detail = StockDetail()
    stock_detail.changed_id(changed_id)
    stock_detail.changed_money(abs(changed_money))
    stock_detail.changed_number(abs(change_number))
    stock_detail.stock_id(stock_id)
    stock_detail.type(change_type)

    stock_detail.update_time(time_utils.get_now()).update_op(common.config.login_user_info[0])
    stock_detail_handler.add_stock_detail(stock_detail)


def add_stock_info(model, brand, model_id, brand_id, unit, second_service_id):
    second_service = service_handler.get_service_by_id(second_service_id)

    stock_info = Stock()

    stock_info.model_id(model_id).model_name(model)
    stock_info.brand_id(brand_id).brand_name(brand)
    stock_info.first_service_id(second_service['father_id']).first_service_name(second_service['father_name'])
    stock_info.second_service_id(second_service_id).second_service_name(second_service['name'])
    stock_info.unit(unit)
    stock_info.name(brand + '-' + model)
    stock_info.create_op(config.login_user_info[0]).create_time(time_utils.get_now())

    stock_id = stock_handler.add_stock_info(stock_info)
    stock_info.id(stock_id)
    return stock_info


def get_stock_by_model(model_id: int):
    return stock_handler.get_stock_by_model(model_id)


def refresh_stock_info(sale_id: int, brand: str, model: str, sale_number: int, unit: str, second_service_id: int):
    if not brand or not model:
        return
    brand_id = brand_and_model_service.get_brand_by_name(brand)
    model_id = brand_and_model_service.get_model_by_name(brand_id, model)
    stock_info = get_stock_by_model(model_id)
    if not stock_info:
        stock_info = add_stock_info(model, brand, model_id, brand_id, unit, second_service_id)
        stock_id = stock_info.id()
        balance_in_db = stock_info.balance()
        total_cost_in_db = stock_info.total_cost()
    else:
        stock_id = stock_info['id']
        balance_in_db = stock_info['balance']
        total_cost_in_db = stock_info['total_cost']
        unit = stock_info['unit']

    change_balance = 0 - sale_number

    if not balance_in_db:
        changed_cost = 0.0
        change_type = StockDetail.by_negative()
    else:
        changed_cost = 0.0 - round(abs(total_cost_in_db / balance_in_db) * sale_number, 2)
        change_type = StockDetail.by_sold()

    # 更新库存量和库存金额
    update_stock_info(stock_id, change_balance, changed_cost)

    # 新增库存明细表
    add_stock_detail(stock_id, sale_id, changed_cost, sale_number, change_type)

    # 更新进货批次中的剩余量
    buy_service.decrease_buy_left(stock_id, sale_number)
