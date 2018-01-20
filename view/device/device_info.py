from PyQt5 import QtWidgets

from view.device.ui.ui_device import Ui_Form as UiDevice
from view.utils.table_utils import set_table_content, get_table_current_index_info
from database.dao.device.device_handler import get_all_device, update_device_state


class DeviceInfo(QtWidgets.QWidget, UiDevice):
    def __init__(self):
        super(DeviceInfo, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('设备管理')
        self.table_title = ('ID', '创建时间', '设备名称', '设备IP', '设备状态')
        self._update_device_table()

        self.start_state = '1'
        self.stop_state = '0'

        self._init_signal_and_slot()

    def _init_signal_and_slot(self):
        self.start.clicked.connect(self._start)
        self.stop.clicked.connect(self._stop)
        self.refresh.clicked.connect(self._update_device_table)

    def _update_device_table(self):
        set_table_content(self.device_table, get_all_device(), self.table_title)
        self.device_table.resizeColumnsToContents()

    def _start(self):
        device_id = get_table_current_index_info(self.device_table, 0)
        if not device_id:
            QtWidgets.QMessageBox.information(self.start, "提示", "请选择设备")
        else:
            update_device_state(device_id, self.start_state)
            QtWidgets.QMessageBox.information(self.stop, "提示", "设备已启用")
            self._update_device_table()

    def _stop(self):
        device_id = get_table_current_index_info(self.device_table, 0)
        if not device_id:
            QtWidgets.QMessageBox.information(self.stop, "提示", "请选择设备")
        else:
            update_device_state(device_id, self.stop_state)
            QtWidgets.QMessageBox.information(self.stop, "提示", "设备已禁用")
            self._update_device_table()
