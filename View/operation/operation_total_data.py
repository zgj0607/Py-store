from PyQt5 import QtWidgets

from View.operation.ui.ui_operation_total_data import Ui_operationtotaldataForm


class OperationTotalData(QtWidgets.QWidget, Ui_operationtotaldataForm):
    def __init__(self):
        super(OperationTotalData, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('总体经营数据')

        self.search.clicked.connect(self._do_search)

    # 历史进货信息查询
    def _do_search(self):
        start_time = self.start_date.date().toString('yyyy-MM-dd')
        end_time = self.end_date.date().toString('yyyy-MM-dd')
        print(start_time, end_time)