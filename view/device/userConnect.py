from PyQt5 import QtWidgets

from common import config
from view.device.ui.ui_pad_connect import Ui_PadConnect
from database.dao.device import device_handler
from domain.device import Device


class PadConnect(QtWidgets.QDialog, Ui_PadConnect):
    def __init__(self, device: Device):
        super(PadConnect, self).__init__()
        self.setupUi(self)

        self.device = device

        self.info.setText("员工：{}<br/>请求连接服务器，是否允许？".format(self.device.ip()))
        self.refuse.setFocus()

        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.allow.clicked.connect(self.allow_connect)
        self.refuse.clicked.connect(self.refuse_connect)

    def allow_connect(self):
        self._add_new_device('1')

    def refuse_connect(self):
        self._add_new_device("0")

    def _add_new_device(self, state='0'):
        self.device.state(state)
        device_handler.add_new_device(self.device)
        config.ui._confirm_result = (state == '1')
        self.close()
