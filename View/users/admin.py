# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worker.ui'
#
# Created: Tue Feb 14 11:34:10 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QIcon

from Controller.Interface import AdminHandler


class Admin_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self,mainWin,AdminTableSet,title="创建系统管理员"):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.title = title
        self.setWindowIcon(myIcon)
        self.mainWin = mainWin
        self.AdminTableSet = AdminTableSet
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
        self.resize(269, 221)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 221, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.usernameEdit = QtWidgets.QLineEdit(self.widget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout.addWidget(self.usernameEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 90, 221, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pwdEdit = QtWidgets.QLineEdit(self.widget1)
        self.pwdEdit.setObjectName("pwdEdit")
        self.horizontalLayout_2.addWidget(self.pwdEdit)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 140, 221, 51))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        # self.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)


        #禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        #按钮事件
        self.pushButton.clicked.connect(self.Create)
        self.pushButton.setMaximumSize(106,56)
        self.pushButton.setMinimumSize(106,56)

        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.title))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密  码："))
        # self.label_3.setText(_translate("MainWindow", "身份证："))
        self.pushButton.setText(_translate("MainWindow", "提交"))

    def Create(self):
        pwd = self.pwdEdit.text() + "udontknowwhy"
        username = self.usernameEdit.text()
        try:
            AdminHandler.AddAdmin(username,pwd)
            QtWidgets.QMessageBox.information(self.pushButton,"提示","提交成功")
            self.AdminTableSet(self.mainWin.AdminTable)
        except:
            QtWidgets.QMessageBox.information(self.pushButton,"提示","已有此用户")

