import json
import logging
from datetime import datetime

import requests

from Common import config
from Common.config import domain, code

logger = logging.getLogger(__name__)


def check_serial_number(pc_code, serial_number):
    result = False
    data = {'code': serial_number, 'pcCode': pc_code}
    req = requests.post(config.domain + "store/api/check", data)
    req_text = req.text
    try:
        req_text = json.loads(req_text)
        if req_text.get("data"):
            result = req_text.get("data")
    except Exception as e:
        print(e)
        result = req_text

    return result


def update_store_pc_info(register_id, address, store_phone):
    url = domain + 'store/api/update'
    data = {
        "pcAddress": address,
        "pcSign": register_id,
        "pcPhone": store_phone,
        "code": code
    }
    req = requests.post(url, data=data)
    req = json.loads(req.text)
    if req.get("code") == 200:
        return True
    else:
        return False


def get_store_info():
    url = domain + "store/api/list?code={}".format(code)
    logger.info('从' + url + '获取数据')
    req = requests.get(url=url)
    logger.info('获取到数据' + req.text)
    result = json.loads(req.text)
    return result


# 验证注册码
def check_register_code(pc_code, code):
    result = False
    data = {'code': code, 'pcCode': pc_code}
    url = config.domain + "store/api/check"
    logger.info('从' + url + '获取数据')
    req = requests.post(url, data)
    req_text = req.text
    logger.info('获取到数据' + req_text)
    try:
        req_text = json.loads(req_text)
        if req_text.get("data"):
            result = req_text.get("data")
    except Exception as e:
        logger.error(e.__str__())
        result = req_text

    return result


def get_store_detail():
    url = domain + "store/api/detail?code={}".format(code)
    try:
        logger.info('从远程路径获取门店信息：' + url)
        req = requests.get(url)
        json_data = req.text
        logger.info('从远程路径获取门店信息：' + url)
        data = json.loads(json_data)
    except Exception as e:
        logger.error(e.__str__())
        data = None

    return data


def get_try_time():
    url = domain + '/store/api/time'
    try:
        logger.info('调用软件使用时间接口：' + url)
        req = requests.get(url)
    except Exception as try_use_exception:
        logger.error(try_use_exception.__str__())
        return "online"
    logger.info(req.text)
    json_data = json.loads(req.text)
    return datetime.strptime(json_data.get("data"), "%Y-%m-%d %H:%M:%S")
