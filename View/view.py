# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt5.uic.pyuic.ui'
#
# Created: Thu Feb  9 17:34:01 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon
from Controller.Interface import ViewHandler
from Controller.Interface.TableHandler import *
from View.types.first_service_info import Menu1_Ui_MainWindow
from View.types.second_service_info import SecondServiceInfo
from Common.config import domain, code
from View.users.worker import Worker_Ui_MainWindow
from View.users.admin import Admin_Ui_MainWindow
from View.users.change_password import ChangeAdmin_Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from Common.Common import ClientClose
from View.userConnect import Ui_MainWindow_UserConnect
import requests
import traceback
from View.main.callback import CallBack_Ui_MainWindow


class Ui_MainWindow(QtWidgets.QMainWindow):
    signal = QtCore.pyqtSignal(list)
    signal2 = QtCore.pyqtSignal()

    def __init__(self, level=None):
        # super(Ui_MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.myIcon = QIcon('img/logo.png')
        # self.setStyleSheet("background-color:#987e65")
        self.setWindowIcon(self.myIcon)
        self.level = level
        # 设置背景
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon))  # 添加背景图片
        self.setPalette(palette)
        self.deviceName = list()

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1010, 720)
        self.setMinimumSize(QtCore.QSize(1010, 720))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.tab_15)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.comboBox = QtWidgets.QComboBox(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(86, 20))
        self.comboBox.setMaximumSize(QtCore.QSize(86, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_18.addWidget(self.comboBox)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_5.sizePolicy().hasHeightForWidth())
        self.dateEdit_5.setSizePolicy(sizePolicy)
        self.dateEdit_5.setMinimumSize(QtCore.QSize(88, 25))
        self.dateEdit_5.setMaximumSize(QtCore.QSize(88, 25))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.horizontalLayout_18.addWidget(self.dateEdit_5)
        self.label_10 = QtWidgets.QLabel(self.tab_15)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_6.sizePolicy().hasHeightForWidth())
        self.dateEdit_6.setSizePolicy(sizePolicy)
        self.dateEdit_6.setMinimumSize(QtCore.QSize(88, 25))
        self.dateEdit_6.setMaximumSize(QtCore.QSize(88, 25))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.horizontalLayout_18.addWidget(self.dateEdit_6)
        self.xiaofeiCheck = QtWidgets.QPushButton(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xiaofeiCheck.sizePolicy().hasHeightForWidth())
        self.xiaofeiCheck.setSizePolicy(sizePolicy)
        self.xiaofeiCheck.setMinimumSize(QtCore.QSize(86, 25))
        self.xiaofeiCheck.setMaximumSize(QtCore.QSize(86, 25))
        self.xiaofeiCheck.setObjectName("xiaofeiCheck")
        self.horizontalLayout_18.addWidget(self.xiaofeiCheck)
        self.xiaofeiOut = QtWidgets.QPushButton(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xiaofeiOut.sizePolicy().hasHeightForWidth())
        self.xiaofeiOut.setSizePolicy(sizePolicy)
        self.xiaofeiOut.setMinimumSize(QtCore.QSize(85, 25))
        self.xiaofeiOut.setMaximumSize(QtCore.QSize(86, 25))
        self.xiaofeiOut.setObjectName("xiaofeiOut")
        self.horizontalLayout_18.addWidget(self.xiaofeiOut)
        self.xiaofeiIn = QtWidgets.QPushButton(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xiaofeiIn.sizePolicy().hasHeightForWidth())
        self.xiaofeiIn.setSizePolicy(sizePolicy)
        self.xiaofeiIn.setMinimumSize(QtCore.QSize(85, 25))
        self.xiaofeiIn.setMaximumSize(QtCore.QSize(86, 25))
        self.xiaofeiIn.setObjectName("xiaofeiIn")
        self.horizontalLayout_18.addWidget(self.xiaofeiIn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.verticalLayout_27.addLayout(self.horizontalLayout_18)
        self.xiaofeiTable = QtWidgets.QTableView(self.tab_15)
        self.xiaofeiTable.setMinimumSize(QtCore.QSize(941, 564))
        self.xiaofeiTable.setObjectName("xiaofeiTable")
        self.verticalLayout_27.addWidget(self.xiaofeiTable)
        self.verticalLayout_3.addLayout(self.verticalLayout_27)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.tab_15)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.loading = QtWidgets.QLabel(self.tab_15)
        self.loading.setObjectName("loading")
        self.horizontalLayout_8.addWidget(self.loading)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_24.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_15, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuOut = QtWidgets.QPushButton(self.tab)
        self.menuOut.setMinimumSize(QtCore.QSize(75, 31))
        self.menuOut.setMaximumSize(QtCore.QSize(75, 31))
        self.menuOut.setObjectName("menuOut")
        self.horizontalLayout_3.addWidget(self.menuOut)
        self.menuIn = QtWidgets.QPushButton(self.tab)
        self.menuIn.setMinimumSize(QtCore.QSize(75, 31))
        self.menuIn.setMaximumSize(QtCore.QSize(75, 31))
        self.menuIn.setObjectName("menuIn")
        self.horizontalLayout_3.addWidget(self.menuIn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mendianMenu1 = QtWidgets.QTableView(self.tab)
        self.mendianMenu1.setMinimumSize(QtCore.QSize(271, 489))
        self.mendianMenu1.setObjectName("mendianMenu1")
        self.verticalLayout_7.addWidget(self.mendianMenu1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu1Add = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu1Add.sizePolicy().hasHeightForWidth())
        self.menu1Add.setSizePolicy(sizePolicy)
        self.menu1Add.setMinimumSize(QtCore.QSize(79, 42))
        self.menu1Add.setMaximumSize(QtCore.QSize(79, 42))
        self.menu1Add.setObjectName("menu1Add")
        self.horizontalLayout.addWidget(self.menu1Add)
        self.menu1Update = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu1Update.sizePolicy().hasHeightForWidth())
        self.menu1Update.setSizePolicy(sizePolicy)
        self.menu1Update.setMinimumSize(QtCore.QSize(79, 42))
        self.menu1Update.setMaximumSize(QtCore.QSize(79, 42))
        self.menu1Update.setObjectName("menu1Update")
        self.horizontalLayout.addWidget(self.menu1Update)
        self.menu1Remove = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu1Remove.sizePolicy().hasHeightForWidth())
        self.menu1Remove.setSizePolicy(sizePolicy)
        self.menu1Remove.setMinimumSize(QtCore.QSize(79, 42))
        self.menu1Remove.setMaximumSize(QtCore.QSize(79, 42))
        self.menu1Remove.setObjectName("menu1Remove")
        self.horizontalLayout.addWidget(self.menu1Remove)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mendianMenu2 = QtWidgets.QTableView(self.tab)
        self.mendianMenu2.setMinimumSize(QtCore.QSize(531, 491))
        self.mendianMenu2.setObjectName("mendianMenu2")
        self.verticalLayout_6.addWidget(self.mendianMenu2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.menu2Add = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu2Add.sizePolicy().hasHeightForWidth())
        self.menu2Add.setSizePolicy(sizePolicy)
        self.menu2Add.setMinimumSize(QtCore.QSize(75, 39))
        self.menu2Add.setMaximumSize(QtCore.QSize(75, 39))
        self.menu2Add.setObjectName("menu2Add")
        self.horizontalLayout_2.addWidget(self.menu2Add)
        self.menu2Update = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu2Update.sizePolicy().hasHeightForWidth())
        self.menu2Update.setSizePolicy(sizePolicy)
        self.menu2Update.setMinimumSize(QtCore.QSize(75, 39))
        self.menu2Update.setMaximumSize(QtCore.QSize(75, 39))
        self.menu2Update.setObjectName("menu2Update")
        self.horizontalLayout_2.addWidget(self.menu2Update)
        self.menu2Remove = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu2Remove.sizePolicy().hasHeightForWidth())
        self.menu2Remove.setSizePolicy(sizePolicy)
        self.menu2Remove.setMinimumSize(QtCore.QSize(75, 39))
        self.menu2Remove.setMaximumSize(QtCore.QSize(75, 39))
        self.menu2Remove.setObjectName("menu2Remove")
        self.horizontalLayout_2.addWidget(self.menu2Remove)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.checkBoxTable = QtWidgets.QTableView(self.tab)
        self.checkBoxTable.setMinimumSize(QtCore.QSize(127, 541))
        self.checkBoxTable.setMaximumSize(QtCore.QSize(127, 16777215))
        self.checkBoxTable.setObjectName("checkBoxTable")
        self.horizontalLayout_7.addWidget(self.checkBoxTable)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.userAdd = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userAdd.sizePolicy().hasHeightForWidth())
        self.userAdd.setSizePolicy(sizePolicy)
        self.userAdd.setMinimumSize(QtCore.QSize(105, 39))
        self.userAdd.setMaximumSize(QtCore.QSize(105, 39))
        self.userAdd.setObjectName("userAdd")
        self.horizontalLayout_4.addWidget(self.userAdd)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.UserTable = QtWidgets.QTableView(self.tab_2)
        self.UserTable.setMinimumSize(QtCore.QSize(940, 491))
        self.UserTable.setObjectName("UserTable")
        self.verticalLayout_5.addWidget(self.UserTable)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.deleteWorker = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteWorker.sizePolicy().hasHeightForWidth())
        self.deleteWorker.setSizePolicy(sizePolicy)
        self.deleteWorker.setMinimumSize(QtCore.QSize(127, 59))
        self.deleteWorker.setMaximumSize(QtCore.QSize(127, 59))
        self.deleteWorker.setObjectName("deleteWorker")
        self.horizontalLayout_13.addWidget(self.deleteWorker)
        self.updateWorker = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateWorker.sizePolicy().hasHeightForWidth())
        self.updateWorker.setSizePolicy(sizePolicy)
        self.updateWorker.setMinimumSize(QtCore.QSize(126, 59))
        self.updateWorker.setMaximumSize(QtCore.QSize(126, 59))
        self.updateWorker.setObjectName("updateWorker")
        self.horizontalLayout_13.addWidget(self.updateWorker)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_23.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.AdminTable = QtWidgets.QTableView(self.tab_3)
        self.AdminTable.setMinimumSize(QtCore.QSize(940, 541))
        self.AdminTable.setObjectName("AdminTable")
        self.verticalLayout_20.addWidget(self.AdminTable)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.addUser = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addUser.sizePolicy().hasHeightForWidth())
        self.addUser.setSizePolicy(sizePolicy)
        self.addUser.setMinimumSize(QtCore.QSize(75, 58))
        self.addUser.setMaximumSize(QtCore.QSize(75, 58))
        self.addUser.setObjectName("addUser")
        self.horizontalLayout_19.addWidget(self.addUser)
        self.changeUser = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeUser.sizePolicy().hasHeightForWidth())
        self.changeUser.setSizePolicy(sizePolicy)
        self.changeUser.setMinimumSize(QtCore.QSize(75, 58))
        self.changeUser.setMaximumSize(QtCore.QSize(75, 58))
        self.changeUser.setObjectName("changeUser")
        self.horizontalLayout_19.addWidget(self.changeUser)
        self.removeUser = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeUser.sizePolicy().hasHeightForWidth())
        self.removeUser.setSizePolicy(sizePolicy)
        self.removeUser.setMinimumSize(QtCore.QSize(75, 58))
        self.removeUser.setMaximumSize(QtCore.QSize(75, 58))
        self.removeUser.setObjectName("removeUser")
        self.horizontalLayout_19.addWidget(self.removeUser)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.verticalLayout_20.addLayout(self.horizontalLayout_19)
        self.verticalLayout_13.addLayout(self.verticalLayout_20)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setMinimumSize(QtCore.QSize(151, 41))
        self.label.setMaximumSize(QtCore.QSize(151, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.today = QtWidgets.QPushButton(self.tab_4)
        self.today.setMinimumSize(QtCore.QSize(119, 39))
        self.today.setMaximumSize(QtCore.QSize(119, 39))
        self.today.setObjectName("today")
        self.horizontalLayout_5.addWidget(self.today)
        self.week = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.week.sizePolicy().hasHeightForWidth())
        self.week.setSizePolicy(sizePolicy)
        self.week.setMinimumSize(QtCore.QSize(119, 39))
        self.week.setMaximumSize(QtCore.QSize(119, 39))
        self.week.setObjectName("week")
        self.horizontalLayout_5.addWidget(self.week)
        self.month = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month.sizePolicy().hasHeightForWidth())
        self.month.setSizePolicy(sizePolicy)
        self.month.setMinimumSize(QtCore.QSize(119, 39))
        self.month.setMaximumSize(QtCore.QSize(119, 39))
        self.month.setObjectName("month")
        self.horizontalLayout_5.addWidget(self.month)
        self.year = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year.sizePolicy().hasHeightForWidth())
        self.year.setSizePolicy(sizePolicy)
        self.year.setMinimumSize(QtCore.QSize(119, 39))
        self.year.setMaximumSize(QtCore.QSize(119, 39))
        self.year.setObjectName("year")
        self.horizontalLayout_5.addWidget(self.year)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.yejiTable = QtWidgets.QTableView(self.tab_4)
        self.yejiTable.setMinimumSize(QtCore.QSize(911, 391))
        self.yejiTable.setObjectName("yejiTable")
        self.verticalLayout_4.addWidget(self.yejiTable)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.jiaoyiPrice = QtWidgets.QLabel(self.tab_4)
        self.jiaoyiPrice.setMinimumSize(QtCore.QSize(181, 119))
        self.jiaoyiPrice.setMaximumSize(QtCore.QSize(181, 119))
        self.jiaoyiPrice.setObjectName("jiaoyiPrice")
        self.horizontalLayout_6.addWidget(self.jiaoyiPrice)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shebeiTable = QtWidgets.QTableView(self.tab_5)
        self.shebeiTable.setMinimumSize(QtCore.QSize(941, 551))
        self.shebeiTable.setObjectName("shebeiTable")
        self.verticalLayout_2.addWidget(self.shebeiTable)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.start = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMinimumSize(QtCore.QSize(75, 29))
        self.start.setMaximumSize(QtCore.QSize(75, 29))
        self.start.setObjectName("start")
        self.horizontalLayout_11.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        self.stop.setMinimumSize(QtCore.QSize(75, 29))
        self.stop.setMaximumSize(QtCore.QSize(75, 29))
        self.stop.setObjectName("stop")
        self.horizontalLayout_11.addWidget(self.stop)
        self.refresh = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        self.refresh.setMinimumSize(QtCore.QSize(75, 29))
        self.refresh.setMaximumSize(QtCore.QSize(75, 29))
        self.refresh.setObjectName("refresh")
        self.horizontalLayout_11.addWidget(self.refresh)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_15.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.callbackTable = QtWidgets.QTableView(self.tab_6)
        self.callbackTable.setMinimumSize(QtCore.QSize(941, 551))
        self.callbackTable.setObjectName("callbackTable")
        self.verticalLayout_11.addWidget(self.callbackTable)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.callback = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.callback.sizePolicy().hasHeightForWidth())
        self.callback.setSizePolicy(sizePolicy)
        self.callback.setMinimumSize(QtCore.QSize(75, 29))
        self.callback.setMaximumSize(QtCore.QSize(75, 29))
        self.callback.setObjectName("callback")
        self.horizontalLayout_17.addWidget(self.callback)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.verticalLayout_14.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_5 = QtWidgets.QLabel(self.tab_7)
        self.label_5.setMinimumSize(QtCore.QSize(121, 31))
        self.label_5.setMaximumSize(QtCore.QSize(121, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem16)
        self.verticalLayout_19.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pcTable = QtWidgets.QTableView(self.tab_7)
        self.pcTable.setMinimumSize(QtCore.QSize(295, 214))
        self.pcTable.setMaximumSize(QtCore.QSize(16777215, 214))
        self.pcTable.setObjectName("pcTable")
        self.horizontalLayout_10.addWidget(self.pcTable)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.tab_7)
        self.label_7.setMinimumSize(QtCore.QSize(91, 165))
        self.label_7.setMaximumSize(QtCore.QSize(91, 165))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.pcSave = QtWidgets.QPushButton(self.tab_7)
        self.pcSave.setMinimumSize(QtCore.QSize(91, 41))
        self.pcSave.setMaximumSize(QtCore.QSize(91, 41))
        self.pcSave.setObjectName("pcSave")
        self.verticalLayout_16.addWidget(self.pcSave)
        self.horizontalLayout_10.addLayout(self.verticalLayout_16)
        self.verticalLayout_19.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15.addLayout(self.verticalLayout_19)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.tab_7)
        self.label_3.setMinimumSize(QtCore.QSize(121, 31))
        self.label_3.setMaximumSize(QtCore.QSize(121, 31))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_21.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pwdTable = QtWidgets.QTableView(self.tab_7)
        self.pwdTable.setMinimumSize(QtCore.QSize(294, 214))
        self.pwdTable.setMaximumSize(QtCore.QSize(16777215, 214))
        self.pwdTable.setObjectName("pwdTable")
        self.horizontalLayout_12.addWidget(self.pwdTable)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_8 = QtWidgets.QLabel(self.tab_7)
        self.label_8.setMinimumSize(QtCore.QSize(91, 165))
        self.label_8.setMaximumSize(QtCore.QSize(91, 165))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_17.addWidget(self.label_8)
        self.pwdUpdate = QtWidgets.QPushButton(self.tab_7)
        self.pwdUpdate.setMinimumSize(QtCore.QSize(91, 41))
        self.pwdUpdate.setMaximumSize(QtCore.QSize(91, 41))
        self.pwdUpdate.setObjectName("pwdUpdate")
        self.verticalLayout_17.addWidget(self.pwdUpdate)
        self.horizontalLayout_12.addLayout(self.verticalLayout_17)
        self.verticalLayout_21.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_21)
        self.verticalLayout_22.addLayout(self.horizontalLayout_15)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setMinimumSize(QtCore.QSize(101, 31))
        self.label_4.setMaximumSize(QtCore.QSize(101, 31))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_18.addWidget(self.label_4)
        self.mendianTable = QtWidgets.QTableView(self.tab_7)
        self.mendianTable.setMinimumSize(QtCore.QSize(941, 311))
        self.mendianTable.setObjectName("mendianTable")
        self.verticalLayout_18.addWidget(self.mendianTable)
        self.verticalLayout_22.addLayout(self.verticalLayout_18)
        self.tabWidget.addTab(self.tab_7, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # 如果不是超级管理员和安装员则只能看到：
        # 服务项目管理、门店人员管理、业绩报表、未回访列表
        if self.level != 0:
            self.tabWidget.removeTab(0)
            self.tabWidget.removeTab(2)
            self.tabWidget.removeTab(3)
            self.tabWidget.removeTab(4)

        # 去除问号
        # self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # 设置外边距
        # self.horizontalLayout_7.setContentsMargins(30,30,30,30)

        # 隐藏字段
        self.hindMenu1 = QtWidgets.QLabel()
        self.hindMenu1.setEnabled(True)
        self.hindMenu1.setText("")
        self.hindMenu1.setObjectName("hindMenu1")
        self.hindMenu1.hide()

        self.hindWorkerId = QtWidgets.QLabel()
        self.hindWorkerId.setEnabled(True)
        self.hindWorkerId.setText("")
        self.hindWorkerId.setObjectName("hindWorkerId")
        self.hindWorkerId.hide()

        # 隔行变色
        # self.xiaofeiTable.setAlternatingRowColors(True)
        # self.mendianTable.setAlternatingRowColors(True)
        # self.mendianMenu1.setAlternatingRowColors(True)
        # self.mendianMenu2.setAlternatingRowColors(True)
        # self.UserTable.setAlternatingRowColors(True)
        # self.yejiTable.setAlternatingRowColors(True)
        # self.shebeiTable.setAlternatingRowColors(True)

        # 静态数据
        self.checkDict = {}
        self.mustSet = ['数量', '单价', '小计', '总价', '单位', '备注']

        # 表格设置
        # 单选
        self.xiaofeiTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.mendianMenu1.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.mendianMenu2.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.UserTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.callbackTable.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)

        # 选择整行
        self.mendianMenu1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.mendianMenu2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.UserTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shebeiTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.AdminTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.yejiTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.callbackTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # 表格铺满
        self.xiaofeiTable.horizontalHeader().setStretchLastSection(True)
        self.mendianMenu1.horizontalHeader().setStretchLastSection(True)
        self.mendianMenu2.horizontalHeader().setStretchLastSection(True)
        self.UserTable.horizontalHeader().setStretchLastSection(True)
        self.yejiTable.horizontalHeader().setStretchLastSection(True)
        self.shebeiTable.horizontalHeader().setStretchLastSection(True)
        self.mendianTable.horizontalHeader().setStretchLastSection(True)
        self.AdminTable.horizontalHeader().setStretchLastSection(True)
        self.pcTable.horizontalHeader().setStretchLastSection(True)
        self.pwdTable.horizontalHeader().setStretchLastSection(True)
        self.checkBoxTable.horizontalHeader().setStretchLastSection(True)
        self.callbackTable.horizontalHeader().setStretchLastSection(True)

        # 不可选择
        # self.yejiTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.mendianTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.checkBoxTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        # 设置单元格禁止更改
        self.xiaofeiTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mendianMenu1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mendianMenu2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.UserTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.yejiTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.shebeiTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mendianTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.AdminTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.checkBoxTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.callbackTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # 表头信息显示居中
        self.xiaofeiTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.mendianMenu1.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.mendianMenu2.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.UserTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.yejiTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.shebeiTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.mendianTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.AdminTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.callbackTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)

        # 去除表头
        self.pcTable.horizontalHeader().setVisible(False)
        self.pwdTable.horizontalHeader().setVisible(False)
        self.checkBoxTable.horizontalHeader().setVisible(False)

        # 去除数字列
        xiaofeiHeader = self.xiaofeiTable.verticalHeader()
        xiaofeiHeader.hide()
        yejiHeader = self.yejiTable.verticalHeader()
        yejiHeader.hide()
        menu1Header = self.mendianMenu1.verticalHeader()
        menu1Header.hide()
        menu2Header = self.mendianMenu2.verticalHeader()
        menu2Header.hide()
        pcTableHeader = self.pcTable.verticalHeader()
        pcTableHeader.hide()
        pwdTableHeader = self.pwdTable.verticalHeader()
        pwdTableHeader.hide()
        checkBoxHeader = self.checkBoxTable.verticalHeader()
        checkBoxHeader.hide()

        # 去除表格网纹
        self.checkBoxTable.setShowGrid(False)

        # 初始化时间
        nowTime = datetime.now()
        self.dateEdit_5.setDate(nowTime.date())
        self.dateEdit_6.setDate(nowTime.date())

        # 添加按钮事件
        self.xiaofeiCheck.clicked.connect(self.XiaofeiCheck)
        # self.comboBox.currentTextChanged['QString'].connect(self.selectXiaoFei)
        self.xiaofeiOut.clicked.connect(self.XiaofeiOut)
        self.xiaofeiOut.pressed.connect(self.JustInfo)
        self.xiaofeiIn.clicked.connect(self.XiaofeiIn)
        self.xiaofeiTable.clicked['QModelIndex'].connect(self.Printer)

        self.mendianMenu1.clicked['QModelIndex'].connect(self.CheckMenu)
        self.mendianMenu2.clicked['QModelIndex'].connect(self.CheckMenu2)

        self.menu1Update.clicked.connect(self.UpdateMenu)
        self.menu1Add.clicked.connect(self.CreateMenu)
        self.menu1Remove.clicked.connect(self.DeleteMenu1)
        self.menu2Update.clicked.connect(self.UpdateMenu2)
        self.menu2Add.clicked.connect(self.CreateMenu2)
        self.menu2Remove.clicked.connect(self.DeleteMenu2)
        self.menuOut.clicked.connect(self.MenuOutFunc)
        self.menuIn.clicked.connect(self.MenuInFunc)

        self.userAdd.clicked.connect(self.CreateWorker)
        self.updateWorker.clicked.connect(self.UpdateWorker)
        self.deleteWorker.clicked.connect(self.DeleteWorker)

        self.week.clicked.connect(self.CheckWeek)
        self.month.clicked.connect(self.CheckMonth)
        self.year.clicked.connect(self.CheckYear)
        self.today.clicked.connect(self.CheckToday)

        self.start.clicked.connect(self.Start)
        self.stop.clicked.connect(self.Stop)
        self.refresh.clicked.connect(self.Refresh)

        self.tabWidget.currentChanged.connect(self.TabChange)
        self.pwdUpdate.clicked.connect(self.UpdatePwd)
        self.pcSave.clicked.connect(self.SavePcName)

        self.addUser.clicked.connect(self.AddAdmin)
        self.changeUser.clicked.connect(self.ChangeAdmin)
        self.removeUser.clicked.connect(self.RemoveAdmin)

        self.callback.clicked.connect(self.CallBack)

        # 添加自定义信号槽
        self.signal.connect(self.AddYuanGong)
        self.signal2.connect(self.JustInfo)

        # 设置无边框
        # self.tabWidget.setDocumentMode(True)

        # 设置样式
        self.setStyleSheet("""
            QMessageBox{background-image: url(img/1.jpg)}
            QLabel{color:#fff;}
            QLineEdit{background:#fff;}
            QPushButton{background-image: url(img/button.png);background-color:transparent;background-repeat:no-repeat}
            QCheckBox{color:#fff}
            QTableView{background-color:#f8f8f7;color:#000;padding:0;margin:0}

            QTabWidget::pane{
                             border-width:0px;\
                             background: transparent;\
                             border-image: url(img/table.jpg);
                             padding:16px
                             }
            QHeaderView::section, QTableCornerButton::section {
                            padding: 7px;
                            border: none;
                            color:#837762;
                            border-bottom: 1px solid rgb(160, 160, 160);
                            border-right: 1px solid rgb(160, 160, 160);
                            border-bottom: 1px solid gray;
                            background-color: qlineargradient(spread:reflect,
                                x1:0, y1:0, x2:0, y2:1,
                                stop:0 rgba(248, 247, 246, 1),
                                stop:1 rgba(248, 247, 246, 1));
                            }
            QTableView::item:selected {
                            background-color: #FFEAB1;
                            color:#000;
            }
       """
                           )

        # 局部修改
        self.btnOrange = "background-image: url(img/btn_orange.png);background-color:transparent;background-repeat:no-repeat"
        self.btnGrey = "background-image: url(img/tag_grey.png);background-color:transparent;background-repeat:no-repeat"
        self.btnGrey2 = "background-image: url(img/tag_grey2.png);background-color:transparent;background-repeat:no-repeat"
        self.btnYellow = "background-image: url(img/button.png);background-color:transparent;background-repeat:no-repeat"

        self.xiaofeiTable.setStyleSheet("background-color:#f8f8f7")
        self.checkBoxTable.setStyleSheet("""background: transparent;
                                        border:none;
                                        font-size:14px;
                                    """)
        self.mendianMenu1.setStyleSheet("background-color:#f8f8f7")
        self.mendianMenu2.setStyleSheet("background-color:#f8f8f7")

        # 设置按钮图片
        # self.week.setStyleSheet("background-color: green")

        self.week.setStyleSheet(self.btnGrey2)
        self.year.setStyleSheet(self.btnGrey2)
        self.month.setStyleSheet(self.btnGrey2)
        self.today.setStyleSheet(self.btnGrey)
        self.xiaofeiCheck.setStyleSheet(self.btnOrange)
        self.xiaofeiOut.setStyleSheet(self.btnOrange)
        self.xiaofeiIn.setStyleSheet(self.btnOrange)
        self.comboBox.setStyleSheet("background-color:#EBEBEB;")
        self.dateEdit_5.setStyleSheet("background-color:#EBEBEB;")
        self.dateEdit_6.setStyleSheet("background-color:#EBEBEB;")
        self.userAdd.setStyleSheet(self.btnGrey)
        self.pcSave.setStyleSheet(self.btnOrange)
        self.pwdUpdate.setStyleSheet(self.btnOrange)

        # 设置label图片
        self.jiaoyiPrice.setStyleSheet("background-image: url(img/sec_moneypc.png);"
                                       "background-color:transparent;"
                                       "background-repeat:no-repeat;font-size:13px;"
                                       "padding:10px")

        # 设置tab图片
        # QTabBar:tab {background-image: url(img/tab.jpg); height: 30px; width:125px;background-repeat:no-repeat;background-position: center;}
        self.tabWidget.setStyleSheet("""
            QTabBar:tab {
                background-image: url(img/TAG1.png);
                height: 44px;
                width:115px;
                font-size:12px;
                background-color:transparent;
                background-repeat:no-repeat
            }
            QTabBar::tab:selected{
                background-image: url(img/TAG2.png);
                font-size:12px;
                background-color:transparent;
                background-repeat:no-repeat
            }
        """)

        # 微调：
        self.horizontalLayout_5.setSpacing(0)
        self.verticalLayout_5.setSpacing(10)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_4.setSpacing(0)
        self.verticalLayout_4.setSpacing(0)

        self.UserTable.setMinimumSize(QtCore.QSize(930, 435))
        self.mendianMenu1.setMinimumSize(QtCore.QSize(271, 450))
        self.mendianMenu2.setMinimumSize(QtCore.QSize(500, 450))
        self.pwdTable.setMinimumSize(QtCore.QSize(340, 180))
        self.pwdTable.setMaximumSize(QtCore.QSize(16777215, 180))
        self.pcTable.setMinimumSize(QtCore.QSize(340, 180))
        self.pcTable.setMaximumSize(QtCore.QSize(16777215, 180))
        self.deleteWorker.setMinimumSize(QtCore.QSize(100, 45))
        self.deleteWorker.setMaximumSize(QtCore.QSize(100, 45))
        self.updateWorker.setMinimumSize(QtCore.QSize(100, 45))
        self.updateWorker.setMaximumSize(QtCore.QSize(100, 45))
        self.AdminTable.setMinimumSize(QtCore.QSize(930, 450))
        self.addUser.setMinimumSize(QtCore.QSize(75, 45))
        self.addUser.setMaximumSize(QtCore.QSize(75, 45))
        self.changeUser.setMinimumSize(QtCore.QSize(75, 45))
        self.changeUser.setMaximumSize(QtCore.QSize(75, 45))
        self.removeUser.setMinimumSize(QtCore.QSize(75, 45))
        self.removeUser.setMaximumSize(QtCore.QSize(75, 45))
        self.shebeiTable.setMinimumSize(QtCore.QSize(930, 450))
        self.label_7.setMinimumSize(QtCore.QSize(91, 135))
        self.label_7.setMaximumSize(QtCore.QSize(91, 135))
        self.label_8.setMinimumSize(QtCore.QSize(91, 135))
        self.label_8.setMaximumSize(QtCore.QSize(91, 135))
        self.xiaofeiTable.setMinimumSize(QtCore.QSize(930, 450))
        self.checkBoxTable.setMinimumSize(QtCore.QSize(127, 550))
        self.userAdd.setMaximumSize(QtCore.QSize(125, 45))

        self.label.setMinimumSize(QtCore.QSize(151, 10))
        self.label.setMaximumSize(QtCore.QSize(151, 10))
        self.jiaoyiPrice.setMinimumSize(QtCore.QSize(180, 96))
        self.jiaoyiPrice.setMaximumSize(QtCore.QSize(180, 96))
        self.menu1Add.setMinimumSize(QtCore.QSize(106, 56))
        self.menu1Add.setMaximumSize(QtCore.QSize(106, 56))
        self.menu1Update.setMinimumSize(QtCore.QSize(106, 56))
        self.menu1Update.setMaximumSize(QtCore.QSize(106, 56))
        self.menu1Remove.setMinimumSize(QtCore.QSize(106, 56))
        self.menu1Remove.setMaximumSize(QtCore.QSize(106, 56))
        self.menu2Add.setMinimumSize(QtCore.QSize(106, 56))
        self.menu2Add.setMaximumSize(QtCore.QSize(106, 56))
        self.menu2Update.setMinimumSize(QtCore.QSize(106, 56))
        self.menu2Update.setMaximumSize(QtCore.QSize(106, 56))
        self.menu2Remove.setMinimumSize(QtCore.QSize(106, 56))
        self.menu2Remove.setMaximumSize(QtCore.QSize(106, 56))
        self.deleteWorker.setMinimumSize(QtCore.QSize(106, 56))
        self.deleteWorker.setMaximumSize(QtCore.QSize(106, 56))
        self.updateWorker.setMinimumSize(QtCore.QSize(106, 56))
        self.updateWorker.setMaximumSize(QtCore.QSize(106, 56))
        self.start.setMinimumSize(QtCore.QSize(106, 56))
        self.start.setMaximumSize(QtCore.QSize(106, 56))
        self.stop.setMinimumSize(QtCore.QSize(106, 56))
        self.stop.setMaximumSize(QtCore.QSize(106, 56))
        self.refresh.setMinimumSize(QtCore.QSize(106, 56))
        self.refresh.setMaximumSize(QtCore.QSize(106, 56))
        self.addUser.setMinimumSize(QtCore.QSize(106, 56))
        self.addUser.setMaximumSize(QtCore.QSize(106, 56))
        self.removeUser.setMinimumSize(QtCore.QSize(106, 56))
        self.removeUser.setMaximumSize(QtCore.QSize(106, 56))
        self.changeUser.setMinimumSize(QtCore.QSize(106, 56))
        self.changeUser.setMaximumSize(QtCore.QSize(106, 56))
        self.pcSave.setMinimumSize(QtCore.QSize(120, 61))
        self.pcSave.setMaximumSize(QtCore.QSize(120, 61))
        self.pwdUpdate.setMinimumSize(QtCore.QSize(120, 61))
        self.pwdUpdate.setMaximumSize(QtCore.QSize(120, 61))

        self.week.setMinimumSize(QtCore.QSize(125, 52))
        self.week.setMaximumSize(QtCore.QSize(125, 52))
        self.month.setMinimumSize(QtCore.QSize(125, 52))
        self.month.setMaximumSize(QtCore.QSize(125, 52))
        self.year.setMinimumSize(QtCore.QSize(125, 52))
        self.year.setMaximumSize(QtCore.QSize(125, 52))
        self.today.setMinimumSize(QtCore.QSize(125, 52))
        self.today.setMaximumSize(QtCore.QSize(125, 52))

        self.xiaofeiCheck.setMinimumSize(QtCore.QSize(115, 36))
        self.xiaofeiCheck.setMaximumSize(QtCore.QSize(115, 36))
        self.xiaofeiOut.setMinimumSize(QtCore.QSize(115, 36))
        self.xiaofeiOut.setMaximumSize(QtCore.QSize(15, 36))
        self.xiaofeiIn.setMinimumSize(QtCore.QSize(115, 36))
        self.xiaofeiIn.setMaximumSize(QtCore.QSize(115, 36))
        self.comboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.dateEdit_5.setMinimumSize(QtCore.QSize(100, 30))
        self.dateEdit_5.setMaximumSize(QtCore.QSize(100, 30))
        self.dateEdit_6.setMinimumSize(QtCore.QSize(100, 30))
        self.dateEdit_6.setMaximumSize(QtCore.QSize(100, 30))
        self.callback.setMinimumSize(QtCore.QSize(106, 56))
        self.callback.setMaximumSize(QtCore.QSize(106, 56))
        self.callbackTable.setMinimumSize(QtCore.QSize(930, 435))

        # self.pMovie = QtGui.QMovie("img/loading.gif")
        # self.loading.setMovie(self.pMovie)
        self.loading.hide()
        self.loadCheck = True

        self.retranslateUi(self)
        # 默认选择第一个空间
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "门店管理系统"))
        self.comboBox.setItemText(0, _translate("MainWindow", "本店"))
        self.comboBox.setItemText(1, _translate("MainWindow", "全店"))
        self.label_10.setText(_translate("MainWindow", "---"))
        self.xiaofeiCheck.setText(_translate("MainWindow", "查询"))
        self.xiaofeiOut.setText(_translate("MainWindow", "导出"))
        self.xiaofeiIn.setText(_translate("MainWindow", "导入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "营业明细查询"))
        self.menu1Add.setText(_translate("MainWindow", "新增"))
        self.menu1Update.setText(_translate("MainWindow", "修改"))
        self.menu1Remove.setText(_translate("MainWindow", "删除"))
        self.menu2Add.setText(_translate("MainWindow", "新增"))
        self.menu2Update.setText(_translate("MainWindow", "修改"))
        self.menu2Remove.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "服务项目管理"))
        self.userAdd.setText(_translate("MainWindow", "新增员工"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "门店人员管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "系统人员管理"))
        self.addUser.setText(_translate("MainWindow", "添加用户"))
        self.changeUser.setText(_translate("MainWindow", "重置密码"))
        self.removeUser.setText(_translate("MainWindow", "删除用户"))
        self.today.setText(_translate("MainWindow", "今日"))
        self.week.setText(_translate("MainWindow", "本周"))
        self.month.setText(_translate("MainWindow", "本月"))
        self.year.setText(_translate("MainWindow", "本年"))
        # self.jiaoyiNumber.setText(_translate("MainWindow", "总交易单数："))
        # self.jiaoyiPrice.setText(_translate("MainWindow", "总交易金额："))
        self.jiaoyiPrice.setText(_translate("MainWindow", "     总交易单数：\n\n     总交易金额："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "业绩报表"))
        self.start.setText(_translate("MainWindow", "启用"))
        self.stop.setText(_translate("MainWindow", "禁用"))
        self.refresh.setText(_translate("MainWindow", "刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "设备管理"))
        self.label_3.setText(_translate("MainWindow", "修改最高权限密码"))
        self.pcSave.setText(_translate("MainWindow", "保存"))
        self.pwdUpdate.setText(_translate("MainWindow", "修改"))
        self.label_4.setText(_translate("MainWindow", "所有门店信息"))
        self.deleteWorker.setText(_translate("MainWindow", "删除"))
        self.updateWorker.setText(_translate("MainWindow", "修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "设置"))
        self.menuOut.setText(_translate("MainWindow", "导出"))
        self.menuIn.setText(_translate("MainWindow", "导入"))
        self.callback.setText(_translate("MainWindow", "回访"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "未回访的信息"))
        self.label_11.setText(_translate("MainWindow", "云南原点电子科技有限公司"))
        self.loading.setText(_translate("MainWindow", "查询中请耐心等候.."))
        # self.label_11.setText(_translate("MainWindow", "联系方式"))
        if self.level == 0:
            self.XiaofeiCheck()
        else:
            self.ResetMenu1()

    # =======================================================消费==============================================
    def JustInfo(self):
        # self.pMovie.start()
        self.loading.show()
        QtCore.QCoreApplication.processEvents()

    def XiaofeiCheck(self):

        startTime = self.dateEdit_5.text()
        endTime = self.dateEdit_6.text()
        remote = False
        text = self.comboBox.currentText()
        if text == "全店":
            remote = True
            self.signal2.emit()
        resultStr = xiaofeiTableSet(self.xiaofeiTable, startTime, endTime, remote)
        if resultStr == None:
            pass
            # QtWidgets.QMessageBox.information(self.xiaofeiCheck,"提示","无消费信息")
        elif resultStr == False:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "网络连接错误")
        elif resultStr == 'restart':
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "与服务器链接中断，请重新运行软件")
        else:
            pass
        self.loading.hide()
        # self.pMovie.stop()

        # self.loading.hide()

    # def selectXiaoFei(self):
    #     startTime = self.dateEdit_5.text()
    #     endTime = self.dateEdit_6.text()
    #     remote = False
    #     text = self.comboBox.currentText()
    #     if text == "全店":
    #         remote = True
    #     xiaofeiTableSet(self.xiaofeiTable,startTime,endTime,remote)

    # 导出excel
    def XiaofeiOut(self):
        startTime = self.dateEdit_5.text()
        endTime = self.dateEdit_6.text()
        fileName = ViewHandler.CreateXls(startTime, endTime)
        if fileName:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "文件名为：{}".format(fileName))
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "暂无消费记录")

    # 导入excel
    def XiaofeiIn(self):
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                                                   "Text Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,注意用分号间隔
        if fileName:
            try:
                ViewHandler.ImportExcel(fileName, self)
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "导入成功")
            except Exception as e:
                print(e)
                print('traceback.print_exc():{}'.format(traceback.print_exc()))
                print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "文件错误")

    # 打印
    def Printer(self, Item=None):
        try:
            model = self.xiaofeiTable.model()
            num = model.columnCount()
            import time
            if Item == None or Item.column() != num - 1:
                return
            else:
                try:
                    model = self.xiaofeiTable.model()
                    index = model.index(Item.row(), 0)
                    orderNo = model.data(index)

                    result = ViewHandler.DoPrinter(self, orderNo)
                    if not result:
                        QtWidgets.QMessageBox.information(self.menu1Add, "提示", "打印格式出错")

                except Exception as e:
                    print(e)
                    print('traceback.print_exc():{}'.format(traceback.print_exc()))
                    print('traceback.format_exc():\n{}'.format(traceback.format_exc()))

        except Exception as e:
            print(e)
            print('traceback.print_exc():{}'.format(traceback.print_exc()))
            print('traceback.format_exc():\n{}'.format(traceback.format_exc()))

    # =======================================================消费==============================================

    # =======================================================菜单==============================================
    def CheckMenu(self, Item=None):
        # 清空二级菜单
        self.ResetMenu2()
        if Item == None:
            return
        else:
            model = self.mendianMenu1.model()
            index = model.index(Item.row(), 0)
            id = model.data(index)
            self.hindMenu1.setText(id)
            MenuTableSet(self.mendianMenu2, id)

    # 点击二级菜单后修改属性（checkbox）状态
    def CheckMenu2(self, Item=None):
        if Item == None:
            return
        else:
            # 因为不是每个按钮都有这个表单点击事件的触发，所以缓存一下列表
            self.GetSelectMenu2Attribute(Item)
            AttributeTableSet(self.checkBoxTable, self.showAttributeList)

    def GetSelectMenu2Attribute(self, Item):
        model = self.mendianMenu2.model()
        index = model.index(Item.row(), 0)
        id = model.data(index)
        result = ViewHandler.GetTwoMenu(id)
        attribute = result[4].split(',')
        attributeState = result[5].split(',')
        showNameList = list()
        for i in range(len(attribute)):
            if attributeState[i] == '1':
                showNameList.append(attribute[i])
        self.showAttributeList = showNameList

    # 初始化一级菜单
    def ResetMenu1(self):
        MenuTableSet(self.mendianMenu1)
        model = self.mendianMenu2.model()
        if model:
            model.clear()

    # 初始化二级菜单
    def ResetMenu2(self):
        MenuTableSet(self.mendianMenu2, self.hindMenu1.text())
        AttributeTableSet(self.checkBoxTable, [])

    # 删除一级菜单
    def DeleteMenu1(self):
        id = ViewHandler.GetTableMsg(self.mendianMenu1, 0)
        if id:
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                   "是否删除此菜单?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                ViewHandler.RemoveById(id, 'OneMenu')
                self.ResetMenu1()
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")

    # 打开一级菜单修改界面
    def UpdateMenu(self, Item=None):
        # 初始化新窗口
        row = self.mendianMenu1.currentIndex().row()
        model = self.mendianMenu1.model()
        if model:
            index = model.index(row, 0)
            id = model.data(index)
            if id:
                result = ViewHandler.GetOneMenu(id)
                self.menu = Menu1_Ui_MainWindow(self, "修改一级菜单", id, result[2])
                self.menu.exec()
            else:
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")

    # 打开一级菜单新建界面
    def CreateMenu(self):
        # 初始化新窗口
        try:
            self.menu2 = Menu1_Ui_MainWindow(self, "创建一级菜单", menuId=self.hindMenu1.text())
            self.menu2.exec()
        except Exception as e:
            print(e)

    # 打开二级菜单修改界面
    def UpdateMenu2(self, Item=None):
        # 初始化新窗口
        row = self.mendianMenu2.currentIndex().row()
        model = self.mendianMenu2.model()
        if model:
            index = model.index(row, 0)
            id = model.data(index)
            if id:
                result = ViewHandler.GetTwoMenu(id)
                self.menu2 = SecondServiceInfo(self, "修改二级菜单", self.mustSet, id, result[2], self.showAttributeList)
                self.menu2.exec()
            else:
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择二级菜单")
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")

    # 打开二级菜单新建界面
    def CreateMenu2(self):
        # 初始化新窗口
        model = self.mendianMenu2.model()
        if model:
            # 初始化新窗口
            try:
                self.menu2 = SecondServiceInfo(self, "创建二级菜单", service_id=self.hindMenu1.text())
                self.menu2.exec()
            except Exception as e:
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", e)
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")

    # 删除二级菜单
    def DeleteMenu2(self):
        row = self.mendianMenu2.currentIndex().row()
        model = self.mendianMenu2.model()
        if model:
            index = model.index(row, 0)
            id = model.data(index)
            if id:
                reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                       "是否删除此菜单?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    ViewHandler.RemoveById(id, "TwoMenu")
                    self.ResetMenu2()
            else:
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择二级菜单")
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "请选择一级菜单")

    # 导出excel
    def MenuOutFunc(self):
        fileName = ViewHandler.CreateMenuExcel()
        if fileName:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "文件名为：{}".format(fileName))
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "菜单内容欠缺")

    # 导入excel
    def MenuInFunc(self):
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                                                   "Text Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,注意用分号间隔
        if fileName:
            try:
                ViewHandler.ImportMenuExcel(fileName, self.mustSet)
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "导入成功")
                self.ResetMenu1()
            except:
                QtWidgets.QMessageBox.information(self.menu1Add, "提示", "文件错误")

    # =======================================================菜单==============================================

    # =======================================================员工==============================================
    def CreateWorker(self):
        self.worker = Worker_Ui_MainWindow(self, WorkerTableSet, "新建员工")
        self.worker.exec()

    def UpdateWorker(self):
        id = ViewHandler.GetTableMsg(self.UserTable, 0)
        workerName = ViewHandler.GetTableMsg(self.UserTable, 1)
        sex = ViewHandler.GetTableMsg(self.UserTable, 2)
        idCard = ViewHandler.GetTableMsg(self.UserTable, 3)
        if id:
            self.worker = Worker_Ui_MainWindow(self, WorkerTableSet, "修改员工信息", workerId=id, name=workerName,
                                               idCard=idCard, sex=sex)
            self.worker.exec()
            # WorkerTableSet(self.UserTable)
        else:
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "请选择员工")

    def DeleteWorker(self):
        id = ViewHandler.GetTableMsg(self.UserTable, 0)
        if id:
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                   "是否删除此员工?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                ViewHandler.RemoveById(id, "Worker")
                WorkerTableSet(self.UserTable)
        else:
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "请选择员工")

    # =======================================================员工==============================================

    # =======================================================报表==============================================
    def CheckWeek(self):
        self.week.setStyleSheet(self.btnGrey)
        self.year.setStyleSheet(self.btnGrey2)
        self.month.setStyleSheet(self.btnGrey2)
        self.today.setStyleSheet(self.btnGrey2)
        YeJiTableSet(self.yejiTable, "week", self.jiaoyiPrice)

    def CheckMonth(self):
        self.week.setStyleSheet(self.btnGrey2)
        self.year.setStyleSheet(self.btnGrey2)
        self.month.setStyleSheet(self.btnGrey)
        self.today.setStyleSheet(self.btnGrey2)
        YeJiTableSet(self.yejiTable, "month", self.jiaoyiPrice)

    def CheckYear(self):
        self.week.setStyleSheet(self.btnGrey2)
        self.year.setStyleSheet(self.btnGrey)
        self.month.setStyleSheet(self.btnGrey2)
        self.today.setStyleSheet(self.btnGrey2)
        YeJiTableSet(self.yejiTable, "year", self.jiaoyiPrice)

    def CheckToday(self):
        self.week.setStyleSheet(self.btnGrey2)
        self.year.setStyleSheet(self.btnGrey2)
        self.month.setStyleSheet(self.btnGrey2)
        self.today.setStyleSheet(self.btnGrey)
        YeJiTableSet(self.yejiTable, "today", self.jiaoyiPrice)

    # =======================================================报表==============================================

    # =======================================================设备管理==============================================

    def Start(self):
        id = ViewHandler.GetTableMsg(self.shebeiTable, 0)
        if id:
            updateData = "state='1'"
            ViewHandler.UpdateById(id, "Device", updateData)
            SheBeiTableSet(self.shebeiTable)
        else:
            QtWidgets.QMessageBox.information(self.start, "提示", "请选择设备")

    def Stop(self):
        id = ViewHandler.GetTableMsg(self.shebeiTable, 0)
        if id:
            updateData = "state='0'"
            ViewHandler.UpdateById(id, "Device", updateData)
            SheBeiTableSet(self.shebeiTable)
        else:
            QtWidgets.QMessageBox.information(self, "提示", "请选择设备")

    def Refresh(self):
        SheBeiTableSet(self.shebeiTable)
        QtWidgets.QMessageBox.information(self, "提示", "刷新成功")

    def AddYuanGong(self, myList):
        word = myList[0]
        key = myList[1]
        today = myList[2]
        deviceName = myList[3]
        ip = myList[4]
        if deviceName not in self.deviceName:
            self.deviceName.append(deviceName)
            self.tempUi = Ui_MainWindow_UserConnect(word, key, today, deviceName, ip, ViewHandler.Insert())
            self.tempUi.exec_()
            self.deviceName.remove(deviceName)
            SheBeiTableSet(self.shebeiTable)

    # =======================================================设备管理==============================================

    # =======================================================设置==============================================
    def SavePcName(self):
        pcSign = ViewHandler.GetCellMsg(self.pcTable, 0, 1)
        pcPhone = ViewHandler.GetCellMsg(self.pcTable, 1, 1)
        address = ViewHandler.GetCellMsg(self.pcTable, 2, 1)
        if pcSign == "":
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "标识不能为空")
        elif address == "":
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "地址不能为空")
        elif pcPhone == "":
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "联系方式不能为空")
        else:
            req = ViewHandler.UpdatePcName(pcSign, address, pcPhone, code)
            if req:
                QtWidgets.QMessageBox.information(self.updateWorker, "提示", "修改成功")
                url = domain + "store/api/list?code={}".format(code)
                req = requests.get(url=url)
                resultData = json.loads(req.text)
                storeList = resultData.get("data").get("storeList", [])
                store = resultData.get("data").get("store", {})
                StoreTableSet(self.mendianTable, storeList)
                SheZhiTableSet(self.pcTable, self.pwdTable, store)
            else:
                QtWidgets.QMessageBox.information(self.updateWorker, "提示", "修改失败")

    def UpdatePwd(self):
        pwd = ViewHandler.GetCellMsg(self.pwdTable, 1, 1)
        repwd = ViewHandler.GetCellMsg(self.pwdTable, 2, 1)
        oldpwd = ViewHandler.GetCellMsg(self.pwdTable, 0, 1)
        if oldpwd == "":
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "原密码不能为空")
        elif pwd == "":
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "密码不能为空")
        elif pwd != repwd:
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "两次输入密码不一致")
        else:
            if ViewHandler.UpdatePwd(pwd, oldpwd):
                QtWidgets.QMessageBox.information(self.updateWorker, "提示", "修改成功")
                model = self.pwdTable.model()
                model.setItem(0, 1, QtGui.QStandardItem(""))
                model.setItem(1, 1, QtGui.QStandardItem(""))
                model.setItem(2, 1, QtGui.QStandardItem(""))
                self.pwdTable.setModel(model)
            else:
                QtWidgets.QMessageBox.information(self.updateWorker, "提示", "原密码输入有误")

    # =======================================================设置==============================================

    # =======================================================系统人员管理==============================================
    def AddAdmin(self):
        self.admin = Admin_Ui_MainWindow(self, AdminTableSet)
        self.admin.exec()

    def ChangeAdmin(self):
        id = ViewHandler.GetTableMsg(self.AdminTable, 0)
        if id:
            self.worker = ChangeAdmin_Ui_MainWindow(self, id)
            self.worker.exec()
            # WorkerTableSet(self.UserTable)
        else:
            QtWidgets.QMessageBox.information(self.changeUser, "提示", "请选择管理员")

    def RemoveAdmin(self):
        id = ViewHandler.GetTableMsg(self.AdminTable, 0)
        if id:
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                   "是否删除此管理员?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                ViewHandler.RemoveById(id, "Admin")
                AdminTableSet(self.AdminTable)
        else:
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "请选择员工")

    # =======================================================系统人员管理==============================================
    # =======================================================回访==============================================
    def CallBack(self):
        id = ViewHandler.GetTableMsg(self.callbackTable, 0)
        username = ViewHandler.GetTableMsg(self.callbackTable, 1)
        carId = ViewHandler.GetTableMsg(self.callbackTable, 2)
        carPhone = ViewHandler.GetTableMsg(self.callbackTable, 3)
        callbackTime = ViewHandler.GetTableMsg(self.callbackTable, 4)
        print(callbackTime)
        if id:
            msg = "您于  <b>{}</b> 要回访用户 ： <b>{}</b><br>联系方式为 ： <b>{}</b><br>车牌号为 ： <b>{}</b>".format(callbackTime[:10],
                                                                                                    username, carPhone,
                                                                                                    carId)
            ui = CallBack_Ui_MainWindow(msg, id, carPhone, carId, username)
            ui.exec_()
            CallBackSet(self.callbackTable)
        else:
            QtWidgets.QMessageBox.information(self.updateWorker, "提示", "请选择未回访记录")

    # =======================================================回访==============================================

    def closeEvent(self, event):
        ClientClose()

    # tab點擊事件
    def TabChange(self, i):
        # 設置
        self.ResetMenu2()
        if i == 7:
            try:
                url = domain + "store/api/list?code={}".format(code)
                req = requests.get(url=url)
                resultData = json.loads(req.text)
            except:
                resultData = {'code': 400}
            print(resultData)
            if resultData.get("code") != 200:
                if resultData.get("code") == 400:
                    QtWidgets.QMessageBox.information(self.updateWorker, "提示", "与服务器链接失败")
                else:
                    QtWidgets.QMessageBox.information(self.updateWorker, "提示", "门店已经失效，详情请联系客服")
            else:
                store = resultData.get("data").get("store", {})
                storeList = resultData.get("data").get("storeList", [])
                StoreTableSet(self.mendianTable, storeList)
                SheZhiTableSet(self.pcTable, self.pwdTable, store)

        elif i == 0:
            if self.level == 0:
                # 門店消費
                # self.XiaofeiCheck()
                pass
            else:
                # 服務項目管理
                MenuTableSet(self.mendianMenu1)

        elif i == 1:
            if self.level == 0:
                # 服務項目管理
                MenuTableSet(self.mendianMenu1)
            else:
                # 門店人員管理
                WorkerTableSet(self.UserTable)

        elif i == 2:
            if self.level == 0:
                # 門店人員管理
                WorkerTableSet(self.UserTable)
            else:
                # 業績報表
                YeJiTableSet(self.yejiTable, "today", self.jiaoyiPrice)


        elif i == 3:
            if self.level == 0:
                # 系统管理员管理
                AdminTableSet(self.AdminTable)
            else:
                # 回访设置
                CallBackSet(self.callbackTable)

        # 業績報表
        elif i == 4:
            YeJiTableSet(self.yejiTable, "today", self.jiaoyiPrice)

        # 設備管理
        elif i == 5:
            SheBeiTableSet(self.shebeiTable)

        # 回访设置
        elif i == 6:
            CallBackSet(self.callbackTable)
