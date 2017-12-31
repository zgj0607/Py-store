from PyQt5 import QtWidgets

from View.users.ui_staff import Ui_Staff as UiStaff


class Staff(QtWidgets.QWidget, UiStaff):
    def __init__(self):
        super(Staff, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('门店人员管理')

    def _init_signal_and_slot(self):
        self.add_staff.clicked.connect(self._add_staff)
        self.delete_staff.clicked.connect(self._delete_staff)
        self.update_staff.clicked.connect(self._update_staff)
    #
    # def _add_staff(self):
    #
    #
    # def _udpate_staff(self):
    #
    #
    # def _delect_staff(self):
