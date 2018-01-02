# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.inventory.ui.ui_inventory_unsalable_warning import Ui_inventoryunsalablewarningForm
from View.stock.history_compare_dialog import Diglog_historystock


class inventory_unsalable_warninForm(QtWidgets.QWidget, Ui_inventoryunsalablewarningForm):
    def __init__(self):
        super(inventory_unsalable_warninForm, self).__init__()
        self.setupUi(self)
        self.exportButton.clicked.connect(self.export)
        self.setWindowTitle('滞销库存预警')
    def _retranslateUi(self):
        print('123')

    def export(self):
        dialog = Diglog_historystock()
        dialog.show()
        dialog.exec()
        # stockForm.




