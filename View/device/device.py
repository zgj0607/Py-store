from PyQt5 import QtWidgets

from View.device.ui_device import Ui_Form as UiDevice


class Device(QtWidgets.QWidget, UiDevice):
    def __init__(self):
        super(Device, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('设备管理')
