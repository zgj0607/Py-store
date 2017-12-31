from PyQt5 import QtWidgets

from View.statics.ui_performance import Ui_Form as UiPerformance


class Performance(QtWidgets.QWidget, UiPerformance):
    def __init__(self):
        super(Performance, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('业绩报表')