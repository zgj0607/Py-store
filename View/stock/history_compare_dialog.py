from PyQt5 import QtWidgets

from View.stock.ui.ui_history_compare_dialog import Ui_historystockDialog


class Diglog_historystock(QtWidgets.QDialog, Ui_historystockDialog):
    def __init__(self):
        super(Diglog_historystock, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self._retranslateUi)

    def _retranslateUi(self):
        self.retranslateUi
