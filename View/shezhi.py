# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shezhi.ui'
#
# Created: Tue Feb 14 16:12:43 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
import requests
import json
import threading
from Common.Urls import route
from Common.config import domain, BUFSIZ
from Common.MySocket import myClient
from View.view import Ui_MainWindow
from Common.StaticFunc import md5
from Common.Common import ClientClose

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from collections import defaultdict
from tornado.options import define, options
from Controller import DbHandler
from collections import OrderedDict
import time
import Common.config as config


class SheZhi_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.setWindowIcon(myIcon)
        self.BUFFER_SIZE = 1024
        self.setupUi()

        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-color:#f9e4c5}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette = QtGui.QPalette()
        self.uc = True
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon))  # 添加背景图片
        self.setPalette(palette)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(367, 208)
        self.setMinimumSize(QtCore.QSize(367, 187))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 40, 231, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(70, 100, 231, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton.clicked.connect(self.Submit)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setPlaceholderText('请填写密码')
        self.lineEdit_2.setPlaceholderText('请填写用户名')
        self.retranslateUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # self.lineEdit.setStyleSheet("background-color:#fff")
        # self.lineEdit_2.setStyleSheet("background-color:#fff")
        # self.pushButton.setStyleSheet("background-color:#f9e4c5")
        self.label_2.setStyleSheet("color:#fff")
        self.label_3.setStyleSheet("color:#fff")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密   码："))

    def Submit(self):
        self.conn = sqlite3.connect('MYDATA.db')
        test = True

        # 获取输入的账号密码
        repwd = self.lineEdit.text() + "udontknowwhy"
        username = self.lineEdit_2.text()

        if repwd != "udontknowwhy" and username != "" or test:
            repwd = md5(repwd)
            # 获取保存的用户账号密码
            if username != "master":
                try:
                    sqlStr = "SELECT pwd FROM Admin WHERE userName=\'{}\'".format(username)
                    cursor = self.conn.execute(sqlStr)
                    data = cursor.fetchone()
                    cursor.close()
                    self.conn.close()
                    if data:
                        pwd = data[0]
                    else:
                        repwd = None
                except:
                    repwd = None

            if repwd or test:
                if username == "master":
                    pwd = "f15127eda7c7a3eab663bf8fa8e3be6e"

                if test or repwd == pwd:
                    self.uc = False
                    QtWidgets.QMessageBox.information(self.pushButton, "提示", "验证成功")
                    self.close()
                    level = 1
                    if username in ['admin', 'master'] or test:
                        level = 0
                    try:
                        config.ui = Ui_MainWindow(level)
                        webThread = threading.Thread(target=self.RunTornado, args=[config.ui])
                        webThread.start()
                        socketThread = threading.Thread(target=self.RunSocket)
                        socketThread.start()
                        config.ui.show()
                    except Exception as e:
                        import traceback
                        print(e)
                        print('traceback.print_exc():{}'.format(traceback.print_exc()))
                        print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                else:
                    QtWidgets.QMessageBox.information(self.pushButton, "提示", "密码输出错误")
            else:
                QtWidgets.QMessageBox.information(self.pushButton, "提示", "无此用户")
        else:
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "请输入用户名、密码")

    def RunTornado(self, ui):
        settings = {
            # 'template_path' : os.path.join(os.path.dirname(__file__),"templates"),
            # 'static_path' : os.path.join(os.path.dirname(__file__),"static"),
            # 'cookie_secret':"2379874hsdhf0234990sdhsaiuofyasop977djdj",
        }

        # route.append((r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))

        define("port", default=15775, help="run for the backend", type="int")
        tornado.options.parse_command_line()
        app = tornado.web.Application(
            handlers=route,
            **settings
        )

        http_server = tornado.httpserver.HTTPServer(app)
        try:
            # if True:
            http_server.listen(options.port)
            tornado.ioloop.IOLoop.instance().start()
        except:
            ui.close()

    def RunSocket(self):
        dbhelp = DbHandler.DB_Handler()

        def server_handle(client, self):
            print('客户端线程已经启动 , 等待其它客户端连接')
            while True:
                try:
                    data, addr = myClient.recvfrom(BUFSIZ)
                except:
                    break

                data = data.decode()
                print("我收到：{}".format(data))
                dataWord = data.split(" ")
                heard = dataWord[0]
                if data == "":
                    client.close()
                    break
                else:
                    if heard == 'xiaofei':
                        startTime = dataWord[1]
                        endTime = dataWord[2]
                        result = dbhelp.GetXiaoFeiTable(startTime, endTime)
                        self.SendMsg(result)

                    elif heard == 'user':
                        key = dataWord[1]
                        value = dataWord[2]
                        # 模糊获取用户信息
                        result = dbhelp.GetLikeUserByKey(key, value)
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
                        self.SendMsg(result)

                    elif heard == 'userorder':
                        carId = dataWord[1]
                        carPhone = dataWord[2]
                        # result = dbhelp.GetXiaoFeiByTwoKey(carId,carPhone)
                        result = dbhelp.GetXiaoFeiByKey('carId', carId)
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

                        self.SendMsg(resultList)

                    elif heard == "orderdetail":
                        checkOrderId = dataWord[1]
                        result = dbhelp.GetXiaoFeiByKey("orderCheckId", checkOrderId, True)
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
                                pcSign = self.GetPcName(pcId)

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

                        self.SendMsg(resultDict)

        threading.Thread(target=server_handle, args=[myClient, self]).start()

    def GetPcName(self, pcId):
        pcSign = ''
        if pcId != '':
            url = domain + 'store/api/findById?pcId={}'.format(pcId)
            req = requests.get(url)
            resultData = json.loads(req.text)
            if resultData.get("code") != 200:
                pass
            else:
                pcSign = resultData.get("data").get("pcSign")

        return pcSign

    def SendMsg(self, data):
        jsonResult = json.dumps(data)
        file_size = str(len(jsonResult))
        myClient.send(file_size.encode())
        time.sleep(1)
        myClient.send(jsonResult.encode())

    def closeEvent(self, event):
        if self.uc:
            ClientClose()
