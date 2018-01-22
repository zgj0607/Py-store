import logging

from tornado.concurrent import run_on_executor

from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts
from controller.web.base_handler import BaseHandler
from database.dao.service import service_handler
from database.dao.stock import stock_handler

logger = logging.getLogger(__name__)


class ServiceHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(ServiceHandler, self).__init__(application, request, **kwargs)
        self.func = self.ApiService

    @run_on_executor
    def ApiService(self, keyword, para_data):
        try:
            if self.request.method == "GET":
                if keyword == "one":
                    second_services = service_handler.get_all_first_level_service()
                    send_data = list()
                    for data in second_services:
                        send_data.append({
                            "oneMenuId": data[0],
                            "name": data[1]
                        })
                    return set_return_dicts(send_data)

                elif keyword == "two":
                    first_service_id = para_data.get("oneMenuId")
                    second_services = service_handler.get_second_service_by_father(first_service_id)
                    send_data = list()
                    for data in second_services:
                        second_service_id = data[2]
                        second_service_name = data[3]
                        attribute_dict = {}
                        for attr in service_handler.get_attribute_by_service(second_service_id):
                            attribute_dict[attr[1]] = '1'

                        send_data.append({
                            "twoMenuId": second_service_id,
                            "name": second_service_name,
                            "attribute": attribute_dict,
                        })
                    return set_return_dicts(send_data)

                elif keyword == 'brand':
                    second_service_id = para_data.get['second_service_id']
                    brands = []
                    for brand in stock_handler.get_brand_by_second_service(second_service_id):
                        brands.append({'name': brand['brand_name'], 'id': brand['brand_id']})
                    send_data = {
                        'second_service_id': second_service_id,
                        'brands': brands
                    }
                    return set_return_dicts(send_data)

                elif keyword == 'model':
                    second_service_id = para_data.get['second_service_id']
                    brand_id = para_data.get['brand_id']
                    models = []
                    for model in stock_handler.get_model_by_second_service_and_brand(second_service_id, brand_id):
                        models.append(({'name': model['model_name'], 'id': model['model_id']}))
                    send_data = {
                        'second_service_id': second_service_id,
                        'models': models
                    }
                    return set_return_dicts(send_data)

                elif keyword == 'balance':
                    model_id = para_data.get['model_id']
                    stock = stock_handler.get_stock_by_model(model_id)
                    if stock:
                        balance = stock['balance']
                    else:
                        balance = 0
                    send_data = {
                        'model_id': model_id,
                        'balance': balance
                    }

                    return set_return_dicts(send_data)

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])
