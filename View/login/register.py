# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
import os
import sys

import remote.store_pc_info
from Common import Common
from View.login.ui.ui_register import Ui_Dialog as UiRegister
import configparser


class Register(QtWidgets.QDialog, UiRegister):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)

        # signal and slot
        self.copy_pc_code.clicked.connect(self.do_copy)
        self.verify_reg_code.clicked.connect(self.do_register)

        serial_number = Common.get_pc_mac()
        self.pc_code.setPlainText(serial_number)

    def do_register(self):
        pc_code = self.pc_code.toPlainText()
        serial_number = self.serial_number.text()
        msg = '验证成功，点击【确定】重启服务程序'
        try:
            result = remote.store_pc_info.check_register_code(pc_code, serial_number)
            print(result)
            if result:
                root = 'config.ini'
                basic_msg = configparser.ConfigParser()
                basic_msg.read(root)
                basic_msg.set("msg", "code", serial_number)
                basic_msg.set("msg", "storeId", result.get("storeId"))
                basic_msg.write(open(root, "w"))

                fp = open("pc.conf", 'wb')
                pc_msg = "{},,,".format(result.get("pcId", ""), result.get("pcPhone", ""), result.get("pcAddress", ""),
                                        result.get("pcSign", ""))
                fp.write(pc_msg.encode())
                fp.close()
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
        Common.ClientClose()

