# -*- coding: utf-8 -*-
import json
import logging
import time
import traceback
from threading import Thread

import requests

from common.config import BUFSIZ, domain
from controller.DbHandler import DB_Handler as DbHelp
from database.dao.customer.customer_handler import get_like_customer_by_key
from database.dao.sale.sale_handler import get_sale_info_by_one_key
from .MySocket import myClient

logger = logging.getLogger(__name__)


def run_socket():
    Thread(target=server_handle, args=[myClient]).start()


def server_handle(client):
    logger.info('客户端线程已经启动 , 等待其它客户端连接')
    while True:
        try:
            data, addr = myClient.recvfrom(BUFSIZ)
        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            break

        data = data.decode()
        logger.info("我收到：{}".format(data))
        dataWord = data.split(" ")
        heard = dataWord[0]
        if data == "":
            client.close()
            break
        else:
            if heard == 'xiaofei':
                startTime = dataWord[1]
                endTime = dataWord[2]
                result = DbHelp.GetXiaoFeiTable(startTime, endTime)
                self.send_message(result)

            elif heard == 'user':
                key = dataWord[1]
                value = dataWord[2]
                # 模糊获取用户信息
                result = get_like_customer_by_key(value)
                userList = list()
                for data in result:
                    # userName,carModel,carPhone,carId
                    userList.append({
                        "userId": data[0],
                        "userName": data[1],
                        "carModel": data[2],
                        "phone": data[3],
                        "carId": data[4],
                    })

                result = {
                    "user": userList,
                }
                self.send_message(result)

            elif heard == 'userorder':
                carId = dataWord[1]
                carPhone = dataWord[2]
                # result = dbhelp.GetXiaoFeiByTwoKey(carId,carPhone)
                result = get_sale_info_by_one_key(carId)
                xiaoFeiList = defaultdict(list)

                for data in result:
                    attribute = OrderedDict(json.loads(data[8]))
                    pcSign = data[11]
                    try:
                        price = float(attribute.pop("总价", 0))
                    except:
                        price = 0

                    orderNo = data[1]
                    orderCheckId = data[10]
                    msg = {
                        "project": data[7],
                        "price": price,
                        'attribute': attribute,

                    }
                    if orderNo not in xiaoFeiList.keys():
                        # 如果没有保存此项则新建
                        temp = {
                            "createdTime": data[0],
                            "msg": [msg],
                            "orderNo": orderNo,
                            "orderCheckId": orderCheckId,
                            'pcSign': pcSign,
                        }
                        temp["totalPrice"] = price

                        xiaoFeiList[orderNo] = temp
                    else:
                        temp = xiaoFeiList[orderNo]
                        temp["totalPrice"] = price + temp.get("totalPrice")
                        temp["msg"].append(msg)
                        xiaoFeiList[orderNo] = temp
                resultList = list()
                for k, v in xiaoFeiList.items():
                    resultList.append(v)

                self.send_message(resultList)

            elif heard == "orderdetail":
                checkOrderId = dataWord[1]
                result = get_sale_info_by_one_key(checkOrderId, True)
                resultList = list()

                resultDict = {}
                if result:
                    createdTime = ''
                    carId = ''
                    carUser = ''
                    carPhone = ''
                    carModel = ''
                    totalPrice = 0
                    pcId = ''
                    orderNo = ''
                    for data in result:
                        attribute = OrderedDict(json.loads(data[8]))
                        createdTime = data[0]
                        carId = data[2]
                        carUser = data[3]
                        carPhone = data[4]
                        carModel = data[5]
                        price = float(attribute.get("总价", 0))
                        pcId = data[9]
                        orderNo = data[1]
                        if pcId:
                            totalPrice += price
                            attribute['project'] = data[7]
                            attribute['totalPrice'] = price
                            attribute['orderNo'] = orderNo
                            resultList.append(attribute)

                    if pcId:
                        pcSign = self.get_pc_name(pcId)

                        resultDict = {
                            "msg": resultList,
                            "totalPrice": totalPrice,
                            "createdTime": createdTime,
                            "carId": carId,
                            "carUser": carUser,
                            "carPhone": carPhone,
                            "carModel": carModel,
                            "orderNo": orderNo,
                            "checkOrderId": checkOrderId,
                            "pcSign": pcSign,
                        }

                self.send_message(resultDict)


def get_pc_name(pc_id):
    logger.info('远程获取店面名称')
    pc_sign = ''
    if pc_id != '':
        url = domain + 'store/api/findById?pcId={}'.format(pc_id)
        logger.info('调用远程URL：' + url)
        req = requests.get(url)
        result_data = json.loads(req.text)
        logger.info('获取远程数据：' + result_data)

        if result_data.get("code") != 200:
            pass
        else:
            pc_sign = result_data.get("data").get("pcSign")
    return pc_sign


def send_message(data):
    json_result = json.dumps(data)
    file_size = str(len(json_result))
    myClient.send(file_size.encode())
    time.sleep(1)
    myClient.send(json_result.encode())
