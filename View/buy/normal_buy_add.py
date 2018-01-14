from collections import OrderedDict
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QWidget, QLineEdit, QCompleter, QComboBox

from Common import time_utils, Common, config
from View.buy.ui.ui_normal_buy_add import Ui_stockQueryForm
from View.utils import pyqt_utils, db_transaction_util
from database.dao.buy import buy_handler, payment_handler
from database.dao.service import service_handler
from database.dao.stock import stock_detail_handler, brand_handler, model_handler, stock_handler
from database.dao.supplier import supplier_handler
from domain.buy import BuyInfo
from domain.payment import Payment
from domain.stock import Stock
from domain.stock_detail import StockDetail


class NormalBuyAdd(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(NormalBuyAdd, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('普通进货录入')

        self.line_title = (
            'seq', 'buy_date', 'brand', 'model', 'number', 'unit', 'price', 'total', 'supplier', 'service', 'paid',
            'unpaid', 'payment', 'note', 'remove'
        )

        self.edit_type = (
            'QLabel', 'QDateEdit', 'QLineEdit', 'QLineEdit', 'QSpinBox', 'QLineEdit', 'QLineEdit', 'QLineEdit',
            'QLineEdit', 'QComboBox', 'QLineEdit', 'QLineEdit', 'QComboBox', 'QLineEdit', 'QPushButton'
        )

        self.title_desc = (
            '序号', '进货日期', '商品品牌', '商品型号', '进货数量', '单位', '进货单价', '单品小计', '供应商', '所属项目',
            '付款金额', '未付金额', '支付方式', '备注', '操作'
        )

        self._init_first_line()
        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.add.clicked.connect(self._add_new_line)
        self.remove_1.clicked.connect(self.do_remove)
        self.submit.clicked.connect(self.do_add)
        self.paid_1.textEdited.connect(self._text_edit)
        self.price_1.textEdited.connect(self._text_edit)
        self.number_1.valueChanged.connect(self._text_edit)

    def _init_first_line(self):
        self.line_number = 1
        self.buy_date_1.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self._add_all_service_item(self.service_1)
        Payment.add_all_payment(self.payment_1)
        for title in self.line_title:
            name = title + '_' + '1'
            editor = getattr(self, name)
            self._set_completer(editor, title)
        pyqt_utils.set_validator(self.price_1, 'float')
        pyqt_utils.set_validator(self.paid_1, 'float')
        self.paid_1.setText('0.0')
        self.price_1.setText('0.0')
        self.total_1.setText('0.0')
        self.unpaid_1.setText('0.0')

    def _add_new_line(self):
        if self.buy_info_container.count() >= 11:
            QMessageBox.information(self.submit, "提示", '添加的行数过多，请提交后再做新增！')
            return

        self.line_number += 1
        line_number = str(self.line_number)
        buy_info_name = 'buy_info' + '_' + line_number
        setattr(self, buy_info_name, QtWidgets.QHBoxLayout())
        buy_info = getattr(self, buy_info_name)
        buy_info.setObjectName(buy_info_name)

        for index, title in enumerate(self.line_title):
            editor = self.create_instance('PyQt5.QtWidgets.' + self.edit_type[index])
            attr_name = title + '_' + line_number
            editor.setObjectName(attr_name)

            first_attr_name = title + '_' + '1'
            first_attr = getattr(self, first_attr_name)

            editor.setMinimumSize(getattr(first_attr, 'minimumSize')())
            editor.setMaximumSize(getattr(first_attr, 'maximumSize')())
            editor.setFont(getattr(first_attr, 'font')())

            if hasattr(first_attr, 'setClearButtonEnabled') and first_attr.isClearButtonEnabled():
                editor.setClearButtonEnabled(True)

            if title == 'buy_date':
                editor.setDisplayFormat("yyyy-MM-dd")
                editor.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))

            if title == 'remove':
                editor.setText('删除')
                editor.clicked.connect(self.do_remove)
                editor.setObjectName(attr_name)

            if title == 'seq':
                editor.setText(line_number)

            # 只读
            if title in ('total', 'unpaid'):
                editor.setReadOnly(first_attr.isReadOnly())
                editor.setEnabled(first_attr.isEnabled())
                editor.setText('0.0')

            if title in ('paid', 'price'):
                pyqt_utils.set_validator(editor, 'float')
                editor.textEdited.connect(self._text_edit)
                editor.setText('0.0')

            if title == 'number':
                editor.valueChanged.connect(self._text_edit)

            if title == 'service':
                self._add_all_service_item(editor)

            if title == 'payment':
                Payment.add_all_payment(editor)

            self._set_completer(editor, title)
            setattr(self, attr_name, editor)
            buy_info.addWidget(editor)
        self.buy_info_container.addLayout(buy_info)

    def do_remove(self, line_number=None):
        if not line_number:
            button = self.sender()
            line_number = button.objectName().split('_')[1]
        if line_number == '1':
            self._clear_first_line()
            return
        attr_name = 'buy_info_' + line_number
        buy_info = getattr(self, attr_name)

        for title in self.line_title:
            editor_name = title + '_' + line_number
            editor = getattr(self, editor_name)
            editor.hide()
            buy_info.removeWidget(editor)
            del editor

        self.buy_info_container.removeItem(buy_info)
        del buy_info

    def _clear_first_line(self):
        line_number = '1'
        for title in self.line_title:
            name = title + '_' + line_number
            editor = getattr(self, name)
            if title == 'buy_date':
                editor.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
                continue
            if title == 'number':
                editor.setValue(0)
                continue
            if title in ('seq', 'remove', 'payment', 'service'):
                continue
            editor.clear()
        QMessageBox.information(self.submit, "提示", '首行数据已经被重执！')

    def _set_completer(self, editor: QWidget, title: str):
        if isinstance(editor, QLineEdit):
            if title in ('brand', 'model', 'supplier'):
                completer_list = []
                if title == 'brand':
                    completer_list = self._get_all_brand()
                if title == 'model':
                    completer_list = self._get_all_model()
                if title == 'supplier':
                    completer_list = self._get_all_supplier()

                completer = QCompleter(completer_list)
                completer.setCaseSensitivity(Qt.CaseInsensitive)
                editor.setCompleter(completer)

    def _text_edit(self, text: str):
        editor = self.sender()
        obj_name = editor.objectName()
        names = obj_name.split('_')
        line_number = names[-1]
        attr_name = names[0]

        number_editor = getattr(self, 'number_' + line_number)

        number = number_editor.value()
        price_editor = getattr(self, 'price_' + line_number)
        price = Decimal(price_editor.text() if price_editor.text() else '0.0')
        paid_editor = getattr(self, 'paid_' + line_number)
        paid = Decimal(paid_editor.text() if paid_editor.text() else '0.0')
        unpaid_editor = getattr(self, 'unpaid_' + line_number)
        total_editor = getattr(self, 'total_' + line_number)
        total = Decimal(total_editor.text())

        if attr_name in ('number', 'price'):
            new_total = price * number
            total_editor.setText(str(new_total))
            new_unpaid = new_total - paid
            unpaid_editor.setText(str(new_unpaid))

        if attr_name == 'paid':
            new_unpaid = total - paid
            unpaid_editor.setText(str(new_unpaid))

    def do_add(self):
        succeeded_list = ''
        failed_dict = OrderedDict()
        for row_index in range(1, self.line_number + 1):
            # 如果没有这个对应的序号属性，则说明已经删除，继续处理下一条记录
            if not hasattr(self, 'seq_' + str(row_index)):
                continue

            line_number = getattr(self, 'seq_' + str(row_index)).text()
            msg = self._check_required(line_number)
            # 如果必填检查不通过，则将错误信息记录下来，继续处理下一条记录
            if msg:
                failed_dict[line_number] = msg
                continue

            # 提取所有表单项的值
            buy_date = getattr(self, 'buy_date_' + line_number).date().toString('yyyy-MM-dd')
            brand = getattr(self, 'brand_' + line_number).text()
            model = getattr(self, 'model_' + line_number).text()
            supplier = getattr(self, 'supplier_' + line_number).text()

            unit = getattr(self, 'unit_' + line_number).text()
            price = Decimal(getattr(self, 'price_' + line_number).text())
            number = getattr(self, 'number_' + line_number).value()
            total = Decimal(getattr(self, 'total_' + line_number).text())
            paid_value = getattr(self, 'paid_' + line_number).text()
            paid = Decimal(paid_value if paid_value else '0.0')
            unpaid = Decimal(getattr(self, 'unpaid_' + line_number).text())
            note = getattr(self, 'note_' + line_number).text()
            payment = int(getattr(self, 'payment_' + line_number).currentData())

            try:
                db_transaction_util.begin()

                brand_id = self._get_brand(brand)

                model_id = self._get_model(brand_id, model)

                supplier_id = self._get_supplier(supplier)

                stock_info = stock_handler.get_stock_by_model(model_id)

                # 如果通过型号找到库存，则单位属性沿用库存中的单位，并更新库存总额和库存量
                if stock_info:
                    stock_id = stock_info[0]
                    self._update_stock_info(stock_id, number, total)
                else:
                    # 新增库存信息
                    stock_id = self._add_stock_info(model, brand, model_id, brand_id, line_number, total, number, unit)

                # 新增进货信息
                buy_id = self._add_buy_info(stock_id, supplier_id, price, number, buy_date, unpaid, paid, total,
                                            payment, note)

                # 新增库存明细
                self._add_stock_detail(stock_id, buy_id, total, number)

                # 新增供应商支付信息，如果数量大于0，则为进货，小于零则为退货
                self._add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment, number < 0)

                db_transaction_util.commit()
                succeeded_list = succeeded_list + '第' + line_number + '行、'
            except Exception as e:
                print(e)
                failed_dict[line_number] = e.__str__()
                db_transaction_util.rollback()

        failed_info = '未新增：'
        for key in list(failed_dict.keys()):
            failed_info += '第' + key + '数据：' + failed_dict[key]

        succeeded_list += '\n' + failed_info
        QMessageBox.information(self.submit, '提示', succeeded_list)

    def _check_required(self, line_number: str):
        msg = ''
        for index, title in enumerate(self.line_title):
            editor = getattr(self, title + '_' + line_number)
            if title in ('seq', 'buy_date', 'remove', 'note', 'service', 'payment'):
                continue

            if title == 'number':
                number = editor.value()
                if not number:
                    msg = self.title_desc[index] + '不能为零\n'

            if title == 'price':
                price = editor.text()
                if not price or not Decimal(price):
                    msg += self.title_desc[index] + '不能为零或空\n'

            text = editor.text()

            if not text:
                msg += self.title_desc[index] + '不能为空\n'

        return msg

    @staticmethod
    def _add_buy_info(stock_id, supplier_id, price, number, buy_date, unpaid, paid, total, payment, note):
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
        # 判断是进货还是退货
        if number < 0:
            buy_info.buy_type(BuyInfo.returned())
        else:
            buy_info.buy_type(BuyInfo.bought())

        return buy_handler.add_buy_info(buy_info)

    def _add_stock_info(self, model, brand, model_id, brand_id, line_number, total, number, unit):
        service_id = getattr(self, 'service_' + line_number).currentData()
        service_name = getattr(self, 'service_' + line_number).currentText()
        stock_info = Stock()

        services = service_name.split('-')
        service_ids = service_id.split('-')

        first_service_id = int(service_ids[0])
        first_service_name = services[0]
        second_service_id = int(service_ids[1])
        second_service_name = services[1]

        stock_info.model_id(model_id).model_name(model)
        stock_info.brand_id(brand_id).brand_name(brand)
        stock_info.first_service_id(first_service_id).first_service_name(first_service_name)
        stock_info.second_service_id(second_service_id).second_service_name(second_service_name)
        stock_info.unit(unit).name(brand + '-' + model)
        stock_info.create_op(config.login_user_info[0]).create_time(time_utils.get_now())
        stock_info.total_cost(total).balance(number)

        stock_id = stock_handler.add_stock_info(stock_info)

        return stock_id

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
    def _get_all_brand():
        brands = []
        for brand in brand_handler.get_all_brand():
            brands.append(brand[1])

        return brands

    @staticmethod
    def _get_all_model():
        models = []
        for model in model_handler.get_all_model():
            models.append(model[1])
        return models

    @staticmethod
    def _get_all_supplier():
        suppliers = []
        for supplier in supplier_handler.get_all_supplier():
            suppliers.append(supplier[1])
        return suppliers

    @staticmethod
    def create_instance(class_name, *args, **kwargs):
        (module_name, class_name) = class_name.rsplit('.', 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        obj = class_meta(*args, **kwargs)
        return obj

    @staticmethod
    def _add_all_service_item(combo_box: QComboBox):
        for service in service_handler.get_all_second_level_service():
            name = service[1] + '-' + service[3]
            service_id = str(service[0]) + '-' + str(service[2])
            combo_box.addItem(name, service_id)

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
    def _get_supplier(name):
        supplier_in_db = supplier_handler.get_supplier_by_name(name)
        if supplier_in_db:
            return supplier_in_db[0]
        else:
            return supplier_handler.add_supplier(name)

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
