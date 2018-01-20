from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from common import config
from common.static_func import md5
from view.users.ui.ui_store_password import Ui_Form as UiStoreAndPassword
from view.utils.table_utils import get_table_cell, add_table_header
from database.dao.users.user_handler import update_super_user_pwd
from domain.store import Store
from remote.store_pc_info import update_store_pc_info, get_store_info


class StoreAndPassword(QtWidgets.QWidget, UiStoreAndPassword):
    def __init__(self):
        super(StoreAndPassword, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('门店和密码管理')

        self.store_pc_info_save.clicked.connect(self._save_store_pc_info)
        self.update_super_user_pwd.clicked.connect(self._update_pwd)

        self.store_pc_table_title = ('门店标识', '联系方式', '门店地址')

        self.remote_data = get_store_info()
        self._init_all_table()

    def _save_store_pc_info(self):
        register_id = get_table_cell(self.store_pc_info_table, 0, 1)
        store_phone = get_table_cell(self.store_pc_info_table, 1, 1)
        address = get_table_cell(self.store_pc_info_table, 2, 1)
        if register_id == "":
            QtWidgets.QMessageBox.information(self.store_pc_info_save, "提示", "标识不能为空")
        elif address == "":
            QtWidgets.QMessageBox.information(self.store_pc_info_save, "提示", "地址不能为空")
        elif store_phone == "":
            QtWidgets.QMessageBox.information(self.store_pc_info_save, "提示", "联系方式不能为空")
        else:
            req = update_store_pc_info(register_id, address, store_phone)
            if req:
                QtWidgets.QMessageBox.information(self.store_pc_info_save, "提示", "修改成功")
                self.remote_data = get_store_info()
                self._init_all_table()
            else:
                QtWidgets.QMessageBox.information(self.updateWorker, "提示", "修改失败")

    def _update_pwd(self):
        pwd_one = get_table_cell(self.super_user_pwd_table, 1, 1)
        pwd_two = get_table_cell(self.super_user_pwd_table, 2, 1)
        old_pwd = get_table_cell(self.super_user_pwd_table, 0, 1)
        if old_pwd == "":
            QtWidgets.QMessageBox.information(self.update_super_user_pwd, "提示", "原密码不能为空")
        elif pwd_one == "":
            QtWidgets.QMessageBox.information(self.update_super_user_pwd, "提示", "密码不能为空")
        elif pwd_one != pwd_two:
            QtWidgets.QMessageBox.information(self.update_super_user_pwd, "提示", "两次输入密码不一致")
        else:
            pwd_one += 'udontknowwhy'
            pwd_one = md5(pwd_one)
            old_pwd += 'udontknowwhy'
            old_pwd = md5(old_pwd)
            if update_super_user_pwd(pwd_one, old_pwd):
                QtWidgets.QMessageBox.information(self.update_super_user_pwd, "提示", "修改成功")
                model = self.super_user_pwd_table.model()
                model.setItem(0, 1, QStandardItem(""))
                model.setItem(1, 1, QStandardItem(""))
                model.setItem(2, 1, QStandardItem(""))
                self.super_user_pwd_table.setModel(model)
            else:
                QtWidgets.QMessageBox.information(self.update_super_user_pwd, "提示", "原密码输入有误")

    def _update_store_info_table(self, store_list):
        add_table_header(self.store_info_table, self.store_pc_table_title)
        model = self.store_info_table.model()
        for row_index, row_data in enumerate(store_list):
            model.setItem(row_index, 0, QStandardItem(str(row_data['pcSign'])))
            model.setItem(row_index, 1, QStandardItem(str(row_data['pcPhone'])))
            model.setItem(row_index, 2, QStandardItem(str(row_data['pcAddress'])))

    def _init_store_pc_table(self, pc_info_dict):
        model = QStandardItemModel()

        model.setColumnCount(2)

        store_name = QStandardItem("设置PC标识")
        store_phone = QStandardItem("联系方式")
        store_address = QStandardItem("设置地址")
        store_name.setFlags(Qt.NoItemFlags)
        store_phone.setFlags(Qt.NoItemFlags)
        store_address.setFlags(Qt.NoItemFlags)
        store_name.setTextAlignment(Qt.AlignCenter)
        store_phone.setTextAlignment(Qt.AlignCenter)
        store_address.setTextAlignment(Qt.AlignCenter)

        model.setItem(0, 0, store_name)
        model.setItem(1, 0, store_phone)
        model.setItem(2, 0, store_address)

        store_name = pc_info_dict.get("pcSign", "")
        store_phone = pc_info_dict.get("pcPhone", "")
        store_address = pc_info_dict.get("pcAddress", "")
        store_id = pc_info_dict.get("pcId", "")

        if store_id:
            store = Store()
            store.name(store_name)
            store.id(store_id)
            store.phone(store_phone)
            store.address(store_address)
            config.add_store_info(store)

        model.setItem(0, 1, QtGui.QStandardItem(str(store_name)))
        model.setItem(1, 1, QtGui.QStandardItem(str(store_phone)))
        model.setItem(2, 1, QtGui.QStandardItem(str(store_address)))

        self.store_pc_info_table.setModel(model)

        self.store_pc_info_table.setRowHeight(0, 59)
        self.store_pc_info_table.setRowHeight(1, 59)
        self.store_pc_info_table.setRowHeight(2, 59)

    def _init_pwd_table(self):
        model2 = QStandardItemModel()
        model2.setColumnCount(2)

        oldPwd = QtGui.QStandardItem("原密码")
        newPwd = QtGui.QStandardItem("新密码")
        newPwd2 = QtGui.QStandardItem("确认密码")
        oldPwd.setFlags(Qt.NoItemFlags)
        newPwd.setFlags(Qt.NoItemFlags)
        newPwd2.setFlags(Qt.NoItemFlags)

        oldPwd.setTextAlignment(Qt.AlignCenter)
        newPwd.setTextAlignment(Qt.AlignCenter)
        newPwd2.setTextAlignment(Qt.AlignCenter)
        model2.setItem(0, 0, oldPwd)
        model2.setItem(1, 0, newPwd)
        model2.setItem(2, 0, newPwd2)
        model2.setItem(0, 1, QtGui.QStandardItem(""))
        model2.setItem(1, 1, QtGui.QStandardItem(""))
        model2.setItem(2, 1, QtGui.QStandardItem(""))
        self.super_user_pwd_table.setModel(model2)
        self.super_user_pwd_table.setRowHeight(0, 59)
        self.super_user_pwd_table.setRowHeight(1, 59)
        self.super_user_pwd_table.setRowHeight(2, 59)

    def _init_all_table(self):
        data = self.remote_data.get("data")
        self._update_store_info_table(data.get("storeList", []))
        store = data.get("store", {})
        self._init_pwd_table()
        self._init_store_pc_table(store)
