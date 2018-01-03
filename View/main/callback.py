# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'callback.ui'
#
# Created: Sun Apr  2 20:02:24 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import configparser
import json
import sqlite3
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Common.StaticFunc import GetOrderId
from Controller import DbHandler


class CallBack_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self, msg, id, carPhone, carId, carUser):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.setWindowIcon(myIcon)
        self.msg = msg
        self.id = id
        self.carPhone = carPhone
        self.carId = carId
        self.carUser = carUser
        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-image: url(img/button.png);background-color:transparent;background-repeat:no-repeat}
            QCheckBox{color:#fff}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon))  # 添加背景图片
        self.setPalette(palette)
        self.setupUi()
        self.dbhelp = DbHandler.DB_Handler()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(394, 243)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 100, 361, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 227, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        # self.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

        # 禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.pushButton.clicked.connect(self.ChangeState)
        self.checkBox.stateChanged.connect(self.SetTime)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "回访设置"))
        self.label.setText(_translate("MainWindow", self.msg))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_2.setText(_translate("MainWindow", "回访备注："))
        self.checkBox.setText(_translate("MainWindow", "设置二次回访时间："))
        # 设置默认不可操作
        self.dateEdit.setDisabled(True)

    def ChangeState(self):
        remarks = self.lineEdit.text().strip()
        if not remarks:
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "请输入备注")
        else:
            today = datetime.now()
            getData = {}
            orderNo = self.dbhelp.GetOrderNo(today)
            getData["orderNo"] = orderNo
            getData["createdTime"] = today
            getData["carUser"] = self.carUser
            getData["carId"] = self.carId
            getData["carPhone"] = self.carPhone

            carUser = getData.get("carUser", '-')
            userId = getData.get("userId", '-')
            workerId = getData.get("workerId", "-")
            pcId = getData.get("pcId", "-")
            carPhone = getData.get("carPhone", "-")
            carModel = getData.get("carModel", "-")
            carId = getData.get("carId", "-")
            pcSign = getData.get("pcSign", '-')
            workerName = getData.get("workerName", '-')
            root = 'config.ini'
            basicMsg = configparser.ConfigParser()
            basicMsg.read(root)
            orderCheckId = GetOrderId()
            orderId = GetOrderId()
            saveData = {
                'createdTime': getData.get("createdTime").strftime("%Y-%m-%d %H:%M:%S"),
                'userId': userId,
                'pcId': pcId,
                'pcSign': pcSign,
                'carId': carId,
                'workerName': workerName,
                'workerId': workerId,
                'carUser': carUser,
                'carPhone': carPhone,
                'carModel': carModel,
                "orderNo": orderNo,
                "orderCheckId": orderCheckId,
                'code': basicMsg.get("msg", "code"),
                'attribute': json.dumps({"回访备注": remarks}),
                'project': getData.get('project', '-'),
                'id': orderId
            }

            self.dbhelp.InsertXiaoFei(saveData)

            conn = sqlite3.connect('MYDATA.db')
            search = "id={}".format(self.id)

            updateData = "state=\'{}\'".format("1")
            sqlStr = "UPDATE CallBack SET {} WHERE {}".format(updateData, search)
            conn.execute(sqlStr)
            conn.commit()

            if self.checkBox.isChecked():
                # 回访设置
                dbname = "CallBack"
                timeStr = self.dateEdit.text()
                timeList = timeStr.split('/')
                # XP上的时间是以-分割的
                if len(timeList) < 3:
                    timeList = timeStr.split("-")
                # 有时候年份会在以后一个,如：03-25-2016，此时查询数据将出错，因此要判断一下
                if len(timeList[2]) == 4:
                    mon = timeList[0]
                    day = timeList[1]
                    timeList[0] = timeList[2]
                    timeList[1] = mon
                    timeList[2] = day

                timeStr = ""
                for t in timeList:
                    if len(t) < 2:
                        t = "0" + t
                    timeStr += t + "-"
                timeStr = timeStr[:-1]
                key = "{},{},{},{},{},{}".format("callbackTime", "phone", 'carId', "username", 'createdTime', 'state')
                value = "\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\'".format(timeStr, carPhone, carId, carUser, today,
                                                                           '0')
                self.dbhelp.InsertData(dbname, key, value)

            conn.close()
            self.close()

    def SetTime(self):
        if self.checkBox.isChecked():
            self.dateEdit.setEnabled(True)
        else:
            self.dateEdit.setEnabled(False)
