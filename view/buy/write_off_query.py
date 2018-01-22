import logging
import traceback
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QCompleter

from common import time_utils
from controller.view_service import buy_service, supplier_service, brand_and_model_service, stock_service
from database.dao.stock import stock_detail_handler, stock_handler
from domain.stock_detail import StockDetail
from view.buy.ui.ui_write_off_query import Ui_writeOffForm
from view.utils import table_utils, view_utils, db_transaction_util

logger = logging.getLogger(__name__)


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
        view_utils.get_all_payment(self.payment)
        self.payment.addItem('点击新增')
        completer = QCompleter(supplier_service.get_all_supplier())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.supplier.setCompleter(completer)
        view_utils.set_validator(self.price, 'float')
        view_utils.set_validator(self.unpaid, 'float')

    def _init_signal_and_slot(self):
        self.buy_number.valueChanged.connect(self._text_edit)
        self.price.textEdited.connect(self._text_edit)
        self.paid.textEdited.connect(self._text_edit)
        self.writeOffButton.clicked.connect(self.do_write_off)
        self.write_off_table.clicked['QModelIndex'].connect(self.show_detail)
        self.payment.activated['int'].connect(self._need_add_payment)

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

        # 计算剩余量
        if self.balance < 0:
            left_number = buy_number + self.balance
        else:
            left_number = buy_number

        try:
            db_transaction_util.begin()

            # 更新库存中的商品信息
            brand_id = brand_and_model_service.get_brand_by_name(brand_name)
            model_id = brand_and_model_service.get_model_by_name(brand_id, model_name)
            stock_handler.update_brand_name(self.stock_id, brand_name)
            stock_handler.update_brand_id(self.stock_id, brand_id)
            stock_handler.update_model_name(self.stock_id, model_name)
            stock_handler.update_model_id(self.stock_id, model_id)

            # 更新库存
            stock_service.update_stock_info(self.stock_id, left_number, Decimal(left_number) * price)

            # 新增进货信息
            supplier_id = supplier_service.get_supplier_by_name(self.supplier.text())

            buy_id = buy_service.add_buy_info(self.stock_id, supplier_id, price, buy_number, buy_date, unpaid, paid,
                                              total, payment, note, left_number)

            # 新增进货库存明细
            stock_service.add_stock_detail(self.stock_id, buy_id, total, buy_number, StockDetail.by_bought())

            # 更新销售库存明细状态
            stock_detail_handler.update_negative_info(self.sale_id, total)

            # 更新供应商付款信息
            supplier_service.add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment)

            db_transaction_util.commit()
            QMessageBox.information(self.writeOffButton, "提示", '销负成功！')
            self._clear_detail()
            self._init_write_off_table()
        except Exception as e:
            logger.error(e.__str__())
            logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
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

        if not self.payment.currentData():
            msg += '付款方式未选择\n'

        return msg

    def _need_add_payment(self, index):
        combo_box = self.sender()
        if index == combo_box.count() - 1:
            view_utils.add_new_payment_method(combo_box, self.writeOffButton)
