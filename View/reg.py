# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
# import win32con
# import win32clipboard as w
from PyQt5.QtGui import QIcon
import sys
import os
from Common import Common
import configparser
import traceback


class Ui_MainWindow_reg(QtWidgets.QDialog):
    def __init__(self, reg=True):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.reg = reg
        self.c = QIcon(':c.png')
        self.setWindowIcon(myIcon)
        self.setWindowIcon(myIcon)
        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-color:#f9e4c5}
        """)
        bgIcon = QtGui.QPixmap('img/1.jpg')
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bgIcon))  # 添加背景图片
        self.setPalette(palette)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(330, 180)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 50, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(96, 17, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(202, 16, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(40, 58, 50, 18))
        # self.label_3.setObjectName("label_3")
        # self.linkNumber = QtWidgets.QLineEdit(self.centralwidget)
        # self.linkNumber.setGeometry(QtCore.QRect(96, 58, 181, 20))
        # self.linkNumber.setObjectName("linkNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 75, 50, 18))
        self.label_4.setObjectName("label_4")
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(96, 75, 181, 20))
        self.code.setObjectName("code")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(115, 130, 100, 35))
        self.pushButton.setObjectName("pushButton")

        # 禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.DoReg)
        self.pushButton_2.clicked.connect(self.translate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "验证"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">序列号：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "复制"))
        # self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">用户名：</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">注册码：</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "验证"))
        if self.reg:
            # for physical_disk in c.Win32_DiskDrive():
            #    try:
            #         serialNumber = physical_disk.SerialNumber.strip()
            #    except:
            #         continue
            #    if serialNumber !=  "读取失败":
            #        break
            serialNumber = Common.GetPCcode()
            self.lineEdit.setText(serialNumber)

    def DoReg(self):
        code = self.code.text()
        pcCode = self.lineEdit.text()
        msg = '验证成功，点击\"确定\"重启服务程序'
        try:
            # if True:
            result = Common.CheckCodeRemote(pcCode, code)
            if result:
                root = 'config.ini'
                basicMsg = configparser.ConfigParser()
                basicMsg.read(root)
                basicMsg.set("msg", "code", code)
                basicMsg.set("msg", "storeId", result.get("storeId"))
                basicMsg.write(open(root, "w"))

                fp = open("pc.conf", 'wb')
                pcMsg = "{},,,".format(result.get("pcId", ""), result.get("pcPhone", ""), result.get("pcAddress", ""),
                                       result.get("pcSign", ""))
                fp.write(pcMsg.encode())
                fp.close()
                QtWidgets.QMessageBox.information(self.pushButton, "提示", msg)
                python = sys.executable
                # Common.JustSend("close {}".format(code))
                # Common.ClientClose()
                os.execl(python, python, *sys.argv)

            else:
                msg = '注册码错误'
                QtWidgets.QMessageBox.information(self.pushButton, "提示", msg)

        except Exception as e:
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "与服务器链接出错")
            # QtWidgets.QMessageBox.information(self.pushButton,"提示",str(e))
            # QtWidgets.QMessageBox.information(self.pushButton,"提示",str(traceback.print_exc()))
            # QtWidgets.QMessageBox.information(self.pushButton,"提示",str(traceback.format_exc()))

    def translate(self):
        clipboard = QApplication.clipboard()
        copy_text = self.lineEdit.text()
        clipboard.setText(copy_text)
        QMessageBox.information(self.pushButton_2, "提示", '复制成功')

    def closeEvent(self, event):
        Common.ClientClose()
