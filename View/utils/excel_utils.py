import xlwt
from PyQt5.QtCore import QAbstractItemModel

from Common.StaticFunc import set_style


def export_to_file(file_name: str, title: tuple, sheet_name: str, model: QAbstractItemModel):
    file = xlwt.Workbook()
    sheet1 = file.add_sheet(sheet_name, cell_overwrite_ok=True)

    for index, header in enumerate(title):
        sheet1.write(0, index, header, set_style('Times New Roman', 220, True))
    default = set_style('SimSun', 180, True, True, True)
    for row in range(model.rowCount()):
        for col in range(model.columnCount()):
            index = model.index(row, col)
            data = model.data(index)
            sheet1.write(row + 1, col, data, default)
    file.save(file_name)
