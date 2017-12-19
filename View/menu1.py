# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
#
# Created: Mon Feb 13 18:54:11 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QIcon

from Controller.Interface import MenuHandler



class Menu1_Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self,mainWin,title,menuId=None,name=""):
        QtWidgets.QDialog.__init__(self)
        myIcon = QIcon('img/logo.png')
        self.title = title
        self.menuId = menuId
        self.name = name
        self.setWindowIcon(myIcon)
        self.mainWin = mainWin
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
        self.resize(335, 137)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 80, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 311, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        #禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.lineEdit.setText(self.name)

        #按钮事件
        self.pushButton.clicked.connect(self.Update)

        #隐藏此字段
        self.hindLabelMsg = QtWidgets.QLabel()
        self.hindLabelMsg.setEnabled(True)
        self.hindLabelMsg.setText(self.menuId)
        self.hindLabelMsg.setObjectName("hindLabelMsg")
        self.hindLabelMsg.hide()

        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.title))
        self.label.setText(_translate("MainWindow", "名称："))
        self.pushButton.setText(_translate("MainWindow", "提交"))

    def Update(self):
        name = self.lineEdit.text()
        id = self.hindLabelMsg.text()
        if '-' in name:
            QtWidgets.QMessageBox.information(self.pushButton,"提示","名字输入有误，请勿添加\"-\"符号")
        elif name == "":
            QtWidgets.QMessageBox.information(self.pushButton,"提示","请输入名称")
        else:
            MenuHandler.SubmitMenu(name, id, self.name)
            QtWidgets.QMessageBox.information(self.pushButton,"提示","提交成功")
            self.mainWin.ResetMenu1()
