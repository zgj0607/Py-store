# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_first_service_info.ui'
#
# Created: Mon Feb 13 18:54:11 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from View.service.ui.ui_first_service_info import Ui_MainWindow as UiFirstLevelServiceInfo
from database.dao.service import service_handler
from database.dao.stock import stock_handler


class FirstLevelServiceInfo(QtWidgets.QDialog, UiFirstLevelServiceInfo):
    def __init__(self, title, service_id=None, service_name=""):
        super(FirstLevelServiceInfo, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.service_id = service_id
        self.service_name.setText(service_name)
        self.name = service_name

        # 按钮事件
        self.submit.clicked.connect(self._update)

    def _update(self):
        name = self.service_name.text()
        if '-' in name:
            QtWidgets.QMessageBox.information(self.submit, "提示", "名字输入有误，请勿添加\"-\"符号")
        elif name == "":
            QtWidgets.QMessageBox.information(self.submit, "提示", "请输入名称")
        else:
            if not self.service_id:
                service_handler.add_first_level_service(name)
            else:
                if self.name != name:
                    service_handler.update_service(self.service_id, name)
                    stock_handler.update_first_service_name(self.service_id, name)

            QtWidgets.QMessageBox.information(self.submit, "提示", "提交成功")
            self.close()
