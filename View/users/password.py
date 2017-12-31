from PyQt5 import QtWidgets

from View.users.ui_password import Ui_Form as UiPassword


class Password(QtWidgets.QWidget, UiPassword):
    def __init__(self):
        super(Password, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('密码管理')
