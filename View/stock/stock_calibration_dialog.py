from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Common import time_utils, Common
from View.stock.ui.ui_stock_calibration_dialog import Ui_stock_calibrationDialog
from View.utils import db_transaction_util
from database.dao.buy import payment_handler, buy_handler
from database.dao.stock import brand_handler, model_handler
from PyQt5.QtCore import QDateTime
from domain.stock import Stock
from database.dao.stock import stock_handler
from domain.buy import BuyInfo

class stock_calibrationDialog(QtWidgets.QDialog, Ui_stock_calibrationDialog):
    def __init__(self):
        super(stock_calibrationDialog, self).__init__()
        self.setupUi(self)
        self._init_brand()
        self._init_staffComb()
        self.setWindowTitle('请填写校准信息')
        time_now = time_utils.get_now()
        self.dateEdit.setDateTime(QDateTime.fromString(time_now, 'yyyy-MM-dd hh:mm:ss'))
        self.addButton.clicked.connect(self._submit)
        # self._init_input_info(buy)
        # self._init_signal_and_slot()
        #
        # self.buy_id = buy.buy_id()


    def _pay_changed(self):
        pay = Decimal(self.pay.text())
        need_pay = Decimal(self.need_pay.text())

        changed = need_pay - pay

        self.unpaid.setText(str(changed))

    def do_pay(self):

        unpaid = Decimal(self.unpaid.text())
        if unpaid < 0:
            QMessageBox.information(self.payButton, '提示', '付款额度超过未付款额度，请重新填写！')
            return
        pay = Decimal(self.pay.text())
        note = self.notes.text()
        paid = Decimal(self.paid.text())
        new_paid = paid + pay
        try:
            db_transaction_util.begin()

            # 新增付款明细
            self._add_payment_detail(new_paid, unpaid)
            # 更新进货付款信息
            self._update_buy_pay_info(new_paid, unpaid, note)

            db_transaction_util.commit()

            QMessageBox.information(self.payButton, '提示', '付款成功！')
            self.close()

        except Exception as e:
            print(e)
            db_transaction_util.rollback()
            QMessageBox.information(self.payButton, '提示', '付款失败！')

    def _submit(self):
        # stock = Stock()
        #
        # brand = self.brand_combo
        # stock.brand_name(brand.currentText()).brand_id(brand.currentData())
        #
        # model = self.model_combo
        # stock.model_name(model.currentText()).model_id(model.currentData())
        #
        # name = brand.currentText() + '-' + model.currentText()
        # stock.name(name)
        # # stock.unit(self.unit.text())
        # stock.create_op(self.staffComb.currentData())
        # stock.create_time(self.dateEdit.text())
        #
        # stock_id = stock_handler.add_stock_info(stock)
        model = self.model_combo
        stock_info = stock_handler.get_stock_by_model(model.currentData())
        buy_info = BuyInfo()
        buy_info.buy_date(self.dateEdit.text())
        buy_info.stock_id(stock_info[0])
        buy_info.supplier_id("99999")
        buy_info.unit_price(Decimal(self.money.text()))

        create_time = time_utils.get_now()
        buy_info.create_time(create_time)
        create_op = self.staffComb.currentData()
        buy_info.create_op(create_op)

        # buy_info.paid(abs(paid))
        # buy_info.unpaid(abs(unpaid))
        buy_info.total(Decimal(self.toal.text()))

        buy_info.note(self.notes.text())
        buy_info.buy_type("8")
        buy_handler.add_buy_info(buy_info)
        QMessageBox.information(self.addButton, '提示', '校准成功！')
        self.close()

    def _update_buy_pay_info(self, paid: float, unpaid: float, notes: str):
        buy_handler.update_paid_info(self.buy_id, unpaid, paid, notes)

    def _init_staffComb(self):
        brands = brand_handler.get_all_staff()
        for brand in brands:
            self.staffComb.addItem(brand[1], brand[0])

    def _init_brand(self):
        brands = brand_handler.get_all_brand()
        for brand in brands:
            self.brand_combo.addItem(brand[1], brand[0])
        if brands:
            brand_id = brands[0][0]
            self._refresh_model(brand_id)
        self.brand_combo.currentIndexChanged.connect(self._brand_index_changed)
    def _brand_index_changed(self):
        self._refresh_model()
        self.brand_edited = False
        self.model_edited = False

    def _refresh_model(self, brand_id=0):
        if not brand_id:
            brand_id = self.brand_combo.currentData()
        if brand_id:
            brand_id = int(brand_id)
            models = model_handler.get_model_by_brand(brand_id)
            self.model_combo.clear()
            for model in models:
                self.model_combo.addItem(model[1], model[0])


