# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu2.ui'
#
# Created: Mon Feb 13 16:30:57 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QIcon

from Controller.Interface import MenuHandler
from collections import OrderedDict


class Menu_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self,mainWin,title,mustSet=[],menuId=None,name="",checkName=[]):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.title = title
        self.menuId = menuId
        self.name = name
        self.mustSet = mustSet
        self.setWindowIcon(myIcon)
        self.mainWin = mainWin
        self.checkName = checkName
        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-color:#f9e4c5}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette=QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon)) #添加背景图片
        self.setPalette(palette)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(534, 280)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 240, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 491, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 70, 491, 161))
        self.tableView.setObjectName("tableView")

        #禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        checkBoxHeader = self.tableView.verticalHeader()
        checkBoxHeader.hide()
        self.tableView.horizontalHeader().setVisible(False)
        # self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.)
        #静态数据


        #隐藏此字段
        self.hindLabelMsg = QtWidgets.QLabel()
        self.hindLabelMsg.setEnabled(True)
        self.hindLabelMsg.setText(self.menuId)
        self.hindLabelMsg.setObjectName("hindLabelMsg")
        self.hindLabelMsg.hide()

        #按钮事件
        self.pushButton.clicked.connect(self.Update)

        self.retranslateUi(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.title))
        self.pushButton.setText(_translate("MainWindow", "提交"))

        self.label.setText(_translate("MainWindow", "名称："))
        allNameList = self.GetMenu2Attribute()
        row = 0
        column = 0
        model = QtGui.QStandardItemModel()
        self.checkDict = OrderedDict()
        for name in allNameList:
            item = QtGui.QStandardItem(name)
            # item.setCheckable(True)

            if name in self.checkName:
                item.setCheckState(2)
            else:
                item.setCheckState(False)

            if name in self.mustSet:
                item.setCheckState(2)
                item.setFlags(QtCore.Qt.NoItemFlags)
            else:
                item.setFlags(QtCore.Qt.ItemIsUserCheckable| QtCore.Qt.ItemIsEnabled)
            model.setItem(row,column,item)
            self.checkDict[name] = item
            column += 1
            if column >= 5:
                row += 1
                column = 0

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setModel(model)

        self.lineEdit.setText(self.name)

    def Update(self):
        name = self.lineEdit.text()
        if '-' in name:
            QtWidgets.QMessageBox.information(self.pushButton,"提示","名字输入有误，请勿添加\"-\"符号")
        elif name == "":
            QtWidgets.QMessageBox.information(self.pushButton,"提示","请输入名称")
        else:
            id = self.hindLabelMsg.text()
            MenuHandler.SubmitMenu2(name,self.checkDict,id,self.name)
            QtWidgets.QMessageBox.information(self.pushButton,"提示","提交成功")
            self.mainWin.ResetMenu2()
            self.close()

    def GetMenu2Attribute(self):
        #读取txt文档获取属性列表，其中有7个属性是必选的
        root = 'attribute.txt'
        fp = open(root,'rb')
        nameList = list()

        for name in fp.readlines():
            try:
                name = name.decode().replace("\r","").replace("\n","").replace("\ufeff","").lstrip()
            except Exception as e:
                try:
                    name = name.decode("GB2312").replace("\r","").replace("\n","").replace("\ufeff","").lstrip()
                except Exception as e:
                    import traceback
                    print (e)
                    print ('traceback.print_exc():{}'.format(traceback.print_exc()))
                    print ('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            if name in self.mustSet:
                continue
            nameList.append(name)
        fp.close()

        return self.mustSet + nameList