from PyQt5.QtWidgets import QInputDialog, QMessageBox, QWidget, QLineEdit

from common import common, time_utils
from database.dao.sale import sale_item_handler
from database.dao.service import attribute_handler, service_handler
from domain.attribute import Attribute
from view.service.ui.ui_attribute import Ui_AttributeQWidget
from view.utils import table_utils, db_transaction_util


class AttributeManage(QWidget, Ui_AttributeQWidget):
    def __init__(self):
        super(AttributeManage, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('服务项目属性管理')
        self.table_title = ('ID', '属性名称', '是否必填', '显示顺序', '打印顺序', '必填标识')

        self._init_table()
        self._init_signal_and_slot()

    def _init_table(self):
        record = attribute_handler.get_all_attributes()

        table_utils.set_table_content(self.tableView, record, self.table_title)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(5, True)

    def _init_signal_and_slot(self):
        self.add.clicked.connect(self.do_add)
        self.edit.clicked.connect(self.do_update)
        self.remove.clicked.connect(self.do_remove)

    def do_add(self):
        attr_name, ok = QInputDialog.getText(self.add, '新增属性', '请输入属性名')
        if attr_name and ok:
            exists_info = attribute_handler.get_count_by_name(attr_name)
            if exists_info:
                if not exists_info[1]:
                    QMessageBox.information(self.add, '提示', '该属性已经存在，请重新输入')
                    return
                else:
                    attribute_handler.undo_delete_attribute_logical(exists_info[2])
            else:
                attribute = Attribute()
                attribute.create_op(common.config.login_user_info[0])
                attribute.name(attr_name)
                attribute.create_time(time_utils.get_now())
                attribute_handler.add_attribute(attribute)
                QMessageBox.information(self.add, '提示', '新增成功')
                self._init_table()

    def do_update(self):
        attr_id = table_utils.get_table_current_index_info(self.tableView, 0)
        if not attr_id:
            QMessageBox.information(self.add, '提示', '请选择一条属性进行修改！')
            return
        attr_id = int(attr_id)
        old_attr_name = table_utils.get_table_current_index_info(self.tableView, 1)

        new_attr_name, ok = QInputDialog.getText(self.edit, '修改属性', '请修改属性名称', QLineEdit.Normal, old_attr_name)

        if new_attr_name and ok:
            exists_info = attribute_handler.get_count_by_name(new_attr_name)
            if exists_info:
                if not exists_info[1]:
                    QMessageBox.information(self.edit, '提示', '该属性已经存在，请重新输入')
                    return
                else:
                    try:
                        db_transaction_util.begin()

                        # 将原来的属性对应的销售信息更新到当前的属性ID上
                        sale_item_handler.update_item_id(exists_info[2], attr_id)
                        # 物理删除原来的属性
                        attribute_handler.delete_attribute_physical(exists_info[2])
                        # 修改新的属性名称
                        attribute_handler.update_attribute(attr_id, new_attr_name)

                        db_transaction_util.commit()
                    except Exception as e:
                        print(e)
                        db_transaction_util.rollback()
                        QMessageBox.information(self.edit, '提示', '该属性名称修改失败，请重新提交！')
            else:
                try:
                    attribute_handler.update_attribute(attr_id, new_attr_name)
                    QMessageBox.information(self.edit, '提示', '新增成功')
                    self._init_table()
                except Exception as e:
                    print(e)
                    QMessageBox.information(self.edit, '提示', '该属性名称修改失败，请重新提交！')

    def do_remove(self):
        attr_id = table_utils.get_table_current_index_info(self.tableView, 0)
        message = QMessageBox.information(self.remove, '提示', '是否要删除该属性？', QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.Yes)
        if message == QMessageBox.No:
            return
        if not attr_id:
            QMessageBox.information(self.remove, '提示', '请选择一条属性进行修改！')
            return

        is_required = int(table_utils.get_table_current_index_info(self.tableView, 3))
        if is_required:
            QMessageBox.information(self.remove, '提示', '必填属性不允许删除！')
            return

        service_count = service_handler.get_count_by_attribute(attr_id)
        if service_count and service_count[0]:
            QMessageBox.information(self.remove, '提示', '该属性已经关联到服务项目上，不允许删除！')
            return

        try:
            attribute_handler.delete_attribute_logical(int(attr_id))
            QMessageBox.information(self.remove, '提示', '删除成功')
            self._init_table()
        except Exception as e:
            print(e)
            QMessageBox.information(self.remove, '提示', '该属性删除失败，请重新尝试！')
