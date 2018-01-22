# -*- coding: utf-8 -*-

import json
import logging
import traceback
from collections import OrderedDict
from datetime import datetime

import requests
from tornado.concurrent import run_on_executor

from common import config
from common.common import SocketServer, cncurrency
from common.config import domain
from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts, get_uuid1
from controller.view_service import stock_service
from controller.view_service.printer_service import Printer
from controller.web.base_handler import BaseHandler
from database.dao.customer import customer_handler
from database.dao.sale import sale_handler, sale_item_handler
from database.dao.sale.sale_handler import get_sale_info_by_one_key, get_sale_order_no
from database.dao.service import service_handler, attribute_handler
from view.utils import db_transaction_util

logger = logging.getLogger(__name__)


class OrderHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(OrderHandler, self).__init__(application, request, **kwargs)
        self.func = self.order

    def preview_html(self, get_data, get_height=False):
        if get_data.get("createdTime"):
            today = get_data.get("createdTime")
        else:
            today = datetime.now()

        if get_data.get("orderNo"):
            order_no = get_data.get("orderNo")
        else:
            order_no = sale_handler.get_sale_order_no(today)

        parameter = get_data.get("parameter", [])
        if type(parameter) == str:
            parameter = json.loads(parameter)

        car_id = get_data.pop("carId", "1")
        car_phone = get_data.pop("carPhone", "1")
        store_name = get_data.pop("pcSign", "1")

        try:
            if not self.connect:
                raise ApiException(ErrorCode.ErrorRequest)
            code = config.get_local_register_code()
            url = domain + "store/api/detail?code={}".format(code)
            req = requests.get(url=url)
            result_data = json.loads(req.text)
        except Exception as exception:
            logger.error(exception)
            store = config.get_local_store_info()

            result_data = {
                'data': {
                    "pcId": store.id(),
                    "pcPhone": store.phone(),
                    "pcAddress": store.address(),
                    "pcSign": store.name(),
                },
                'code': 200
            }
        if result_data.get("code") != 200:
            store_address = ""
            store_phone = ""
        else:
            store_address = result_data.get("data").get("pcAddress", "")
            store_phone = result_data.get("data").get("pcPhone", "")

        font_size = config.get_print_font_size()

        header = """<html>
    <head>
        <style>
            table{
                background-color:#000000
            }
            .linetd{
                text-align: center;
                border:solid 1px #000;
                width: 820px;
                color: red;
                height: 30px;
            }
            .halftd{
                border:solid 1px #000;
                width: 410px;
            }
            #content{
                text-align: center;
                border:solid 1px #000;
                position: relative;
                top: 50%;
                transform: translateY(-50%);
            }
            td{
                padding:2px;
                align:center;
                border:1px solid black;
                background-color:#ffffff
            }
            *{
                font-size: """ + str(font_size) + "pt;}" + "\n            .bigWord{font-size: " + str(
            font_size * 1.5) + "pt;\n            }" + "\n        </style>\n   </head>"

        # 总长度要减去备注和名称，因为名称长度另外设置，备注不打印
        td_width = 19
        logger.info('begin body')
        body = """\n    <body >
        <div style="width:100%;text-align:center">
            <table width=100% CELLPADDING="0" CELLSPACING="1" border="0">
                <tr>
                    <td class="bigWord" align="center" colspan="100" width="100%">
                        {storeName}
                    </td>
                </tr>
                <tr>
                    <td colspan="50">车牌号：{carId}</td>
                    <td colspan="50">销售日期：{createdTime}</td>
                </tr>
                <tr>
                    <td colspan="50">客户电话：{carPhone}</td>
                    <td colspan="50">销售单号：<span style="">{orderNo}</span></td>
                </tr>
                <tr>
                    <td colspan="100" height="20px"> </td>
                </tr>""" \
            .format(storeName=store_name, carId=car_id, createdTime=today.strftime("%Y-%m-%d %H:%M:%S"),
                    carPhone=car_phone, orderNo=order_no)

        logger.info('begin make attribute')
        target_content = ""
        sequence = 1
        total_price = 0
        page_height = 100
        td_indent = '''                    '''
        tr_indent = '''                '''
        for order in parameter:
            attribute = order.get("attribute")
            base_height = 180

            # 按照系统给定的打印顺序排序
            need_print_attributes = attribute_handler.get_all_need_print_attr()

            # 拼接打印预览的表格头部和值
            key_td_str = td_indent + '''<td colspan=''' + str(td_width) + '''" align="center">{key}</td>'''
            value_td_str = td_indent + '''<td colspan="''' + str(td_width) + '''" align="center">{value}</td>'''
            first_key_str = td_indent + '''<td colspan="5" align="center">序</td>'''
            first_value_str = td_indent + '''<td rowspan="{seq_row_span}" colspan="5" align="center">{seq}</td>'''

            value_td_list = [key_td_str.format(key=order.get("project"))]
            key_td_list = [value_td_str.format(value='名称')]
            for print_attr in need_print_attributes:
                key = print_attr['name']
                value = attribute.get(key, '')

                # 是否必须显示，如果是，即便为空也要打印，否则不为空且值不为'-'才打印
                is_required = print_attr['is_required']
                if not is_required and (not value or value == '-') or print_attr['print_order'] == 1000:
                    continue

                key_td_list.append(key_td_str.format(key=key))
                value_td_list.append(value_td_str.format(value=value))

            row_num = len(key_td_list)

            # 补齐最后一行空缺的单元格
            for i in range(5 - row_num % 5):
                key_td_list.append(key_td_str.format(key=''))
                value_td_list.append(value_td_str.format(value=''))

            # 序号列合并行数
            seq_row_span = int(row_num / 5 + 1) * 2

            # 打印所需的高度
            page_height += int(row_num / 5 + 1) * 60 + base_height

            # 拼凑消费项目打印所需HTML
            logger.info('拼凑消费项目打印所需HTML')
            first_value_str = first_value_str.format(seq_row_span=seq_row_span, seq=sequence)
            key_content = tr_indent + '''<tr style="font-weight:800">\n'''
            value_content = tr_indent + '''<tr style="font-weight:800">\n'''
            for index, td_str in enumerate(key_td_list):

                if not index:
                    key_content += first_key_str + '\n'
                    value_content += first_value_str + '\n'

                key_content += td_str + '\n'
                value_content += value_td_list[index] + '\n'

                if not (index + 1) % 5:
                    target_content += key_content + tr_indent + '''</tr>\n'''
                    target_content += value_content + tr_indent + '''</tr>\n'''
                    key_content = tr_indent + '''<tr style="font-weight:800">\n'''
                    value_content = tr_indent + '''<tr style="font-weight:800">\n'''

            separator = tr_indent + """<tr><td colspan="100" height="20px"> </td></tr>\n"""
            total_price_content = tr_indent + """<tr><td colspan="95">总价：{total_price}</td></tr>\n""" \
                .format(total_price=attribute.get('总价', ""))

            target_content += total_price_content
            target_content += separator

            sequence += 1
            total_price += float(attribute.get('总价', 0))

        logger.info('end make attribute')
        total_price = str(total_price)
        cn = cncurrency(total_price)

        logger.info('拼凑消费项目总计消费HTML')
        foot = tr_indent + '''<tr>
                    <td style="height:35px" colspan="70">合计人名币（大写）：{cn}</td>
                    <td style="height:35px"  colspan="30">小写：{total_price}</td>
                </tr>
                <tr>
                    <td colspan="30">{storeName}</td>
                    <td colspan="35">地址：{pcAddress}</td>
                    <td colspan="35">联系电话：{pcPhone}</td>
                </tr>
            </table>
        </div>
    </body>
</html>''' \
            .format(cn=cn, total_price=total_price, storeName=store_name, pcPhone=store_phone, pcAddress=store_address)

        html = header + body + target_content + foot
        logger.info('add str end')
        if get_height:
            return html, page_height
        else:
            return html

    @run_on_executor
    def order(self, keyword, para_data):
        try:
            if self.request.method == 'POST':
                if keyword == "add":
                    today = datetime.now()

                    order_no = get_sale_order_no(today)

                    para_data["orderNo"] = order_no
                    para_data["createdTime"] = today
                    print(keyword)
                    try:
                        car_user = para_data.get("carUser")
                        user_id = para_data.get("userId")
                        worker_id = para_data.get("workerId")
                        pc_id = para_data.get("pcId")
                        car_phone = para_data.get("carPhone")
                        car_model = para_data.get("carModel")
                        car_id = para_data.get("carId")
                        pc_sign = para_data.get("pcSign")
                        worker_name = para_data.get("workerName")
                        order_check_id = get_uuid1()
                        save_data = {
                            'createdTime': para_data.get("createdTime").strftime("%Y-%m-%d %H:%M:%S"),
                            'userId': user_id,
                            'pcId': pc_id,
                            'pcSign': pc_sign,
                            'carId': car_id,
                            'workerName': worker_name,
                            'workerId': worker_id,
                            'carUser': car_user,
                            'carPhone': car_phone,
                            'carModel': car_model,
                            "orderNo": order_no,
                            "orderCheckId": order_check_id,
                            'code': config.get_local_register_code(),

                        }

                        parameter = para_data.get("parameter", [])
                        if type(parameter) == str:
                            parameter = json.loads(parameter)

                        page = 0
                        for data in parameter:
                            page += 1
                            order_id = get_uuid1()

                            services = data.get('project')
                            services = services.split('-')
                            first_service_name = services[0]
                            second_service_name = services[1]

                            first_service_id = service_handler.get_service_id_by_name(first_service_name)[0]
                            second_service_id = service_handler.get_service_id_by_name(second_service_name,
                                                                                       first_service_id)[0]

                            attributes = data.get('attribute')
                            logger.info(attributes)
                            try:
                                unit = attributes.get('单位', '')
                                unit_price = float(attributes.get('单价', ''))
                                number = int(attributes.get('数量', ''))
                                subtotal = float(attributes.get('小计', ''))
                                total = float(attributes.get('总价', ''))
                                note = attributes.get('备注', '')
                                model = attributes.get('型号', '')
                                brand = attributes.get('品牌', '')
                            except Exception as attribute_deal_error:
                                logger.error(attribute_deal_error)
                                unit = ''
                                unit_price = 0.0
                                number = 0
                                subtotal = 0.0
                                total = 0.0
                                note = ''
                                model = ''
                                brand = ''

                            temp = {
                                'project': data.get('project'),
                                'id': order_id,
                                'attribute': json.dumps(attributes, ensure_ascii=False),
                                'serviceId': second_service_id,
                                'unit': unit,
                                'unit_price': unit_price,
                                'number': number,
                                'subtotal': subtotal,
                                'total': total,
                                'note': note
                            }
                            db_transaction_util.begin()
                            logger.info('增加销售数据')
                            logger.info(temp.__str__())
                            logger.info(save_data.__str__())
                            sale_id = sale_handler.add_sale_info(dict(temp, **save_data))

                            service_attributes = service_handler.get_attribute_by_service(second_service_id)
                            all_required_attr = attribute_handler.get_all_required_attributes()
                            required_attr_list = []
                            for attr in all_required_attr:
                                required_attr_list.append(attr[1])

                            logger.info('增加销售扩展属性')
                            for srv_attr in service_attributes:
                                attr_name = srv_attr[1]
                                if attr_name not in required_attr_list:
                                    attr_id = attribute_handler.get_attr_by_name(attr_name)[0]
                                    sale_item_handler.add_sale_item(sale_id, attr_id, attributes.get(attr_name, ''))

                            # 库存信息更新
                            logger.info('更新库存信息')
                            stock_service.refresh_stock_info(sale_id, brand, model, number, unit, second_service_id)

                            # 回访设置
                            if data.get("callbackTime"):
                                logger.info('增加回访信息')
                                customer_handler.add_return_visit_data(data.get("callbackTime"), car_phone, car_id,
                                                                       car_user, today)
                            db_transaction_util.commit()
                    except Exception as add_error:
                        logger.error(add_error)
                        logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                        db_transaction_util.rollback()
                        raise ApiException(ErrorCode.ParameterMiss)

                    try:
                        p = "defaultPrinter"  # 打印机名称
                        html, page_height = self.preview_html(para_data, True)
                        logger.info('\n' + html)
                        Printer.printing(p, html, page_height)
                    except:
                        pass

                    return set_return_dicts({"orderNo": order_no})

                elif keyword == 'preview':
                    html = self.preview_html(para_data)
                    logger.info('\n' + html)
                    return set_return_dicts(html)

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":

                if not self.storeId:
                    raise ApiException(ErrorCode.PCError)

                if keyword == "detail":

                    check_order_id = para_data.get("checkOrderId")
                    if not check_order_id:
                        raise ApiException(ErrorCode.ParameterMiss)

                    if self.connect:
                        result_dict = SocketServer("orderdetail {} {}".format(self.storeId, check_order_id))

                    else:
                        result = get_sale_info_by_one_key("orderCheckId", check_order_id)
                        result_list = list()

                        result_dict = {}
                        if result:
                            created_time = ''
                            car_id = ''
                            car_user = ''
                            car_phone = ''
                            car_model = ''
                            total_price = 0
                            order_no = ''
                            for data in result:
                                attribute = OrderedDict()
                                for attr in sale_item_handler.get_item_info_buy_sale_id(data['sale_id']):
                                    attribute[attr['name']] = attr['attribute_value']
                                logger.info('销售数据属性调整后的记录：' + attribute.__str__())
                                created_time = data['createdTime']
                                car_id = data['carId']
                                car_user = data['carUser']
                                car_phone = data['carPhone']
                                car_model = data['carModel']
                                price = data['unit_price']
                                pc_id = data['pcId']
                                order_no = data['orderNo']
                                if pc_id:
                                    total_price += price
                                    attribute['project'] = data['project']
                                    attribute['totalPrice'] = price
                                    attribute['orderNo'] = order_no
                                    result_list.append(attribute)

                            try:
                                pc_sign = config.get_store_name()
                            except:
                                pc_sign = ""
                            result_dict = {
                                "msg": result_list,
                                "totalPrice": total_price,
                                "createdTime": created_time,
                                "carId": car_id,
                                "carUser": car_user,
                                "carPhone": car_phone,
                                "carModel": car_model,
                                "orderNo": order_no,
                                "checkOrderId": check_order_id,
                                "pcSign": pc_sign,
                            }

                    if result_dict == 'restart':
                        raise ApiException(ErrorCode.ReStartPC)
                    return set_return_dicts(result_dict)
                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])
