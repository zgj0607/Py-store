# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

from Common import Common, StaticFunc
from Common.time_utils import get_now
from View.buy.ui.ui_normal_buy_dialog import Ui_Dialog
from View.utils import db_transaction_util
from database.dao.buy import buy_handler, payment_handler
from database.dao.service import service_handler
from database.dao.stock import brand_handler, model_handler, stock_handler, stock_detail_handler
from database.dao.supplier import supplier_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock import Stock
from domain.stock_detail import StockDetail


class StockInputDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(StockInputDialog, self).__init__()
        self.setupUi(self)

        now = get_now()
        self.buy_time.setDateTime(QDateTime.fromString(now, 'yyyy-MM-dd hh:mm:ss'))
        self.number.setText('1')
        self.number.setFocus()
        self.paid.setText('0.0')
        self.setWindowTitle('进货信息')

        self._init_combo_box()
        self._init_signal_and_slot()
        self._init_validator()

    # 初始化绑定所有的事件处理函数
    def _init_signal_and_slot(self):
        self.commitButton.clicked.connect(self._commit)
        self.brand_comboBox.currentIndexChanged.connect(self._brand_changed)
        self.brand_comboBox.activated.connect(self._add_brand)
        self.model_combo_box.activated.connect(self._add_model)
        self.supplier_combo_box.activated.connect(self._add_supplier)
        self.first_service_combo_box.activated.connect(self._first_srv_text_change)

        self.number.textEdited.connect(self._update_total)
        self.buy_price.textEdited.connect(self._update_total)
        self.total.textChanged.connect(self._update_unpaid)
        self.paid.textEdited.connect(self._update_unpaid)

    # 处理所有Combo Box的初始化和下拉联动
    def _init_combo_box(self):
        self._update_brand()
        self._init_supplier()
        self._init_payment_method()

    def _init_validator(self):
        # int类型输入限制
        StaticFunc.set_validator(self.number, 'int')

        # Float类型显示
        StaticFunc.set_validator(self.buy_price, 'float')
        StaticFunc.set_validator(self.paid, 'float')

    # 品牌和型号下拉框初始化
    def _update_brand(self):
        brand_combo = self.brand_comboBox
        brands = brand_handler.get_all_brand()
        if not brands:
            return

        for brand in brands:
            brand_combo.addItem(brand[1], brand[0])

        brand_combo.addItem('点击新增')

        self._update_model(brands[0][0])

    def _brand_changed(self):
        brand_combo = self.brand_comboBox
        if brand_combo.currentData():
            self._update_model(brand_combo.currentData())

    # 服务项目下拉框初始化
    def _init_service(self):
        first_srv = service_handler.get_all_first_level_service()

        if first_srv:
            self.first_service_combo_box.clear()
            for father_srv in first_srv:
                self.first_service_combo_box.addItem(father_srv[1], father_srv[0])

            self._update_second_service(first_srv[0][0])

        # 一级服务项目下拉联动出发二级服务项目变更

    def _first_srv_text_change(self):
        father_id = self.first_service_combo_box.currentData()
        if father_id:
            self._update_second_service(father_id)
        else:
            self.first_service_combo_box.clear()
            self.second_service_combo_box.clear()
            self._init_service()

    # 二级服务项目初始化
    def _update_second_service(self, father_id):
        self.second_service_combo_box.clear()

        second_srv = service_handler.get_second_service_by_father(father_id)
        for child_srv in second_srv:
            self.second_service_combo_box.addItem(child_srv[3], child_srv[2])

    # 供应商初始化
    def _init_supplier(self):
        suppliers = supplier_handler.get_all_supplier()
        supplier_combo = self.supplier_combo_box
        supplier_combo.clear()

        for supplier in suppliers:
            supplier_combo.addItem(supplier[1], supplier[0])
        supplier_combo.addItem('点击新增')

    # 初始化付款方式
    def _init_payment_method(self):
        methods = Payment.get_payment_method()
        values = list(methods.values())

        payment_method = self.pay_type

        for index, key in enumerate(methods.keys()):
            payment_method.addItem(values[index], key)

    # 型号初始化
    def _update_model(self, brand_id: int):
        model_combo = self.model_combo_box
        model_combo.clear()

        models = model_handler.get_model_by_brand(brand_id)
        if models:
            model_id = models[0][0]
            stock = stock_handler.get_stock_by_model(model_id)
            if stock:
                unit = stock[0][2]
                self.unit.setText(unit)

                self.first_service_combo_box.clear()
                self.first_service_combo_box.addItem(stock[0][4], stock[0][3])
                self.second_service_combo_box.clear()
                self.second_service_combo_box.addItem(stock[0][6], stock[0][5])
            else:
                self.unit.clear()
                self._init_service()

            for model in models:
                model_combo.addItem(model[1], model[0])
            model_combo.addItem('点击新增')
        else:
            model_combo.addItem('点击新增')
            self._init_service()

    # 金额小计自动计算
    def _update_total(self):
        number = self.number.text()
        buy_price = self.buy_price.text()

        if number and buy_price:
            self.total.setText(str(Decimal(int(number) * Decimal(buy_price))))
        else:
            self.total.setText('0.0')

    # 未付金额自动计算
    def _update_unpaid(self):
        total = self.total.text()
        paid = self.paid.text()

        if not paid:
            paid = '0.0'

        if total and paid:
            self.unpaid.setText(str(Decimal(Decimal(total) - Decimal(paid))))

        if total == '0.0' or not total:
            self.paid.setText('0.0')
            self.unpaid.setText('0.0')

    # 进货信息录入
    def _commit(self):
        number = int(self.number.text())
        if not number:
            QMessageBox.warning(self.commitButton, "提示", '数量不能为空或0，请重新填写！')
            return

        if number < 0:
            QMessageBox.information(self.commitButton, "提示", '退货请选择退货按钮，重新输入数量！')
            self.number.setFocus()
            return

        msg = self._check_required()
        if msg:
            QMessageBox.warning(self.commitButton, "提示", msg)
            return

        model_id = self.model_combo_box.currentData()
        try:
            db_transaction_util.begin()

            stock = self._get_stock(model_id)

            # 新增进货信息
            buy_id = self._add_buy_info(stock.id())

            # 新增付款明细
            self._add_payment_detail(buy_id)

            # 库存更新
            self._update_stock_info(stock.id())

            # 更新库存明细
            self._add_stock_detail(stock.id(), buy_id)

            db_transaction_util.commit()
            QMessageBox.information(self.commitButton, "提示", "提交成功")
            self.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.commitButton, "提示", '进货信息录入失败！')
            db_transaction_util.rollback()

    def _add_buy_info(self, stock_id):
        buy_info = BuyInfo()

        buy_date = self.buy_time.date()
        buy_date = buy_date.toString('yyyyMMdd')
        buy_info.buy_date(buy_date)

        buy_info.stock_id(stock_id)

        supplier_id = self.supplier_combo_box.currentData()
        buy_info.supplier_id(supplier_id)

        unit_price = Decimal(self.buy_price.text())
        buy_info.unit_price(unit_price)

        number = int(self.number.text())
        buy_info.number(number)

        create_time = get_now()
        buy_info.create_time(create_time)

        create_op = Common.config.login_user_info[0]
        buy_info.create_op(create_op)

        total = Decimal(self.total.text())
        paid = Decimal(self.paid.text())
        unpaid = Decimal(self.unpaid.text())
        buy_info.paid(paid)
        buy_info.unpaid(unpaid)
        buy_info.total(total)

        notes = self.notelineEdit.text()
        buy_info.notes(notes)

        return buy_handler.add_buy_info(buy_info)

    def _add_brand(self):
        if self.brand_comboBox.currentData():
            return

        brand_name, ok = QInputDialog.getText(self.brand_comboBox, '输入品牌名', '请输入品牌名:', QLineEdit.Normal, '')
        if ok and brand_name:
            brand_id = brand_handler.add_brand(brand_name)
            self.brand_comboBox.insertItem(self.brand_comboBox.count() - 1, brand_name, brand_id)
            self.brand_comboBox.setCurrentIndex(self.brand_comboBox.count() - 2)
            self.model_combo_box.clear()
            self.model_combo_box.addItem('点击新增')
            self.unit.clear()
            self._init_service()

    def _add_model(self):
        if self.model_combo_box.currentData():
            return

        brand_id = self.brand_comboBox.currentData()
        model_name, ok = QInputDialog.getText(self.model_combo_box, '新增型号', '请输入型号:', QLineEdit.Normal, '')
        if ok and model_name:
            model_id = model_handler.add_model(model_name, int(brand_id))
            self.model_combo_box.insertItem(self.model_combo_box.count() - 1, model_name, model_id)
            self.model_combo_box.setCurrentIndex(self.model_combo_box.count() - 2)
            self.unit.clear()

    def _add_supplier(self):
        if self.supplier_combo_box.currentData():
            return

        supplier_name, ok = QInputDialog.getText(self.model_combo_box, '新增供应商', '请输入供应商:', QLineEdit.Normal, '')
        while ok and self.supplier_combo_box.findText(supplier_name) >= 0:
            QMessageBox.warning(self.pushButton, "提示", '供应商已经存在，请重新填写！')
            supplier_name, ok = QInputDialog.getText(self.model_combo_box, '新增供应商', '请输入供应商:', QLineEdit.Normal,
                                                     supplier_name)
        if ok and supplier_name:
            supplier_id = supplier_handler.add_supplier(supplier_name)
            self.supplier_combo_box.insertItem(self.supplier_combo_box.count() - 1, supplier_name, supplier_id)
            self.supplier_combo_box.setCurrentIndex(self.supplier_combo_box.count() - 2)

    def _add_payment_detail(self, buy_id):
        payment_method = int(self.pay_type.currentData())
        paid = Decimal(self.paid.text())
        unpaid = Decimal(self.unpaid.text())

        payment = Payment()

        payment.buy_id(buy_id)
        payment.paid(paid)
        payment.unpaid(unpaid)
        payment.payment_method(payment_method)

        payment_handler.add_payment_detail(payment)

    def _get_stock(self, model_id: int):
        stock = stock_handler.get_stock_by_model(model_id)
        if stock:
            stock_id = stock[0][0]
            stock = Stock()
            stock.id(stock_id)
            return stock
        else:
            stock_id = self._add_stock()
            stock = Stock()
            stock.id(stock_id)
            return stock

    def _add_stock(self):
        stock = Stock()

        brand = self.brand_comboBox
        stock.brand_name(brand.currentText()).brand_id(brand.currentData())

        model = self.model_combo_box
        stock.model_name(model.currentText()).model_id(model.currentData())

        first_service = self.first_service_combo_box
        stock.first_service_id(first_service.currentData()).first_service_name(first_service.currentText())

        second_service = self.second_service_combo_box
        stock.second_service_name(second_service.currentText()).second_service_id(second_service.currentData())

        name = brand.currentText() + '-' + model.currentText()
        stock.name(name)
        stock.unit(self.unit.text())
        stock.create_op(Common.config.login_user_info[0])
        stock.create_time(get_now())

        stock_id = stock_handler.add_stock_info(stock)

        return stock_id

    def _update_stock_info(self, stock_id: int):
        balance = int(self.number.text())
        total = Decimal(self.total.text())
        stock_handler.update_stock_balance(stock_id, balance, total)

    def _check_required(self):
        msg = ''

        if not self.brand_comboBox.currentData():
            msg += '商品品牌、'

        if not self.model_combo_box.currentData():
            msg += '商品型号、'

        if not self.number.text():
            msg += '进货数量、'

        if not self.unit.text():
            msg += '单位、'

        if not self.buy_price.text():
            msg += '进货单价、'

        if not self.supplier_combo_box.currentData():
            msg += '供应商、'

        if not self.first_service_combo_box.currentData():
            msg += '所属一级项目、'

        if not self.second_service_combo_box.currentData():
            msg += '所属二级项目、'

        if not self.paid.text():
            msg += '未付金额、'

        if msg:
            msg = '属性：[' + msg[:-1] + '] 未填写，请填写后重新提交！'

        return msg

    def _add_stock_detail(self, stock_id, buy_id):
        stock_detail = StockDetail()
        stock_detail.buy_id(buy_id).buy_price(Decimal(self.buy_price.text()))

        stock_detail.stock_id(stock_id)

        stock_detail.update_time(get_now()).update_op(Common.config.login_user_info[0])

        for i in range(int(self.number.text())):
            stock_detail_handler.add_stock_detail(stock_detail)
