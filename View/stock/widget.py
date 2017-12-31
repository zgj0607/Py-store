from PyQt5 import QtWidgets

from View.stock.ui_widget import Ui_Form


class TestForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(TestForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('test')

