# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created: Thu Apr  6 13:27:41 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self,word,key,today,deviceName,ip,func):
        QtWidgets.QDialog.__init__(self)
        self.word = word
        self.key = key
        self.func = func
        self.today = today
        self.deviceName = deviceName
        self.ip = ip
        myIcon = QIcon('img/logo.png')
        self.setWindowIcon(myIcon)

        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-image: url(img/button.png);background-color:transparent;background-repeat:no-repeat}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette=QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon)) #添加背景图片
        self.setPalette(palette)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(353, 84)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 311, 23))
        self.progressBar.setMinimumSize(QtCore.QSize(311, 23))
        self.progressBar.setMaximumSize(QtCore.QSize(311, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.WindowStaysOnTopHint )
        self.setFixedSize(self.width(), self.height())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def ImportExcel(self):
        #用于正则判断是否是用软件导出的excel文档
        pattern = re.compile(r"^门店系统:\d{4}[-/]\d{2}[/-]\d{2}至\d{4}[-/]\d{2}[/-]\d{2}$")
        # matchs = pattern.match()
        bk = xlrd.open_workbook(fileName)
        sh = bk.sheet_by_name("消费列表")
        nrows = sh.nrows
        temp = list()
        titleList = ['orderCheckId','orderNo','createdTime',"pcSign","carId","carUser","carPhone","carModel","workerName","project"]
        userList = ["carId","carUser","carPhone","carModel"]
        mustlen = len(titleList)
        check = sh.row_values(0)[0]
        matchs = pattern.match(check)
        title = sh.row_values(1)
        #用正则表达式判断第一行数据内容，从而判断是否用软件导出的EXCEL文档
        if matchs:
            #若是用软件导出的则
            for i in range(2,nrows):
                try:
                    saveData = dict()

                    row_data = sh.row_values(i)
                    if row_data[0] != '':
                        checkOrder = dbhelp.GetXiaoFeiByKey("orderCheckId",row_data[0])
                        #有此订单的就不保存了
                        if not checkOrder:
                            if temp:
                               #接入信息后录入
                               for msg in temp:
                                   attribute = {}
                                   for ki in range(len(title)):
                                       if ki < mustlen:
                                           if titleList[ki] in ["project"]:
                                              saveData[titleList[ki]] = msg[ki]
                                           else:
                                              saveData[titleList[ki]] = row_data[ki]
                                       else:
                                           attribute[title[ki]] = msg[ki]

                                   saveData['attribute'] = json.dumps(attribute)
                                   saveData['id'] = GetOrderId()
                                   dbhelp.InsertXiaoFei(saveData)


                            attribute = {}
                            userSave = {}
                            for ki in range(len(title)):
                                if ki < mustlen:
                                    key = titleList[ki]
                                    saveData[key] = row_data[ki]
                                    #保存用户信息
                                    if key in userList:
                                       userSave[key] = row_data[ki]

                                else:
                                    attribute[title[ki]] = row_data[ki]

                            user = dbhelp.CheckUser(userSave.get("carPhone"),userSave.get("carId"))
                            if not user:
                                #没有此用户则添加
                               key = "userName,carPhone,carModel,carId,createdTime"
                               value = "'{}','{}','{}','{}','{}'".format(userSave.get("carUser"),userSave.get("carPhone"),
                                                                         userSave.get("carModel"),userSave.get("carId"),GetToday())
                               try:
                                  dbhelp.InsertData("User",key,value)
                               except:
                                  pass

                            saveData['attribute'] = json.dumps(attribute)
                            saveData['id'] = GetOrderId()
                            dbhelp.InsertXiaoFei(saveData)

                        #清空缓存
                        temp = list()
                    else:
                        #合并了单元格则合并内容是空，将后面不是空的内容进行缓存，合并的内容会在最后一条信息中显示，此时一并进行录入
                        temp.append(row_data)

                except:
                    continue
        else:
            #若不是用软件导出的EXCEL文档则
            msgList = list()
            for i in range(2,nrows):
                #先整理参数，全部变成列表，列表里面是字典，字典的key就是title
                try:
                    row_data = sh.row_values(i)
                    tempData = dict()

                    for k in range(len(title)):
                        tempData[title[k]] = row_data[k]
                    msgList.append(tempData)
                except:
                    continue

            saveList = defaultdict(list)
            for msg in msgList:
                if not msg.get("消费时间") or not msg.get("车牌号"):
                    continue

                key = msg.get("消费时间") + msg.get("车牌号")
                saveList[key].append(msg)

            #插入信息
            must = ["订单号","接待门店","车牌号","车主姓名","联系电话","车型","操作人员","消费项目","消费时间"]
            for k,v in saveList.items():
                orderCheckId = GetOrderId()
                #对同一个订单进行录入
                userSave = {}
                for tempDict in v:
                    orderNo = tempDict.pop("订单号") if tempDict.get("订单号","") != "" else "-"
                    pcSign = tempDict.pop("接待门店","") if tempDict.get("接待门店","") != "" else "-"
                    carId = tempDict.pop("车牌号") if tempDict.get("车牌号") != "" else "-"
                    carUser = tempDict.pop("车主姓名","") if tempDict.get("车主姓名","") != "" else "-"
                    carPhone = str(tempDict.pop("联系电话","-")).replace(".0","") if tempDict.get("联系电话","") != "" else "-"
                    carModel = tempDict.pop("车型","") if tempDict.get("车型","") != "" else "-"
                    workerName = tempDict.pop("操作人员","") if tempDict.get("操作人员","") != "" else "-"
                    project = tempDict.pop("消费项目","") if tempDict.get("消费项目","") != "" else "-"
                    createdTime = str(tempDict.pop("消费时间")).replace(".","-")
                    #保存用户信息
                    userSave["carId"] = carId if carId != '-' else ""
                    userSave["carUser"] = carUser if carUser != '-' else ""
                    userSave["carPhone"] = carPhone if carPhone != '-' else ""
                    userSave['carModel'] = carModel if carModel != '-' else ""

                    if orderNo != "-":
                        checkOrder = dbhelp.GetXiaoFeiByKey("orderNo",orderNo)
                        if checkOrder:
                            break

                    saveData = {
                        "orderNo" : orderNo,
                        "createdTime" : createdTime,
                        "pcSign" : pcSign,
                        "carId" : carId,
                        "carUser" : carUser,
                        "carPhone" : carPhone,
                        "carModel" : carModel,
                        "workerName" : workerName,
                        "project" : project,
                        "orderCheckId" : orderCheckId,
                        "id" : GetOrderId(),
                    }
                    tempAttribute = tempDict

                    attribute = dict()
                    for k,v in tempAttribute.items():
                        if k not in must:
                            if v == "":
                                v = '-'
                            attribute[k] = v
                    try:
                        gsf = float(attribute.get("工时费")) if attribute.get("工时费") != "" else 0
                        sl = float(attribute.get("数量")) if attribute.get("数量") != "" else 0
                        dj = float(attribute.get("单价")) if attribute.get("单价") != "" else 0
                        attribute["总价"] = gsf + sl * dj
                    except:
                        pass
                    saveData["attribute"] = json.dumps(attribute)
                    dbhelp.InsertXiaoFei(saveData)

                if userSave.get("carId") and userSave.get("carPhone"):
                    #当有用户信息的时候判断是否需要自动添加
                    user = dbhelp.CheckUser(userSave.get("carPhone"),userSave.get("carId"))
                    if not user:
                        #没有此用户则添加
                        key = "userName,carPhone,carModel,carId,createdTime"
                        value = "'{}','{}','{}','{}','{}'".format(userSave.get("carUser"),userSave.get("carPhone"),
                                                                    userSave.get("carModel"),userSave.get("carId"),GetToday())
                        try:
                            dbhelp.InsertData("User",key,value)
                        except:
                            pass

