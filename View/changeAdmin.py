# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeAdmin.ui'
#
# Created: Fri Mar 24 13:27:58 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QIcon

from Controller.Interface import AdminHandler

class ChangeAdmin_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self,mainWin,id,title="重置密码"):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.title = title
        self.id = id
        self.setWindowIcon(myIcon)
        self.mainWin = mainWin
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
        self.resize(214, 239)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 131, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 75, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 131, 41))
        self.label_2.setObjectName("label_2")

        #禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton.clicked.connect(self.Update)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">         请输入新密码</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "确认修改"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">请再次输入密码</span></p></body></html>"))

    def Update(self):
        pwd = self.lineEdit.text()
        id = self.id
        repwd = self.lineEdit_2.text()
        if pwd == "":
            QtWidgets.QMessageBox.information(self.pushButton,"提示","请输入密码")
        elif pwd != repwd:
            QtWidgets.QMessageBox.information(self.pushButton,"提示","两次密码输入不一致")
        else:
            pwd += "udontknowwhy"
            AdminHandler.UpdateAdmin(id,pwd)
            QtWidgets.QMessageBox.information(self.pushButton,"提示","修改成功")
            self.close()