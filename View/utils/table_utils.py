from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView


def get_table_current_index_info(table, num):
    row = table.currentIndex().row()
    model = table.model()
    index = model.index(row, num)
    return model.data(index)


def get_table_cell(table, row, num):
    model = table.model()
    index = model.index(row, num)
    return model.data(index)


def add_table_header(table: QTableView, table_title: tuple):
    model = QStandardItemModel()

    table_len = len(table_title)
    # 设置表格属性：
    model.setColumnCount(table_len)

    for index, item in enumerate(table_title):
        model.setHeaderData(index, Qt.Horizontal, item)

    table.setModel(model)
    table.setColumnWidth(0, 120)


def set_table_content(table: QTableView, record, table_title: tuple):
    add_table_header(table, table_title)
    column_len = len(table_title)
    model = table.model()
    for row_index, data in enumerate(record):
        for column_index in range(column_len):
            model.setItem(row_index, column_index, QStandardItem(str(data[column_index])))
