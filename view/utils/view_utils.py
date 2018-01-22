from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QLineEdit, QCompleter, QWidget, QMessageBox, QComboBox, QPushButton, QInputDialog

from controller.view_service import supplier_service, brand_and_model_service
from database.dao.dictionary import dictionary_handler
from domain.payment import Payment


def set_validator(edit: QLineEdit, value_type: str):
    validator = None
    if value_type == 'int':
        validator = QIntValidator()
    elif value_type == 'float':
        validator = QDoubleValidator()
    edit.setValidator(validator)


def set_completer(editor: QWidget, title: str):
    if isinstance(editor, QLineEdit):
        if title in ('brand', 'model', 'supplier'):
            completer_list = []
            if title == 'brand':
                completer_list = brand_and_model_service.get_all_brand()
            if title == 'model':
                completer_list = brand_and_model_service.get_all_model()
            if title == 'supplier':
                completer_list = supplier_service.get_all_supplier()

            completer = QCompleter(completer_list)
            completer.setFilterMode(Qt.MatchContains)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            editor.setCompleter(completer)


def add_new_payment_method(combo_box: QComboBox, button: QPushButton):
    payment_method, ok = QInputDialog.getText(button, '新增付款方式', '请输入付款方式')
    if ok and not payment_method:
        QMessageBox.warning(button, '警告', '付款方式不能为空，请重新添加！')
        return
    if not ok:
        return
    exist_num = dictionary_handler.get_count_by_group_and_value(Payment.group_name(), payment_method)
    if exist_num:
        QMessageBox.warning(button, '警告', '付款方式已经存在，请重新添加！')
        return
    key_id = dictionary_handler.get_max_key_id_by_group_name(Payment.group_name()) + 1
    dictionary_handler.add_dictionary(key_id, payment_method, Payment.group_name())
    QMessageBox.warning(button, '提示', '付款方式添加成功！')
    combo_box.insertItem(0, payment_method, key_id)
    combo_box.setCurrentIndex(0)


def get_all_payment(combo_box: QComboBox):
    payments = dictionary_handler.get_key_and_value_by_group_name(Payment.group_name())
    for k_v in payments:
        combo_box.addItem(k_v['value_desc'], k_v['key_id'])
