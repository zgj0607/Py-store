from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView, QTableWidget, QTableWidgetItem


def get_table_current_index_info(table, num):
    row = table.currentIndex().row()
    model = table.model()
    index = model.index(row, num)
    return model.data(index)


def get_table_cell(table, row, column):
    model = table.model()
    index = model.index(row, column)
    return model.data(index)


def get_table_cell_by_index(table, model_index):
    model = table.model()
    return model.data(model_index)


def add_table_header(table: QTableView, table_title: tuple):
    if isinstance(table, QTableWidget):
        table.setColumnCount(len(table_title))
        table.setHorizontalHeaderLabels(table_title)
    else:

        model = QStandardItemModel()

        table_len = len(table_title)
        # 设置表格属性：
        model.setColumnCount(table_len)

        for index, item in enumerate(table_title):
            model.setHeaderData(index, Qt.Horizontal, item)

        table.setModel(model)
        table.setColumnWidth(0, 120)


def set_table_content(table: QTableView, record, table_title=()):
    if table_title:
        add_table_header(table, table_title)
    column_len = len(table_title)
    model = table.model()
    for row_index, data in enumerate(record):
        for column_index in range(column_len):
            model.setItem(row_index, column_index, QStandardItem(str(data[column_index])))
            model.item(row_index, column_index).setTextAlignment(Qt.AlignCenter)

    # if record and column_len >= 10:
    #     table.resizeColumnsToContents()
    # else:
    #     table.horizontalHeader().setStretchLastSection(True)


def set_table_content_with_merge(table: QTableView, record, table_title=(), merge_column_index=0):
    if table_title:
        add_table_header(table, table_title)

    column_len = len(table_title)
    model = table.model()
    temp_value = ''
    merge_row_num = 0
    for row_index, data in enumerate(record):
        for column_index in range(column_len):
            model.setItem(row_index, column_index, QStandardItem(str(data[column_index])))

        merge_cell_value = data[merge_column_index]
        if row_index == 0:
            temp_value = merge_cell_value
        if merge_cell_value == temp_value:
            merge_row_num += 1
            if merge_row_num > 1:
                # 其参数为：要合并的单元格的起始行数、列数，要合并的总行数，总列数
                table.setSpan(row_index - merge_row_num + 1, merge_column_index, merge_row_num, 1)
        else:
            merge_row_num = 1

        temp_value = merge_cell_value


def set_table_widget_content(table: QTableWidget, record, table_title=(), need_checkbox=False):
    if table_title:
        add_table_header(table, table_title)

    if not record:
        return

    row_count = len(record)
    table.setRowCount(row_count)
    col_offset = 0
    for row_index, data in enumerate(record):
        if need_checkbox:
            new_item = QTableWidgetItem('')
            new_item.setCheckState(Qt.Unchecked)
            col_offset = 1
            table.setItem(row_index, 0, new_item)
        for col_index in range(table.columnCount() - col_offset):
            new_item = QTableWidgetItem(str(data[col_index]))
            table.setItem(row_index, col_index + col_offset, new_item)
