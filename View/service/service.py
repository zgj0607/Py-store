from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from View.service.excel_process import export_services, import_service
from View.service.first_service_info import FirstLevelServiceInfo
from View.service.second_service_info import SecondServiceInfo
from View.service.ui.ui_service import Ui_Form as UiService
from View.utils import db_transaction_util
from View.utils.table_utils import set_table_content, get_table_current_index_info
from database.dao.service import service_handler
from database.dao.stock import stock_handler


class Service(QtWidgets.QWidget, UiService):
    def __init__(self):
        super(Service, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('服务管理')

        self.first_service_title = ('ID', '一级服务名称')
        self.second_service_title = ('一级服务ID', '一级服务名称', '二级服务ID', '二级服务名称', '属性列表', '属性状态')

        self._init_signal_and_slot()
        self._refresh_all_table()
        print("按钮样式表", self.import_service.backgroundRole())

    def _init_signal_and_slot(self):
        self.export_service.clicked.connect(self._export_data)
        self.import_service.clicked.connect(self._import_data)

        self.add_first_service.clicked.connect(self._add_first_service)
        self.update_first_service.clicked.connect(self._update_first_service)
        self.remove_first_service.clicked.connect(self._remove_first_service)

        self.add_second_service.clicked.connect(self._add_second_service)
        self.update_second_service.clicked.connect(self._update_second_service)
        self.remove_second_service.clicked.connect(self._remove_second_service)

        self.first_service_table.clicked.connect(self._refresh_second_service)
        self.second_service_table.clicked.connect(self._refresh_attribute_table)

    def _refresh_all_table(self):
        self._refresh_first_service()
        # self._refresh_second_service()
        # self._refresh_attribute_table()

    def _refresh_first_service(self):
        set_table_content(self.first_service_table, service_handler.get_all_first_level_service(),
                          self.first_service_title)
        self.first_service_table.setColumnHidden(0, True)

    def _refresh_second_service(self):
        father_id = get_table_current_index_info(self.first_service_table, 0)
        if not father_id:
            return
        set_table_content(self.second_service_table, service_handler.get_second_service_by_father(father_id),
                          self.second_service_title)
        self.second_service_table.setColumnHidden(0, True)
        self.second_service_table.setColumnHidden(1, True)
        self.second_service_table.setColumnHidden(2, True)
        self.second_service_table.setColumnHidden(4, True)
        self.second_service_table.setColumnHidden(5, True)

    def _refresh_attribute_table(self):
        attribute_list = self._get_attribute_list()
        model = QStandardItemModel()

        for index, data in enumerate(attribute_list):
            item = QStandardItem(str(data[1]))
            model.setItem(index, 0, item)
            model.item(index, 0).setTextAlignment(Qt.AlignCenter)

        self.attribute_table.setModel(model)

    def _export_data(self):
        file_name = export_services()
        if file_name:
            QtWidgets.QMessageBox.information(self.export_service, "提示", "文件名为：{}".format(file_name))
        else:
            QtWidgets.QMessageBox.information(self.export_service, "提示", "服务项目内容欠缺")

    def _import_data(self):
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self.import_service, "选取文件", "C:/",
                                                                     "Text Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,注意用分号间隔
        if file_name:
            try:
                import_service(file_name)
                QtWidgets.QMessageBox.information(self.import_service, "提示", "导入成功")
                self._refresh_all_table()
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.information(self.im, "提示", "文件错误")

    def _add_first_service(self):
        service = FirstLevelServiceInfo('新增一级服务项目')
        service.exec()
        self._refresh_all_table()

    def _update_first_service(self):
        service_id = get_table_current_index_info(self.first_service_table, 0)
        if not service_id:
            QtWidgets.QMessageBox.information(self.update_first_service, "提示", "请选择一级服务项目")
            return
        service_name = get_table_current_index_info(self.first_service_table, 1)
        service = FirstLevelServiceInfo('修改一级服务项目', service_id=service_id, service_name=service_name)
        service.exec()
        self._refresh_all_table()

    def _remove_first_service(self):
        service_id = get_table_current_index_info(self.first_service_table, 0)
        if service_id:
            service_name = get_table_current_index_info(self.first_service_table, 1)
            reply = QtWidgets.QMessageBox.question(self.remove_first_service, 'Message',
                                                   "是否删除此服务项目：" + service_name + "？",
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if not service_handler.get_second_service_count_by_father(service_id):
                    service_handler.delete_service(service_id)
                    QtWidgets.QMessageBox.information(self.remove_first_service, "提示", "删除成功！")
                    self._refresh_all_table()
                else:
                    QtWidgets.QMessageBox.information(self.remove_first_service, "提示", "该一级服务项目下存在二级服务项目，不能删除！")
        else:
            QtWidgets.QMessageBox.information(self.remove_first_service, "提示", "请选择一级服务项目")

    def _add_second_service(self):
        father_id = get_table_current_index_info(self.first_service_table, 0)
        if not father_id:
            QtWidgets.QMessageBox.information(self.add_second_service, "提示", "请选择一级服务项目")
        else:
            service = SecondServiceInfo('新增二级服务项目', father_id=father_id)
            service.exec()
            self._refresh_second_service()

    def _update_second_service(self):
        service_id = get_table_current_index_info(self.second_service_table, 2)
        if not service_id:
            QtWidgets.QMessageBox.information(self.add_second_service, "提示", "请选择二级服务项目")
        else:
            father_id = get_table_current_index_info(self.second_service_table, 0)
            service_name = get_table_current_index_info(self.second_service_table, 3)
            service = SecondServiceInfo('修改二级服务项目', service_id=service_id, father_id=father_id,
                                        service_name=service_name)
            service.exec()
            self._refresh_second_service()
            self.attribute_table.model().removeRows(0, self.attribute_table.model().rowCount())

    def _remove_second_service(self):
        service_id = get_table_current_index_info(self.second_service_table, 2)
        if service_id:
            service_name = get_table_current_index_info(self.second_service_table, 3)
            reply = QtWidgets.QMessageBox.question(self.remove_second_service, 'Message',
                                                   "是否删除此服务项目：" + service_name + "？",
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if stock_handler.get_count_by_service(service_id):
                    QtWidgets.QMessageBox.information(self.remove_second_service, "提示", "该服务项目存在库存信息，不允许删除！")
                    return
                else:
                    try:
                        db_transaction_util.begin()
                        service_handler.delete_service_all_attribute(service_id)
                        service_handler.delete_service(service_id)
                        db_transaction_util.commit()
                        QtWidgets.QMessageBox.information(self.remove_second_service, "提示", "删除成功！")
                        self._refresh_second_service()
                    except Exception as e:
                        print(e)
                        db_transaction_util.rollback()
                        QtWidgets.QMessageBox.information(self.remove_second_service, "提示", "删除失败，请重试！")
        else:
            QtWidgets.QMessageBox.information(self.remove_second_service, "提示", "请选择二级服务项目")

    def _get_attribute_list(self):
        service_id = get_table_current_index_info(self.second_service_table, 2)
        attribute = service_handler.get_attribute_by_service(service_id)

        return attribute
