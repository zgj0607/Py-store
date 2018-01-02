from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from Common.Common import ClientClose
from View.customer.return_visit import ReturnVisit
from View.device.device import Device
from View.main.ui.ui_main_view import Ui_MainWindow
from View.sale.all_sale import AllSale
from View.sale.local_sale import LocalSale
from View.statics.performance import Performance
from View.stock.history_stock_query import historystockQueryForm_stock
from View.stock.inventory_money import inventory_moneyForm_stock
from View.stock.inventory_serch import inventory_serchQueryForm_stock
from View.stock.inventory_unsalable_waring import inventory_unsalable_warninForm
from View.stock.normal_stock_query import stockQueryForm_stock
from View.stock.operation_total_data import operationtotaldataForm
from View.stock.stock_monitor_query import stockmonitorQueryForm_stock
from View.stock.sub_service_operation_data import sub_serviceoperationdataForm
from View.stock.supplier_arrears import supplierarrearsForm_stock
from View.stock.write_off_query import write_offForm_stock
from View.types.service import Service
from View.users.staff import Staff
from View.users.store_and_password import StoreAndPassword
from View.users.system_user import SystemUser


class MainView(QtWidgets.QMainWindow, Ui_MainWindow):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self, level):
        super(MainView, self).__init__()
        self.setupUi(self)

        self.init_menu_action()

        self._signal.connect(self._tab_show)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.tab_name = {}
        self.tab_index = {}

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
        self.supplier_payment.triggered.connect(self._supplier_payment_show)

        # 经营分析
        self.performance.triggered.connect(self._performance_show)
        self.sub_service_operation_data.triggered.connect(self._sub_service_operation_data_show)
        self.operation_total_data.triggered.connect(self._operation_total_data_show)

        # 系统管理
        self.store_user.triggered.connect(self._store_user_show)
        self.system_user.triggered.connect(self._system_user_show)
        self.services_add.triggered.connect(self._service_show)
        self.setting_device.triggered.connect(self._setting_device_show)
        self.setting_password.triggered.connect(self._setting_password_show)

    # 本店销售明细
    def _local_sale_show(self):
        self._signal.emit('local_sale')

    # 全店销售明细
    def _all_sale_show(self):
        self._signal.emit('all_sale')

    # 普通进货录入
    def _normal_stock_add_show(self):
        self._signal.emit('normal_stock_add')

    # 销负进货录入
    def _write_off_add_show(self):
        self._signal.emit('write_off_add')

    # 历史进货信息
    def _history_stock_show(self):
        self._signal.emit('history_stock')

    # 进货监控
    def _stock_monitor_show(self):
        self._signal.emit('stock_monitor')

    # 库存查询
    def _inventory_search_show(self):
        self._signal.emit('inventory_search_show')

    # 滞销预警
    def _inventory_unsalable_pre_warning_show(self):
        self._signal.emit('inventory_unsalable_pre_warning')

    # 库存金额
    def _inventory_money_show(self):
        self._signal.emit('inventory_money')

    # 库存校准
    def _inventory_calibration_show(self):
        self._signal.emit('inventory_calibration')

    # 客户回访
    def _return_visit_show(self):
        self._signal.emit('return_visit')

    # 欠款明细
    def _supplier_arrears_show(self):
        self._signal.emit('supplier_arrears')

    # 付款录入
    def _supplier_payment_show(self):
        self._signal.emit('supplier_payment')

    # 业绩报表
    def _performance_show(self):
        self._signal.emit('performance')

    # 二级项目经营明细
    def _sub_service_operation_data_show(self):
        self._signal.emit('sub_service_operation_data')

    # 总体经营数据
    def _operation_total_data_show(self):
        self._signal.emit('operation_total_data')

    # 店面人员
    def _store_user_show(self):
        self._signal.emit('store_user')

    # 管理员管理
    def _system_user_show(self):
        self._signal.emit('system_user')

    # 服务项目管理
    def _service_show(self):
        self._signal.emit('service')

    # 设备管理
    def _setting_device_show(self):
        self._signal.emit('setting_device')

    # 密码管理
    def _setting_password_show(self):
        self._signal.emit('setting_password')

    # 统一处理Tab页的显示
    def _tab_show(self, obj_name):
        tab_widget = None
        tab_id = self.tabWidget.count()

        if tab_id >= 7:
            QMessageBox.information(self, "提示", "选项卡过多，请关闭部分后再打开")
            return

        if self._exists(obj_name):
            tab_index = self.tab_name.get(obj_name)
            tab_widget = self.tabWidget.widget(tab_index)

        else:
            if obj_name == 'local_sale':
                tab_widget = LocalSale()

            elif obj_name == 'all_sale':
                tab_widget = AllSale()

            elif obj_name == 'return_visit':
                tab_widget = ReturnVisit()

            elif obj_name == 'normal_stock_add':
                tab_widget = stockQueryForm_stock()

            elif obj_name == 'write_off_add':
                tab_widget = write_offForm_stock()

            elif obj_name == 'history_stock':
                tab_widget = historystockQueryForm_stock()

            elif obj_name == 'stock_monitor':
                tab_widget = stockmonitorQueryForm_stock()

            elif obj_name == 'inventory_search_show':
                tab_widget = inventory_serchQueryForm_stock()

            elif obj_name == 'inventory_unsalable_pre_warning':
                tab_widget = inventory_unsalable_warninForm()

            elif obj_name == 'inventory_money':
                tab_widget = inventory_moneyForm_stock()

            elif obj_name == 'supplier_arrears':
                tab_widget = supplierarrearsForm_stock()

            elif obj_name == 'sub_service_operation_data':
                tab_widget = sub_serviceoperationdataForm()

            elif obj_name == 'operation_total_data':
                tab_widget = operationtotaldataForm()

            elif obj_name == 'performance':
                tab_widget = Performance()

            elif obj_name == 'store_user':
                tab_widget = Staff()

            elif obj_name == 'system_user':
                tab_widget = SystemUser()

            elif obj_name == 'service':
                tab_widget = Service()

            elif obj_name == 'setting_device':
                tab_widget = Device()

            elif obj_name == 'setting_password':
                tab_widget = StoreAndPassword()

            self._add_tab(tab_widget, tab_id)
            self._add_tab_info_dict(obj_name, tab_id)

        self.tabWidget.setCurrentWidget(tab_widget)

    # 统一处理Tab页的新增
    def _add_tab(self, tab_widget: QWidget, tab_id: int):
        self.tabWidget.addTab(tab_widget, tab_widget.windowTitle())
        # self.tabWidget.setTabIcon(tab_id, self.tab_icon)

    # 统一处理Tab页的所有字典信息
    def _add_tab_info_dict(self, obj_name: str, tab_id: int):
        self.tab_index[tab_id] = obj_name
        self.tab_name[obj_name] = tab_id

    # 判断将要打开的页面是否已经在Tab页中打开，同一个页面强制只能打开一个
    def _exists(self, tab_name):
        if not self.tab_name.__contains__(tab_name):
            return False
        return True

    # 统一处理Tab页的关闭
    def close_tab(self, tab_index):
        tab_name = self.tab_index.get(tab_index)
        del self.tab_name[tab_name]
        del self.tab_index[tab_index]
        self.tabWidget.removeTab(tab_index)

    def closeEvent(self, event):
        ClientClose()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    windows = MainView()
    windows.show()
    sys.exit(app.exec_())
