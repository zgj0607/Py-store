# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_add_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 255)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 271, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.brand_comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.brand_comboBox.setMinimumSize(QtCore.QSize(150, 26))
        self.brand_comboBox.setMaximumSize(QtCore.QSize(160, 26))
        self.brand_comboBox.setBaseSize(QtCore.QSize(150, 26))
        self.brand_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.brand_comboBox.setMinimumContentsLength(10)
        self.brand_comboBox.setObjectName("brand_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.brand_comboBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.model_combo_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.model_combo_box.setMinimumSize(QtCore.QSize(150, 26))
        self.model_combo_box.setMaximumSize(QtCore.QSize(160, 26))
        self.model_combo_box.setBaseSize(QtCore.QSize(150, 26))
        self.model_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.model_combo_box.setMinimumContentsLength(10)
        self.model_combo_box.setObjectName("model_combo_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.model_combo_box)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.unit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.unit.setMinimumSize(QtCore.QSize(150, 0))
        self.unit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.unit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.unit.setObjectName("unit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.unit)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.first_service_combo_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.first_service_combo_box.setMinimumSize(QtCore.QSize(150, 26))
        self.first_service_combo_box.setMaximumSize(QtCore.QSize(160, 45))
        self.first_service_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.first_service_combo_box.setMinimumContentsLength(10)
        self.first_service_combo_box.setObjectName("first_service_combo_box")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.first_service_combo_box)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.second_service_combo_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.second_service_combo_box.setMinimumSize(QtCore.QSize(150, 26))
        self.second_service_combo_box.setMaximumSize(QtCore.QSize(160, 45))
        self.second_service_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.second_service_combo_box.setMinimumContentsLength(10)
        self.second_service_combo_box.setObjectName("second_service_combo_box")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.second_service_combo_box)
        self.commitButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.commitButton.setObjectName("commitButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.commitButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "商品品牌"))
        self.label_3.setText(_translate("Dialog", "商品型号"))
        self.label_5.setText(_translate("Dialog", "单位"))
        self.label_10.setText(_translate("Dialog", "一级项目"))
        self.label_14.setText(_translate("Dialog", "二级项目"))
        self.commitButton.setText(_translate("Dialog", "提交"))

