import traceback
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

from Common import StaticFunc, Common
from Common.time_utils import get_now
from View.buy.ui.ui_write_off_dialog import Ui_writeOffDialog
from View.utils import db_transaction_util
from database.dao.buy import buy_handler, payment_handler
from database.dao.stock import stock_detail_handler, stock_handler, brand_handler, model_handler
from database.dao.supplier import supplier_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock import Stock
from domain.stock_detail import StockDetail


class WriteOffDialog(QtWidgets.QDialog, Ui_writeOffDialog):
    def __init__(self, stock: Stock, sale_number: int, sale_id: int):
        super(WriteOffDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销负信息录入')
        self.stock = stock
        self.sale_number = sale_number
        self.sale_id = sale_id
        self._init_input_info()
        self._init_validator()

        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.pushButton.clicked.connect(self._commit_write_off)
        self.supplier_combo.activated.connect(self._add_supplier)

        self.buy_number.textEdited.connect(self._update_total)
        self.unit_price.textEdited.connect(self._update_total)
        self.total.textChanged.connect(self._update_unpaid)
        self.paid.textEdited.connect(self._update_unpaid)

    def _init_input_info(self):
        self.buy_date.setDisplayFormat('yyyyMMdd')
        self.buy_date.setDateTime(QDateTime.currentDateTime())
        self.brand.setText(self.stock.brand_name())
        self.model.setText(self.stock.model_name())
        self.unit.setText(self.stock.unit())
        self.sold_number.setText(self.sale_number)
        self.buy_number.setText(str(abs(self.stock.balance())))

        suppliers = supplier_handler.get_all_supplier()
        for supplier in suppliers:
            self.supplier_combo.addItem(supplier[1], supplier[0])
        self.supplier_combo.addItem('点击新增')

        self.first_service.setText(self.stock.first_service_name())
        self.second_service.setText(self.stock.second_service_name())
        self.paid.setText('0.0')
        self.unpaid.setText('0.0')
        self.unit_price.setText('0.0')
        self.total.setText('0.0')
        self.first_service.setText(self.stock.first_service_name())
        self.second_service.setText(self.stock.second_service_name())

        payments = Payment.get_payment_method()
        payment_combo = self.payment_method_combo
        for payment in list(payments.keys()):
            payment_combo.addItem(payments[payment], payment)

    def _init_validator(self):
        # int类型输入限制
        StaticFunc.set_validator(self.buy_number, 'int')

        # Float类型显示
        StaticFunc.set_validator(self.unit_price, 'float')
        StaticFunc.set_validator(self.paid, 'float')

    def _add_supplier(self):
        if self.supplier_combo.currentData():
            return

        supplier_name, ok = QInputDialog.getText(self.supplier_combo, '新增供应商', '请输入供应商:', QLineEdit.Normal, '')

        while ok and self.supplier_combo.findText(supplier_name) >= 0:
            QMessageBox.warning(self.pushButton, "提示", '供应商已经存在，请重新填写！')
            supplier_name, ok = QInputDialog.getText(self.supplier_combo, '新增供应商', '请输入供应商:', QLineEdit.Normal,
                                                     supplier_name)
        if ok and supplier_name:
            supplier_id = supplier_handler.add_supplier(supplier_name)
            self.supplier_combo.insertItem(self.supplier_combo.count() - 1, supplier_name, supplier_id)
            self.supplier_combo.setCurrentIndex(self.supplier_combo.count() - 2)

    # 金额小计自动计算
    def _update_total(self):
        number = self.buy_number.text()
        buy_price = self.unit_price.text()

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

    def _commit_write_off(self):
        # 校验必填项
        msg = self._check_required()
        if msg:
            QMessageBox.warning(self.pushButton, "提示", msg)
            return

        try:
            # 更新品牌和型号
            if not self._update_brand():
                QMessageBox.warning(self.pushButton, "提示", '品牌已经存在，请重新修改品牌')
                return

            if not self._update_model():
                QMessageBox.warning(self.pushButton, "提示", '型号已经存在，请重新修改型号')
                return

            db_transaction_util.begin()

            # 新增进货信息
            buy_id = self._add_buy_info()

            # 更新库存明细
            self._update_stock_detail(buy_id)

            # 更新库存
            self._update_stock_info()

            # 新增付款明细
            self._add_payment_detail(buy_id)

            db_transaction_util.commit()

            QMessageBox.information(self.pushButton, "提示", '销负录入成功！')

            self.close()

        except Exception as e:
            print(e)
            print('traceback.print_exc():{}'.format(traceback.print_exc()))
            print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
            QMessageBox.warning(self.pushButton, "提示", '销负信息录入失败！')
            db_transaction_util.rollback()

        # 修改销售信息中的品牌和型号

    def _add_buy_info(self):
        buy_info = BuyInfo()

        buy_date = self.buy_date.date().toString('yyyy-MM-dd')
        buy_info.buy_date(buy_date)

        buy_info.stock_id(self.stock.id())

        supplier_id = self.supplier_combo.currentData()
        buy_info.supplier_id(supplier_id)

        unit_price = Decimal(self.unit_price.text())
        buy_info.unit_price(unit_price)

        number = int(self.buy_number.text())
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

        notes = self.notes.text()
        buy_info.notes(notes)

        return buy_handler.add_buy_info(buy_info)

    def _update_stock_detail(self, buy_id: int):
        # 更新负库存明细
        balance = abs(self.stock.balance())

        unit_price = Decimal(self.unit_price.text())
        stock_id = self.stock.id()
        stock_detail_handler.write_off_negative_on_hand(stock_id, buy_id, unit_price, self.sale_id)

        # 进货数量扣除负库存后，确定新增正向库存明细数量
        need_add_number = int(self.buy_number.text()) - balance
        if need_add_number:
            stock_detail = StockDetail()
            stock_detail.buy_id(buy_id).buy_price(unit_price)

            stock_detail.stock_id(stock_id)

            stock_detail.update_time(get_now()).update_op(Common.config.login_user_info[0])

            for i in range(int(self.buy_number.text()) - balance):
                stock_detail_handler.add_stock_detail(stock_detail)

    def _update_stock_info(self):
        total = Decimal(self.total.text())
        buy_number = int(self.buy_number.text())

        stock_handler.update_stock_balance(self.stock.id(), buy_number, total)

    def _add_payment_detail(self, buy_id: int):
        payment_method = int(self.payment_method_combo.currentData())
        paid = Decimal(self.paid.text())
        unpaid = Decimal(self.unpaid.text())

        payment = Payment()

        payment.buy_id(buy_id)
        payment.paid(paid)
        payment.unpaid(unpaid)
        payment.payment_method(payment_method)

        payment_handler.add_payment_detail(payment)

    def _update_brand(self):
        brand_name = self.brand.text()
        if brand_name != self.stock.brand_name():
            brand = brand_handler.get_brand_by_name(brand_name)
            if brand:
                return False
            else:
                brand_handler.update_brand(self.stock.brand_id(), brand_name)
                stock_handler.update_brand_name(self.stock.id(), brand_name)

        return True

    def _update_model(self):
        model_name = self.model.text()
        if model_name != self.stock.model_name():
            model = model_handler.get_model_by_name(model_name, self.stock.brand_id())
            if model:
                return False
            else:
                model_handler.update_model(self.stock.model_id(), model_name)
                stock_handler.update_model_name(self.stock.id(), model_name)

        return True

    def _check_required(self):
        msg = ''
        if not self.brand.text():
            msg += '商品品牌、'

        if not self.model.text():
            msg += '商品型号、'

        if not int(self.buy_number.text()):
            msg += '进货数量、'

        if not Decimal(self.unit_price.text()):
            msg += '进货单价、'

        if not self.supplier_combo.currentData():
            msg += '供应商、'

        if not Decimal(self.paid.text()):
            msg += '未付金额、'

        if msg:
            msg = '属性：[' + msg[:-1] + '] 未填写，请填写后重新提交！'

        return msg
