from PyQt5.QtWidgets import QDialog, QInputDialog, QMessageBox

from Common import Common, time_utils
from View.types.ui.ui_attribute_dialog import Ui_AttributeDialog
from View.utils import table_utils
from database.dao.service import attribute_handler
from domain.attribute import Attribute


class AttributeDialog(QDialog, Ui_AttributeDialog):
    def __init__(self):
        super(AttributeDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('服务项目属性管理')
        self.table_title = ('ID', '属性名称', '是否必填')

        self._init_table()
        self._init_signal_and_slot()

    def _init_table(self):
        record = attribute_handler.get_all_attributes()

        table_utils.set_table_content(self.tableView, record, self.table_title)
        self.tableView.setColumnHidden(0, True)

    def _init_signal_and_slot(self):
        self.add.clicked.connect(self.do_add)

    def do_add(self):
        attr_name, ok = QInputDialog.getText(self.add, '新增属性', '请输入属性名')
        if attr_name and ok:
            exists_count = attribute_handler.get_count_by_name(attr_name)
            if exists_count:
                QMessageBox.information(self.add, '提示', '该属性已经存在，请重新输入')
                return
            else:
                attribute = Attribute()
                attribute.create_op(Common.config.login_user_info[0])
                attribute.name(attr_name)
                attribute.create_time(time_utils.get_now())
                attribute_handler.add_attribute(attribute)
                QMessageBox.information(self.add, '提示', '新增成功')
                self._init_table()
