from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QCompleter

from Common import time_utils, Common
from View.buy.ui.ui_write_off_query import Ui_writeOffForm
from View.utils import table_utils, pyqt_utils, db_transaction_util
from database.dao.buy import payment_handler, buy_handler
from database.dao.stock import stock_detail_handler, brand_handler, model_handler, stock_handler
from database.dao.supplier import supplier_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock_detail import StockDetail


class WriteOff(QtWidgets.QWidget, Ui_writeOffForm):
    def __init__(self):
        super(WriteOff, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销负进货信息')

        self.table_title = ('序号', '销售日期', '商品品牌', '商品型号', '销售数量', '库存数量', '单位',
                            '品牌ID', '型号ID', '库存ID', '一级项目', '一级项目ID', '二级项目', '二级项目ID', '操作')

        self.sale_id = 0
        self.stock_id = 0
        self.brand_id = 0
        self.model_id = 0
        self.balance = 0

        self._init_write_off_table()

        self._init_ui()

        self._init_signal_and_slot()

    def _init_write_off_table(self):
        write_off_date = stock_detail_handler.get_negative_on_hand()
        table_utils.set_table_content(self.write_off_table, write_off_date, self.table_title)
        self.write_off_table.setColumnHidden(7, True)
        self.write_off_table.setColumnHidden(8, True)
        self.write_off_table.setColumnHidden(9, True)
        self.write_off_table.setColumnHidden(11, True)
        self.write_off_table.setColumnHidden(13, True)
        self.write_off_table.horizontalHeader().setStretchLastSection(True)

    # 初始化界面Ui显示内容
    def _init_ui(self):
        Payment.add_all_payment(self.payment)
        completer = QCompleter(self._get_all_supplier())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.supplier.setCompleter(completer)
        pyqt_utils.set_validator(self.price, 'float')
        pyqt_utils.set_validator(self.unpaid, 'float')

    def _init_signal_and_slot(self):
        self.buy_number.valueChanged.connect(self._text_edit)
        self.price.textEdited.connect(self._text_edit)
        self.paid.textEdited.connect(self._text_edit)
        self.writeOffButton.clicked.connect(self.do_write_off)
        self.write_off_table.clicked['QModelIndex'].connect(self.show_detail)

    # 显示待销负明细
    def show_detail(self, index: QModelIndex):
        if index.column() != 14:
            return
        self.sale_id = table_utils.get_table_cell(self.write_off_table, index.row(), 0)
        self.stock_id = table_utils.get_table_current_index_info(self.write_off_table, 9)
        self.brand_id = table_utils.get_table_current_index_info(self.write_off_table, 7)
        self.model_id = table_utils.get_table_current_index_info(self.write_off_table, 8)

        self.buy_date.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self.brand.setText(table_utils.get_table_current_index_info(self.write_off_table, 2))
        self.model.setText(table_utils.get_table_current_index_info(self.write_off_table, 3))
        self.sale_number.setText(table_utils.get_table_current_index_info(self.write_off_table, 4))
        balance = int(table_utils.get_table_current_index_info(self.write_off_table, 5))
        self.buy_number.setValue(abs(balance))
        self.unit.setText(table_utils.get_table_current_index_info(self.write_off_table, 6))
        self.service.setText(table_utils.get_table_current_index_info(self.write_off_table, 10) + '-' +
                             table_utils.get_table_current_index_info(self.write_off_table, 12))
        self.price.setText('0.0')
        self.total.setText('0.0')
        self.paid.setText('0.0')
        self.unpaid.setText('0.0')

        self.balance = balance

        # self._init_write_off_table()

    def _clear_detail(self):
        self.buy_date.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self.brand.clear()
        self.model.clear()
        self.sale_number.clear()
        self.buy_number.setValue(abs(int(table_utils.get_table_current_index_info(self.write_off_table, 5))))
        self.unit.clear()
        self.service.clear()
        self.price.setText('0.0')
        self.total.setText('0.0')
        self.paid.setText('0.0')
        self.unpaid.setText('0.0')
        self.sale_id = 0
        self.stock_id = 0
        self.brand_id = 0
        self.model_id = 0
        self.balance = 0

    def _text_edit(self):
        edited_editor = self.sender()
        attr_name = edited_editor.objectName()

        buy_number = Decimal(self.buy_number.value())
        price = self.price.text()
        if price:
            price = Decimal(price)
        else:
            price = Decimal(0.0)
        paid = self.paid.text()
        if paid:
            paid = Decimal(paid)
        else:
            paid = Decimal(0.0)

        total_editor = self.total
        unpaid_editor = self.unpaid
        total = price * buy_number
        unpaid = total - paid
        if attr_name in ('buy_number', 'price'):
            total_editor.setText(str(total))
            unpaid_editor.setText(str(unpaid))

        if attr_name == 'paid':
            unpaid_editor.setText(str(unpaid))

    # 销负
    def do_write_off(self):
        if not self.sale_id:
            QMessageBox.information(self.writeOffButton, "提示", '请选择需要销负的记录！')
            return
        msg = self._check_required()
        if msg:
            QMessageBox.information(self.writeOffButton, "提示", msg)
            return
        brand_name = self.brand.text()
        model_name = self.model.text()
        buy_number = self.buy_number.value()
        price = Decimal(self.price.text())
        paid = self.paid.text()
        if paid:
            paid = Decimal(paid)
        else:
            paid = Decimal(0.0)
        unpaid = Decimal(self.unpaid.text())
        total = Decimal(self.total.text())
        note = self.note.text()
        payment = int(self.payment.currentData())
        buy_date = self.buy_date.date().toString('yyyy-MM-dd')

        try:
            db_transaction_util.begin()

            # 更新库存中的商品信息
            brand_id = self._get_brand(brand_name)
            model_id = self._get_model(brand_id, model_name)
            stock_handler.update_brand_name(self.stock_id, brand_name)
            stock_handler.update_brand_id(self.stock_id, brand_id)
            stock_handler.update_model_name(self.stock_id, model_name)
            stock_handler.update_model_id(self.stock_id, model_id)

            # 更新库存
            self._update_stock_info(self.stock_id, buy_number, total)

            # 新增进货信息
            supplier_id = self._get_supplier(self.supplier.text())
            buy_id = self._add_buy_info(self.stock_id, supplier_id, price, buy_number, buy_date, unpaid, paid, total,
                                        payment, note, self.balance)

            # 新增进货库存明细
            self._add_stock_detail(self.stock_id, buy_id, total, buy_number)

            # 更新销售库存明细状态
            stock_detail_handler.update_negative_info(self.sale_id, total)

            # 更新供应商付款信息
            self._add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment)

            db_transaction_util.commit()
            QMessageBox.information(self.writeOffButton, "提示", '销负成功！')
            self._clear_detail()
            self._init_write_off_table()
        except Exception as e:
            print(e)
            db_transaction_util.rollback()
            QMessageBox.information(self.writeOffButton, "提示", '销负失败，请重试！\n' + e.__str__())

    def _check_required(self):
        msg = ''

        if self.buy_number.value() < abs(self.balance):
            msg += '进货数量必须大于等于负库存数量：' + str(self.balance) + '\n'

        if not self.brand.text():
            msg += '商品品牌不能为空\n'

        if not self.model.text():
            msg += '商品型号不能为空\n'

        if not self.price.text() or not Decimal(self.price.text()):
            msg += '进货单价不能为空或零\n'

        if not self.supplier.text():
            msg += '供应商不能为空\n'

        return msg

    @staticmethod
    def _get_supplier(name):
        supplier_in_db = supplier_handler.get_supplier_by_name(name)
        if supplier_in_db:
            return supplier_in_db[0]
        else:
            return supplier_handler.add_supplier(name)

    @staticmethod
    def _get_all_supplier():
        suppliers = []
        for supplier in supplier_handler.get_all_supplier():
            suppliers.append(supplier[1])
        return suppliers

    @staticmethod
    def _get_brand(name: str):
        brand_in_db = brand_handler.get_brand_by_name(name)
        if brand_in_db:
            return brand_in_db[0]
        else:
            return brand_handler.add_brand(name)

    @staticmethod
    def _get_model(brand_id, model_name):
        model_in_db = model_handler.get_model_by_name(model_name, brand_id)
        if model_in_db:
            return model_in_db[0]
        else:
            return model_handler.add_model(model_name, brand_id)

    @staticmethod
    def _add_stock_detail(stock_id, buy_id, total, number):
        stock_detail = StockDetail()
        stock_detail.changed_id(buy_id)
        stock_detail.changed_money(abs(total))
        stock_detail.changed_number(abs(number))
        stock_detail.stock_id(stock_id)
        if number < 0:
            stock_detail.type(stock_detail.by_returned())
        else:
            stock_detail.type(StockDetail.by_bought())

        stock_detail.update_time(time_utils.get_now()).update_op(Common.config.login_user_info[0])
        stock_detail_handler.add_stock_detail(stock_detail)

    @staticmethod
    def _update_stock_info(stock_id: int, balance: int, total: Decimal):
        stock_handler.update_stock_balance(stock_id, balance, total)

    @staticmethod
    def _add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment_method, is_return=False):

        payment = Payment()
        payment.buy_id(buy_id)
        payment.supplier_id(supplier_id)
        payment.payment_method(payment_method)
        payment.paid(paid)
        payment.unpaid(unpaid)
        payment.create_op(Common.config.login_user_info[0])
        payment.create_time(time_utils.get_now())

        if is_return:
            payment.refund_type(Payment.returned())
        else:
            payment.refund_type(Payment.payoff())

        payment_handler.add_payment_detail(payment)

        if unpaid:
            supplier_handler.update_supplier_unpaid(supplier_id, unpaid)

    @staticmethod
    def _add_buy_info(stock_id, supplier_id, price, number, buy_date, unpaid, paid, total, payment, note, balance):
        buy_info = BuyInfo()
        buy_info.buy_date(buy_date)
        buy_info.stock_id(stock_id)
        buy_info.supplier_id(supplier_id)
        buy_info.unit_price(price)
        buy_info.payment_method(payment)

        buy_info.number(abs(number))

        create_time = time_utils.get_now()
        buy_info.create_time(create_time)
        create_op = Common.config.login_user_info[0]
        buy_info.create_op(create_op)

        buy_info.paid(abs(paid))
        buy_info.unpaid(abs(unpaid))
        buy_info.total(abs(total))

        buy_info.note(note)
        buy_info.buy_type(BuyInfo.bought())
        # 计算剩余量
        if balance < 0:
            left_number = number + balance
        else:
            left_number = number

        buy_info.left(left_number)

        return buy_handler.add_buy_info(buy_info)
