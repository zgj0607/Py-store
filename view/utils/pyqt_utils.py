from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QLineEdit


def set_validator(edit: QLineEdit, type: str):
    validator = None
    if type == 'int':
        validator = QIntValidator()
    elif type == 'float':
        validator = QDoubleValidator()
    edit.setValidator(validator)
