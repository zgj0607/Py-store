from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from Common.Common import ClientClose
from View.buy.buy_monitor_query import BuyInfoMonitor
from View.buy.history_buy_query import HistoryStock
from View.buy.normal_buy_query import StockQuery
from View.buy.write_off_query import WriteOff
from View.customer.return_visit import ReturnVisit
from View.device.device_info import DeviceInfo
from View.device.userConnect import PadConnect
from View.main.ui.ui_main_view import Ui_MainWindow
from View.operation.operation_total_data import OperationTotalData
from View.operation.performance import Performance
from View.operation.sub_service_operation_data import SubServiceOperationData
from View.sale.all_sale import AllSale
from View.sale.local_sale import LocalSale
from View.stock.stock_money import StockMoney
from View.stock.stock_search import StockSearch
from View.stock.stock_unsalable_waring import StockUnsalableWarning
from View.supplier.supplier_arrears import SupplierArrears
from View.service.attribute import AttributeManage
from View.service.service import Service
from View.users.staff import Staff
from View.users.system_user import SystemUser
from domain.device import Device


class MainView(QtWidgets.QMainWindow, Ui_MainWindow):
    # 打开Tab页的信号
    _tab_signal = QtCore.pyqtSignal(str)

    # Pad连接请求的信号
    pad_connect_signal = QtCore.pyqtSignal(Device)
    _confirm_result = False

    def __init__(self, level):
        super(MainView, self).__init__()
        self.setupUi(self)

        icon = QIcon('img/logo.png')
        self.setWindowIcon(icon)

        self.init_menu_action()

        self._tab_signal.connect(self._tab_show)
        self.pad_connect_signal.connect(self._confirm_pad_connect)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.tab_name = {}

        self.confirm_dialog = None

    # 初始化所有菜单动作
    def init_menu_action(self):
        # 销售明细
        self.actionAll.triggered.connect(self._all_sale_show)
        self.actionLocal.triggered.connect(self._local_sale_show)

        # 进货管理
        self.normal_stock_add.triggered.connect(self._normal_stock_add_show)
        self.write_off_add.triggered.connect(self._write_off_add_show)
        self.history_stock.triggered.connect(self._history_stock_show)
        self.stock_monitor.triggered.connect(self._stock_monitor_show)

        # 库存管理
        self.inventory_search.triggered.connect(self._inventory_search_show)
        self.inventory_unsalable_pre_warning.triggered.connect(self._inventory_unsalable_pre_warning_show)
        self.inventory_money.triggered.connect(self._inventory_money_show)
        self.inventory_calibration.triggered.connect(self._inventory_calibration_show)

        # 客户回访
        self.return_visit.triggered.connect(self._return_visit_show)

        # 供应商管理
        self.supplier_arrears.triggered.connect(self._supplier_arrears_show)

        # 经营分析
        self.performance.triggered.connect(self._performance_show)
        self.sub_service_operation_data.triggered.connect(self._sub_service_operation_data_show)
        self.operation_total_data.triggered.connect(self._operation_total_data_show)

        # 系统管理
        self.store_user.triggered.connect(self._store_user_show)
        self.system_user.triggered.connect(self._system_user_show)
        self.service_manage.triggered.connect(self._service_show)
        self.attribute_setting.triggered.connect(self._attribute_show)
        self.setting_device.triggered.connect(self._setting_device_show)
        self.setting_password.triggered.connect(self._setting_password_show)

    # 本店销售明细
    def _local_sale_show(self):
        self._tab_signal.emit('local_sale')

    # 全店销售明细
    def _all_sale_show(self):
        self._tab_signal.emit('all_sale')

    # 普通进货录入
    def _normal_stock_add_show(self):
        self._tab_signal.emit('normal_buy_add')

    # 销负进货录入
    def _write_off_add_show(self):
        self._tab_signal.emit('write_off_add')

    # 历史进货信息
    def _history_stock_show(self):
        self._tab_signal.emit('history_buy')

    # 进货监控
    def _stock_monitor_show(self):
        self._tab_signal.emit('buy_monitor')

    # 库存查询
    def _inventory_search_show(self):
        self._tab_signal.emit('stock_search')

    # 滞销预警
    def _inventory_unsalable_pre_warning_show(self):
        self._tab_signal.emit('stock_unsalable_warning')

    # 库存金额
    def _inventory_money_show(self):
        self._tab_signal.emit('stock_money')

    # 库存校准
    def _inventory_calibration_show(self):
        self._tab_signal.emit('inventory_calibration')

    # 客户回访
    def _return_visit_show(self):
        self._tab_signal.emit('return_visit')

    # 欠款明细
    def _supplier_arrears_show(self):
        self._tab_signal.emit('supplier_arrears')

    # 业绩报表
    def _performance_show(self):
        self._tab_signal.emit('performance')

    # 二级项目经营明细
    def _sub_service_operation_data_show(self):
        self._tab_signal.emit('sub_service_operation_data')

    # 总体经营数据
    def _operation_total_data_show(self):
        self._tab_signal.emit('operation_total_data')

    # 店面人员
    def _store_user_show(self):
        self._tab_signal.emit('store_user')

    # 管理员管理
    def _system_user_show(self):
        self._tab_signal.emit('system_user')

    # 服务项目管理
    def _service_show(self):
        self._tab_signal.emit('service_manage')

    def _attribute_show(self):
        self._tab_signal.emit('attribute_manage')

    # 设备管理
    def _setting_device_show(self):
        self._tab_signal.emit('setting_device')

    # 密码管理
    def _setting_password_show(self):
        self._tab_signal.emit('setting_password')

    # 统一处理Tab页的显示
    def _tab_show(self, obj_name):
        tab_widget = None
        tab_id = self.tabWidget.count()

        if tab_id >= 7:
            QMessageBox.information(self, "提示", "选项卡过多，请关闭部分后再打开")
            return

        if self._exists(obj_name):
            tab_widget = self.tab_name.get(obj_name)

        else:
            if obj_name == 'local_sale':
                tab_widget = LocalSale()

            elif obj_name == 'all_sale':
                tab_widget = AllSale()

            elif obj_name == 'return_visit':
                tab_widget = ReturnVisit()

            elif obj_name == 'normal_buy_add':
                tab_widget = StockQuery()

            elif obj_name == 'write_off_add':
                tab_widget = WriteOff()

            elif obj_name == 'history_buy':
                tab_widget = HistoryStock()

            elif obj_name == 'buy_monitor':
                tab_widget = BuyInfoMonitor()

            elif obj_name == 'stock_search':
                tab_widget = StockSearch()

            elif obj_name == 'stock_unsalable_warning':
                tab_widget = StockUnsalableWarning()

            elif obj_name == 'stock_money':
                tab_widget = StockMoney()

            elif obj_name == 'supplier_arrears':
                tab_widget = SupplierArrears()

            elif obj_name == 'sub_service_operation_data':
                tab_widget = SubServiceOperationData()

            elif obj_name == 'operation_total_data':
                tab_widget = OperationTotalData()

            elif obj_name == 'performance':
                tab_widget = Performance()

            elif obj_name == 'store_user':
                tab_widget = Staff()

            elif obj_name == 'system_user':
                tab_widget = SystemUser()

            elif obj_name == 'service_manage':
                tab_widget = Service()

            elif obj_name == 'attribute_manage':
                tab_widget = AttributeManage()

            elif obj_name == 'setting_device':
                tab_widget = DeviceInfo()

            elif obj_name == 'setting_password':
                tab_widget = None
            else:
                tab_widget = None

            if tab_widget:
                self._add_tab(tab_widget)
                self._add_tab_info_dict(obj_name, tab_widget)
                self.tabWidget.setCurrentWidget(tab_widget)
            else:
                QMessageBox.information(self.tabWidget, '提示', '功能开发中，请稍后！')
                return

    # 处理未注册Ip的PAD连接请求
    def _confirm_pad_connect(self, device: Device):

        self.confirm_dialog = PadConnect(device)
        self.confirm_dialog.exec()
        print(self._confirm_result)

    # 统一处理Tab页的新增
    def _add_tab(self, tab_widget: QWidget):
        self.tabWidget.addTab(tab_widget, tab_widget.windowTitle())

    # 统一处理Tab页的所有字典信息
    def _add_tab_info_dict(self, obj_name: str, tab_widget: QWidget):
        self.tab_name[obj_name] = tab_widget

    # 判断将要打开的页面是否已经在Tab页中打开，同一个页面强制只能打开一个
    def _exists(self, tab_name):
        if not self.tab_name.__contains__(tab_name):
            return False
        return True

    # 统一处理Tab页的关闭
    def close_tab(self, tab_index):
        tab_widget = self.tabWidget.widget(tab_index)
        tab_name = list(self.tab_name.keys())[list(self.tab_name.values()).index(tab_widget)]
        del self.tab_name[tab_name]
        self.tabWidget.removeTab(tab_index)

    def closeEvent(self, event):
        ClientClose()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    windows = MainView()
    windows.show()
    sys.exit(app.exec_())
