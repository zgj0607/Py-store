# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_second_service_info.ui'
#
# Created: Mon Feb 13 16:30:57 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from collections import OrderedDict

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

from Common import time_utils, config
from View.service.ui.ui_second_service_info import Ui_MainWindow as UiSecondServiceInfo
from View.utils import db_transaction_util
from database.dao.service import attribute_handler, service_handler
from database.dao.stock import stock_handler
from domain.attribute import Attribute
from domain.service_item import ServiceItem


class SecondServiceInfo(QtWidgets.QDialog, UiSecondServiceInfo):
    def __init__(self, title, service_id=None, service_name="", father_id=None):
        QtWidgets.QDialog.__init__(self)

        self.title = title
        self.service_id = service_id
        self.father_id = father_id
        self.setupUi(self)
        self.service_name.setText(service_name)
        self.name = service_name

        self.checkbox_dict = OrderedDict()
        self.checked_dict = {}

        self.submit.clicked.connect(self._update)
        self._init_checkbox()

    def _init_checkbox(self):
        all_attr_list = attribute_handler.get_all_attributes()
        if self.service_id:
            self.checked_dict = self._get_service_attribute()
        row = 0
        column = 0
        model = QtGui.QStandardItemModel()
        for attr in all_attr_list:
            item = QtGui.QStandardItem(attr[1])

            if attr[3] == Attribute.required():
                # 如果是必填，则默认勾选，同时不允许修改
                item.setCheckState(Qt.Checked)
                item.setFlags(QtCore.Qt.NoItemFlags)
            else:
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                # 如果该属性已经关联了服务项目，则默认勾选
                if attr[0] not in self.checked_dict:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)

            self.checkbox_dict[attr[0]] = item

            model.setItem(row, column, item)
            # 表格中每行显示5条记录
            column += 1
            if column >= 5:
                row += 1
                column = 0

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setModel(model)

    def _update(self):
        name = self.service_name.text()
        if '-' in name:
            QtWidgets.QMessageBox.information(self.submit, "提示", "名字输入有误，请勿添加\"-\"符号")
        elif name == "":
            QtWidgets.QMessageBox.information(self.submit, "提示", "请输入名称")
        else:
            try:
                db_transaction_util.begin()
                if self.service_id:
                    if self.name != name:
                        service_handler.update_service(self.service_id, name)
                        stock_handler.update_second_service_name(self.service_id, name)
                else:
                    self.service_id = service_handler.add_second_level_service(name, father_id=self.father_id)

                for k, v in self.checkbox_dict.items():
                    if v.checkState() == Qt.Checked:
                        if k not in self.checked_dict:
                            attr_item = ServiceItem()
                            attr_item.service_id(self.service_id).attribute_id(k).attribute_name(v.text())
                            attr_item.create_time(time_utils.get_now()).create_op(config.login_user_info[0])
                            service_handler.add_service_attribute(attr_item)
                    else:
                        if k in self.checked_dict:
                            service_handler.delete_service_attribute(self.service_id, k)
                db_transaction_util.commit()

                QtWidgets.QMessageBox.information(self.submit, "提示", "提交成功")
                self.close()
            except Exception as db_excption:
                print(db_excption)
                db_transaction_util.rollback()
                QtWidgets.QMessageBox.information(self.submit, "提示", "服务项目更新失败，请重试")

    def _get_service_attribute(self):
        attributes = service_handler.get_attribute_by_service(self.service_id)
        attr_had = {}
        for data in attributes:
            attr_had[data[0]] = data[1]

        return attr_had
