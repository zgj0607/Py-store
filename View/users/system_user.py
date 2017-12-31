from PyQt5 import QtWidgets

from View.users.ui_system_user import Ui_Form as UiSystemUser


class SystemUser(QtWidgets.QWidget, UiSystemUser):
    def __init__(self):
        super(SystemUser, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('系统人员管理')
