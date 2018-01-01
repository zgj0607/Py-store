import json

import requests

from Common import config
from Common.config import domain, code


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
    req = requests.get(url=url)
    result = json.loads(req.text)
    print(result)
    return result
