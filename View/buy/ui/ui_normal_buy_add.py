# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_normal_buy_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_stockQueryForm(object):
    def setupUi(self, stockQueryForm):
        stockQueryForm.setObjectName("stockQueryForm")
        stockQueryForm.resize(950, 636)
        stockQueryForm.setMinimumSize(QtCore.QSize(950, 603))
        stockQueryForm.setMaximumSize(QtCore.QSize(950, 636))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(stockQueryForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(stockQueryForm)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.submit = QtWidgets.QPushButton(stockQueryForm)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(stockQueryForm)
        self.scrollArea.setMinimumSize(QtCore.QSize(930, 560))
        self.scrollArea.setMaximumSize(QtCore.QSize(930, 560))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.out_container = QtWidgets.QWidget()
        self.out_container.setGeometry(QtCore.QRect(-512, 0, 1440, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_container.sizePolicy().hasHeightForWidth())
        self.out_container.setSizePolicy(sizePolicy)
        self.out_container.setMinimumSize(QtCore.QSize(1440, 550))
        self.out_container.setMaximumSize(QtCore.QSize(1440, 545))
        self.out_container.setObjectName("out_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.out_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buy_info_container = QtWidgets.QVBoxLayout()
        self.buy_info_container.setObjectName("buy_info_container")
        self.title_info = QtWidgets.QHBoxLayout()
        self.title_info.setObjectName("title_info")
        self.label_12 = QtWidgets.QLabel(self.out_container)
        self.label_12.setMinimumSize(QtCore.QSize(15, 28))
        self.label_12.setMaximumSize(QtCore.QSize(15, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.title_info.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.out_container)
        self.label_11.setMinimumSize(QtCore.QSize(102, 0))
        self.label_11.setMaximumSize(QtCore.QSize(102, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.title_info.addWidget(self.label_11)
        self.label_1 = QtWidgets.QLabel(self.out_container)
        self.label_1.setMinimumSize(QtCore.QSize(80, 0))
        self.label_1.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.title_info.addWidget(self.label_1)
        self.label_9 = QtWidgets.QLabel(self.out_container)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.title_info.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.out_container)
        self.label_8.setMinimumSize(QtCore.QSize(60, 0))
        self.label_8.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.title_info.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.out_container)
        self.label_7.setMinimumSize(QtCore.QSize(60, 0))
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.title_info.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.out_container)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.title_info.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.out_container)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.title_info.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.out_container)
        self.label_4.setMinimumSize(QtCore.QSize(155, 0))
        self.label_4.setMaximumSize(QtCore.QSize(155, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.title_info.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.out_container)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.title_info.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.out_container)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.title_info.addWidget(self.label_2)
        self.label_10 = QtWidgets.QLabel(self.out_container)
        self.label_10.setMinimumSize(QtCore.QSize(80, 0))
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.title_info.addWidget(self.label_10)
        self.label_14 = QtWidgets.QLabel(self.out_container)
        self.label_14.setMinimumSize(QtCore.QSize(80, 0))
        self.label_14.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.title_info.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(self.out_container)
        self.label_13.setMinimumSize(QtCore.QSize(95, 0))
        self.label_13.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.title_info.addWidget(self.label_13)
        self.label = QtWidgets.QLabel(self.out_container)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.title_info.addWidget(self.label)
        self.buy_info_container.addLayout(self.title_info)
        self.buy_info_1 = QtWidgets.QHBoxLayout()
        self.buy_info_1.setObjectName("buy_info_1")
        self.seq_1 = QtWidgets.QLabel(self.out_container)
        self.seq_1.setMinimumSize(QtCore.QSize(15, 28))
        self.seq_1.setMaximumSize(QtCore.QSize(15, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.seq_1.setFont(font)
        self.seq_1.setObjectName("seq_1")
        self.buy_info_1.addWidget(self.seq_1)
        self.buy_date_1 = QtWidgets.QDateEdit(self.out_container)
        self.buy_date_1.setMinimumSize(QtCore.QSize(100, 28))
        self.buy_date_1.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buy_date_1.setFont(font)
        self.buy_date_1.setDate(QtCore.QDate(2018, 1, 15))
        self.buy_date_1.setObjectName("buy_date_1")
        self.buy_info_1.addWidget(self.buy_date_1)
        self.brand_1 = QtWidgets.QLineEdit(self.out_container)
        self.brand_1.setMinimumSize(QtCore.QSize(80, 28))
        self.brand_1.setMaximumSize(QtCore.QSize(120, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.brand_1.setFont(font)
        self.brand_1.setClearButtonEnabled(True)
        self.brand_1.setObjectName("brand_1")
        self.buy_info_1.addWidget(self.brand_1)
        self.model_1 = QtWidgets.QLineEdit(self.out_container)
        self.model_1.setMinimumSize(QtCore.QSize(80, 28))
        self.model_1.setMaximumSize(QtCore.QSize(120, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.model_1.setFont(font)
        self.model_1.setClearButtonEnabled(True)
        self.model_1.setObjectName("model_1")
        self.buy_info_1.addWidget(self.model_1)
        self.number_1 = QtWidgets.QSpinBox(self.out_container)
        self.number_1.setMinimumSize(QtCore.QSize(60, 28))
        self.number_1.setMaximumSize(QtCore.QSize(60, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.number_1.setFont(font)
        self.number_1.setSuffix("")
        self.number_1.setMinimum(-99)
        self.number_1.setProperty("value", 0)
        self.number_1.setObjectName("number_1")
        self.buy_info_1.addWidget(self.number_1)
        self.unit_1 = QtWidgets.QLineEdit(self.out_container)
        self.unit_1.setMinimumSize(QtCore.QSize(60, 28))
        self.unit_1.setMaximumSize(QtCore.QSize(60, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unit_1.setFont(font)
        self.unit_1.setClearButtonEnabled(True)
        self.unit_1.setObjectName("unit_1")
        self.buy_info_1.addWidget(self.unit_1)
        self.price_1 = QtWidgets.QLineEdit(self.out_container)
        self.price_1.setMinimumSize(QtCore.QSize(100, 28))
        self.price_1.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.price_1.setFont(font)
        self.price_1.setClearButtonEnabled(False)
        self.price_1.setObjectName("price_1")
        self.buy_info_1.addWidget(self.price_1)
        self.total_1 = QtWidgets.QLineEdit(self.out_container)
        self.total_1.setEnabled(True)
        self.total_1.setMinimumSize(QtCore.QSize(100, 28))
        self.total_1.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_1.setFont(font)
        self.total_1.setReadOnly(True)
        self.total_1.setClearButtonEnabled(False)
        self.total_1.setObjectName("total_1")
        self.buy_info_1.addWidget(self.total_1)
        self.supplier_1 = QtWidgets.QLineEdit(self.out_container)
        self.supplier_1.setMinimumSize(QtCore.QSize(150, 28))
        self.supplier_1.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.supplier_1.setFont(font)
        self.supplier_1.setClearButtonEnabled(True)
        self.supplier_1.setObjectName("supplier_1")
        self.buy_info_1.addWidget(self.supplier_1)
        self.service_1 = QtWidgets.QComboBox(self.out_container)
        self.service_1.setMinimumSize(QtCore.QSize(150, 28))
        self.service_1.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.service_1.setFont(font)
        self.service_1.setEditable(False)
        self.service_1.setProperty("clearButtonEnabled", False)
        self.service_1.setObjectName("service_1")
        self.buy_info_1.addWidget(self.service_1)
        self.paid_1 = QtWidgets.QLineEdit(self.out_container)
        self.paid_1.setMinimumSize(QtCore.QSize(80, 28))
        self.paid_1.setMaximumSize(QtCore.QSize(80, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paid_1.setFont(font)
        self.paid_1.setClearButtonEnabled(False)
        self.paid_1.setObjectName("paid_1")
        self.buy_info_1.addWidget(self.paid_1)
        self.unpaid_1 = QtWidgets.QLineEdit(self.out_container)
        self.unpaid_1.setEnabled(True)
        self.unpaid_1.setMinimumSize(QtCore.QSize(80, 28))
        self.unpaid_1.setMaximumSize(QtCore.QSize(80, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unpaid_1.setFont(font)
        self.unpaid_1.setReadOnly(True)
        self.unpaid_1.setClearButtonEnabled(False)
        self.unpaid_1.setObjectName("unpaid_1")
        self.buy_info_1.addWidget(self.unpaid_1)
        self.payment_1 = QtWidgets.QComboBox(self.out_container)
        self.payment_1.setMinimumSize(QtCore.QSize(80, 28))
        self.payment_1.setMaximumSize(QtCore.QSize(80, 28))
        self.payment_1.setObjectName("payment_1")
        self.buy_info_1.addWidget(self.payment_1)
        self.note_1 = QtWidgets.QLineEdit(self.out_container)
        self.note_1.setMinimumSize(QtCore.QSize(95, 28))
        self.note_1.setMaximumSize(QtCore.QSize(95, 28))
        self.note_1.setObjectName("note_1")
        self.buy_info_1.addWidget(self.note_1)
        self.remove_1 = QtWidgets.QPushButton(self.out_container)
        self.remove_1.setMinimumSize(QtCore.QSize(50, 28))
        self.remove_1.setMaximumSize(QtCore.QSize(50, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remove_1.setFont(font)
        self.remove_1.setObjectName("remove_1")
        self.buy_info_1.addWidget(self.remove_1)
        self.buy_info_container.addLayout(self.buy_info_1)
        self.verticalLayout_4.addLayout(self.buy_info_container)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.scrollArea.setWidget(self.out_container)
        self.verticalLayout_3.addWidget(self.scrollArea)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)

        self.retranslateUi(stockQueryForm)
        QtCore.QMetaObject.connectSlotsByName(stockQueryForm)

    def retranslateUi(self, stockQueryForm):
        _translate = QtCore.QCoreApplication.translate
        stockQueryForm.setWindowTitle(_translate("stockQueryForm", "进货信息"))
        self.add.setText(_translate("stockQueryForm", "新增"))
        self.submit.setText(_translate("stockQueryForm", "提交"))
        self.label_12.setText(_translate("stockQueryForm", "#"))
        self.label_11.setText(_translate("stockQueryForm", "进货日期"))
        self.label_1.setText(_translate("stockQueryForm", "商品品牌"))
        self.label_9.setText(_translate("stockQueryForm", "商品型号"))
        self.label_8.setText(_translate("stockQueryForm", "进货数量"))
        self.label_7.setText(_translate("stockQueryForm", "单位"))
        self.label_6.setText(_translate("stockQueryForm", "进货单价"))
        self.label_5.setText(_translate("stockQueryForm", "单品小计"))
        self.label_4.setText(_translate("stockQueryForm", "供应商"))
        self.label_3.setText(_translate("stockQueryForm", "所属项目"))
        self.label_2.setText(_translate("stockQueryForm", "付款金额"))
        self.label_10.setText(_translate("stockQueryForm", "未付金额"))
        self.label_14.setText(_translate("stockQueryForm", "支付方式"))
        self.label_13.setText(_translate("stockQueryForm", " 备注"))
        self.label.setText(_translate("stockQueryForm", "操作"))
        self.seq_1.setText(_translate("stockQueryForm", "1"))
        self.buy_date_1.setDisplayFormat(_translate("stockQueryForm", "yyyy-MM-dd"))
        self.remove_1.setText(_translate("stockQueryForm", "删除"))
