# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

import remote.store_pc_info
from common import common, config
from view.login.ui.ui_register import Ui_Dialog as UiRegister
from domain.store import Store


class Register(QtWidgets.QDialog, UiRegister):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)

        # signal and slot
        self.copy_pc_code.clicked.connect(self.do_copy)
        self.verify_reg_code.clicked.connect(self.do_register)

        serial_number = common.get_pc_mac()
        self.pc_code.setPlainText(serial_number)

    def do_register(self):
        pc_code = self.pc_code.toPlainText()
        serial_number = self.serial_number.text()
        msg = '验证成功，点击【确定】重启服务程序'
        try:
            result = remote.store_pc_info.check_register_code(pc_code, serial_number)
            print(result)
            if result:
                # 将注册信息写入本地文件
                config.add_register_info(result.get('storeId'), serial_number, '')

                # 写入门店信息
                store = Store()
                store.phone(result.get("pcPhone", ""))
                store.address(result.get("pcAddress", ""))
                store.id(result.get("pcId", ""))
                store.name(result.get("pcSign", ""))
                config.add_store_info(store)

                QtWidgets.QMessageBox.information(self.verify_reg_code, "提示", msg)
                python = sys.executable
                os.execl(python, python, *sys.argv)

            else:
                msg = '注册码错误'
                QtWidgets.QMessageBox.information(self.verify_reg_code, "提示", msg)

        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self.verify_reg_code, "提示", "与服务器链接出错")

    def do_copy(self):
        clipboard = QApplication.clipboard()
        copy_text = self.pc_code.toPlainText()
        clipboard.setText(copy_text)
        QMessageBox.information(self.verify_reg_code, "提示", '复制成功')

    def closeEvent(self, event):
        common.ClientClose()
