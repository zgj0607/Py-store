# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_second_service_info.ui'
#
# Created: Mon Feb 13 16:30:57 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from collections import OrderedDict

from PyQt5 import QtCore, QtWidgets, QtGui

from View.types.ui.ui_second_service_info import Ui_MainWindow as UiSecondServiceInfo
from database.dao.service.service_handler import add_second_level_service, update_service


class SecondServiceInfo(QtWidgets.QDialog, UiSecondServiceInfo):
    def __init__(self, title, service_id=None, service_name="", check_name=[], father_id=None, must_attribute=[]):
        QtWidgets.QDialog.__init__(self)

        self.title = title
        self.service_id = service_id
        self.father_id = father_id
        self.mustSet = must_attribute
        self.check_name = check_name
        self.setupUi(self)
        self.service_name.setText(service_name)

        self.submit.clicked.connect(self._update)
        self._init_checkbox()

    def _init_checkbox(self):
        all_name_list = self.get_second_service_attributes()
        row = 0
        column = 0
        model = QtGui.QStandardItemModel()
        self.checkDict = OrderedDict()
        for name in all_name_list:
            item = QtGui.QStandardItem(name)

            if name in self.check_name:
                item.setCheckState(2)
            else:
                item.setCheckState(False)

            if name in self.mustSet:
                item.setCheckState(2)
                item.setFlags(QtCore.Qt.NoItemFlags)
            else:
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            model.setItem(row, column, item)
            self.checkDict[name] = item
            column += 1
            if column >= 5:
                row += 1
                column = 0

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setModel(model)

    def _update(self):
        name = self.service_name.text()
        if '-' in name:
            QtWidgets.QMessageBox.information(self, "提示", "名字输入有误，请勿添加\"-\"符号")
        elif name == "":
            QtWidgets.QMessageBox.information(self, "提示", "请输入名称")
        else:
            self.attribute_state = ""
            self.attribute = ""
            for k, v in self.checkDict.items():
                if v.checkState() == 2:
                    self.attribute_state += "1,"
                else:
                    self.attribute_state += "0,"
                self.attribute += k + ","
            if self.service_id:
                update_service(self.service_id, self.service_name, self.father_id, self.attribute, self.attribute_state)
            else:
                add_second_level_service(name, father_id=self.father_id, attribute=self.attribute,
                                         attribute_state=self.attribute_state)
            w = self
            QtWidgets.QMessageBox.information(w, "提示", "提交成功")
            self.close()

    def get_second_service_attributes(self):

        # 读取txt文档获取属性列表，其中有7个属性是必选的
        root = 'attribute.txt'
        fp = open(root, 'rb')
        name_list = list()

        for name in fp.readlines():
            try:
                name = name.decode().replace("\r", "").replace("\n", "").replace("\ufeff", "").lstrip()
            except Exception as e:
                print(e)
                try:
                    name = name.decode("GB2312").replace("\r", "").replace("\n", "").replace("\ufeff", "").lstrip()
                except Exception as e:
                    import traceback
                    print(e)
                    print('traceback.print_exc():{}'.format(traceback.print_exc()))
                    print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            if name in self.mustSet:
                continue
            name_list.append(name)
        fp.close()

        return self.mustSet + name_list
