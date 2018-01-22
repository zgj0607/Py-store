import logging
import traceback
from collections import OrderedDict
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QComboBox

from common import time_utils, static_func
from controller.view_service import supplier_service, brand_and_model_service, buy_service, stock_service
from database.dao.service import service_handler
from domain.stock_detail import StockDetail
from view.buy.ui.ui_normal_buy_add import Ui_stockQueryForm
from view.utils import view_utils, db_transaction_util

logger = logging.getLogger(__name__)


class NormalBuyAdd(QtWidgets.QWidget, Ui_stockQueryForm):
    def __init__(self):
        super(NormalBuyAdd, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('普通进货录入')

        self.line_title = (
            'seq', 'buy_date', 'brand', 'model', 'number', 'unit', 'price', 'total', 'supplier', 'first_service',
            'second_service', 'paid', 'unpaid', 'payment', 'note', 'remove'
        )

        self.edit_type = (
            'QLabel', 'QDateEdit', 'QLineEdit', 'QLineEdit', 'QSpinBox', 'QLineEdit', 'QLineEdit', 'QLineEdit',
            'QLineEdit', 'QComboBox', 'QComboBox', 'QLineEdit', 'QLineEdit', 'QComboBox', 'QLineEdit', 'QPushButton'
        )

        self.title_desc = (
            '序号', '进货日期', '商品品牌', '商品型号', '进货数量', '单位', '进货单价', '单品小计', '供应商', '一级项目', '二级项目',
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
        self.payment_1.activated['int'].connect(self._need_add_payment)
        self.first_service_1.activated.connect(self._add_all_service_item)
        self.second_service_1.activated.connect(self._add_all_service_item)
        self.first_service_1.currentIndexChanged.connect(self._first_service_changed)

    def _init_first_line(self):
        self.line_number = 1
        self.buy_date_1.setDateTime(QDateTime.fromString(time_utils.get_now(), 'yyyy-MM-dd hh:mm:ss'))
        self._add_all_service_item(self.first_service_1)
        self._add_all_service_item(self.second_service_1)
        view_utils.get_all_payment(self.payment_1)
        self.payment_1.addItem('点击新增')
        for title in self.line_title:
            name = title + '_' + '1'
            editor = getattr(self, name)
            view_utils.set_completer(editor, title)
        view_utils.set_validator(self.price_1, 'float')
        view_utils.set_validator(self.paid_1, 'float')
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
            editor = static_func.create_instance('PyQt5.QtWidgets.' + self.edit_type[index])
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
                view_utils.set_validator(editor, 'float')
                editor.textEdited.connect(self._text_edit)
                editor.setText('0.0')

            if title == 'number':
                editor.valueChanged.connect(self._text_edit)

            if title in ('first_service', 'second_service'):
                self._add_all_service_item(editor)
                editor.activated.connect(self._add_all_service_item)
                if title == 'first_service':
                    editor.currentIndexChanged.connect(self._first_service_changed)

            if title == 'payment':
                view_utils.get_all_payment(editor)
                editor.addItem('点击新增')
                editor.activated['int'].connect(self._need_add_payment)

            view_utils.set_completer(editor, title)
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
            delattr(self, editor_name)

        self.buy_info_container.removeItem(buy_info)
        delattr(self, attr_name)
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
            if title in ('seq', 'remove', 'payment'):
                continue
            if title.endswith('service'):
                editor.clear()
                self._add_all_service_item(editor)
                continue

            editor.clear()

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
        total = total_editor.text()
        if not total:
            total = 0.0
        else:
            total = Decimal(total)

        if attr_name in ('number', 'price'):
            new_total = price * number
            total_editor.setText(str(new_total))
            new_unpaid = new_total - paid
            unpaid_editor.setText(str(new_unpaid))

        if attr_name == 'paid':
            new_unpaid = total - paid
            unpaid_editor.setText(str(new_unpaid))

    def do_add(self):
        succeeded_list = '成功录入的行数：\n'
        failed_dict = OrderedDict()
        for row_index in range(1, self.line_number + 1):
            # 如果没有这个对应的序号属性，则说明已经删除，继续处理下一条记录
            if not hasattr(self, 'seq_' + str(row_index)):
                print(row_index)
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

                brand_id = brand_and_model_service.get_brand_by_name(brand)

                model_id = brand_and_model_service.get_model_by_name(brand_id, model)

                supplier_id = supplier_service.get_supplier_by_name(supplier)

                stock_info = stock_service.get_stock_by_model(model_id)

                # 如果通过型号找到库存，则单位属性沿用库存中的单位，并更新库存总额和库存量
                if stock_info:
                    stock_id = stock_info[0]
                else:
                    # 新增库存信息
                    second_service = getattr(self, 'second_service_' + line_number)
                    second_service_id = int(second_service.currentData())
                    stock_info = stock_service.add_stock_info(model, brand, model_id, brand_id, unit, second_service_id)
                    stock_id = stock_info.id()

                stock_service.update_stock_info(stock_id, number, total)

                # 新增进货信息
                buy_id = buy_service.add_buy_info(stock_id, supplier_id, price, number, buy_date, unpaid, paid, total,
                                                  payment, note, number)

                change_type = StockDetail.by_bought()
                # 如果是退货，更新原来的进货信息中剩余量
                if number < 0:
                    buy_service.decrease_buy_left(stock_id, number)
                    buy_service.update_buy_unpaid(stock_id, total, supplier_id, payment)
                    change_type = StockDetail.by_returned()
                # 新增库存明细
                stock_service.add_stock_detail(stock_id, buy_id, total, number, change_type)

                # 新增供应商支付信息，如果数量大于0，则为进货，小于零则为退货
                supplier_service.add_supplier_payment_detail(buy_id, supplier_id, paid, unpaid, payment, number < 0)

                db_transaction_util.commit()
                succeeded_list = succeeded_list + '第' + line_number + '行、'
                self.do_remove(line_number)
            except Exception as e:
                logger.error(e.__str__())
                logger.error('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                failed_dict[line_number] = e.__str__()
                db_transaction_util.rollback()

        failed_info = '\n未成功录入的行数：\n'
        for key in list(failed_dict.keys()):
            failed_info += '第' + key + '行数据：' + failed_dict[key]

        succeeded_list += '\n' + failed_info
        QMessageBox.information(self.submit, '提示', succeeded_list)

    def _check_required(self, line_number: str):
        msg = ''
        for index, title in enumerate(self.line_title):
            editor = getattr(self, title + '_' + line_number)
            if title in ('seq', 'buy_date', 'remove', 'note', 'first_service'):
                continue

            if title in ('second_service', 'payment'):
                if not editor.currentData():
                    msg += self.title_desc[index] + '未选择\n'
                continue

            if title == 'number':
                number = editor.value()
                if not number:
                    msg = self.title_desc[index] + '不能为零\n'
                continue

            if title == 'price':
                price = editor.text()
                if not price or not Decimal(price):
                    msg += self.title_desc[index] + '不能为零或空\n'
                continue

            text = editor.text()

            if not text:
                msg += self.title_desc[index] + '不能为空\n'

        return msg

    def _first_service_changed(self, index):
        first_service = self.sender()
        obj_name_seg = first_service.objectName().split('_')
        number = obj_name_seg[2]
        second_service = getattr(self, 'second_service_' + number)
        if not index:
            second_service.setCurrentIndex(0)
            return
        self._add_all_service_item(second_service)

    def _add_all_service_item(self, combo_box=None):
        if not isinstance(combo_box, QComboBox):
            combo_box = self.sender()
        obj_name_seg = combo_box.objectName().split('_')
        level = obj_name_seg[0]
        number = obj_name_seg[2]
        item_count = combo_box.count()

        if not item_count:
            combo_box.insertItem(0, '请选择')

        if level == 'first':
            services = service_handler.get_all_first_level_service()
        else:
            father_id = getattr(self, 'first_service_' + number).currentData()
            if father_id:
                services = service_handler.get_second_service_by_father(int(father_id))
            else:
                services = ()

        for service in services:
            if combo_box.findData(service['id'], flags=Qt.MatchExactly) == -1:
                combo_box.addItem(service['name'], service['id'])

        need_delete = []
        for index in range(1, combo_box.count()):
            cnt = 0
            for service in services:
                if service['id'] == int(combo_box.itemData(index)):
                    cnt += 1
                    break
            if not cnt:
                need_delete.append(index)
        for index, data in enumerate(need_delete):
            combo_box.removeItem(data - index)

    def _need_add_payment(self, index):
        combo_box = self.sender()
        if index == combo_box.count() - 1:
            view_utils.add_new_payment_method(combo_box, self.submit)
