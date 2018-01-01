# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_staff_info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 250)
        MainWindow.setMinimumSize(QtCore.QSize(520, 250))
        MainWindow.setMaximumSize(QtCore.QSize(520, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 519, 259))
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 501, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.staff_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.staff_name.setObjectName("staff_name")
        self.horizontalLayout.addWidget(self.staff_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gender = QtWidgets.QLineEdit(self.layoutWidget)
        self.gender.setObjectName("gender")
        self.horizontalLayout_2.addWidget(self.gender)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.id_card_no = QtWidgets.QLineEdit(self.layoutWidget)
        self.id_card_no.setObjectName("id_card_no")
        self.horizontalLayout_3.addWidget(self.id_card_no)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.submit = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setObjectName("submit")
        self.horizontalLayout_4.addWidget(self.submit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 21))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "姓  名："))
        self.label_2.setText(_translate("MainWindow", "性  别："))
        self.label_3.setText(_translate("MainWindow", "身份证："))
        self.submit.setText(_translate("MainWindow", "提交"))

