from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets

from View.types.ui.ui_service import Ui_Form as UiService


class Service(QtWidgets.QWidget, UiService):
    def __init__(self):
        super(Service, self).__init__()
        self.setupUi(self)
        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)
        self.setWindowTitle('服务管理')

        # signal and slot


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = Service()
    windows.show()
    sys.exit(app.exec_())