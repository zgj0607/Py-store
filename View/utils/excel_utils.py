import xlwt
from PyQt5.QtCore import QAbstractItemModel


def export_to_file_from_table_view(file_name: str, title: tuple, sheet_name: str, model: QAbstractItemModel):
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


def export_to_file_from_db(file_name: str, title: tuple, sheet_name: str, record: ()):
    file = xlwt.Workbook()
    sheet1 = file.add_sheet(sheet_name, cell_overwrite_ok=True)

    for index, header in enumerate(title):
        sheet1.write(0, index, header, set_style('Times New Roman', 220, True))
    default = set_style('SimSun', 180, True, True, True)
    for row_index, row in enumerate(record):
        for col_index, data in enumerate(row):
            sheet1.write(row + 1, col_index, str(data), default)
    file.save(file_name)


def MakeTempMsg(data):
    tempMsg = {
        "checkOrderId": data[0],
        "orderNo": data[1],
        "createdTime": data[2],
        "pcSign": data[3],
        "carId": data[4],
        "carUser": data[5],
        "carPhone": data[6],
        "carModel": data[7],
        "workerName": data[8],
    }
    return tempMsg


def set_style(name, height, bold=False, center=False, up_or_down=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    alignment = xlwt.Alignment()
    # 左右居中
    if center:
        alignment.horz = xlwt.Alignment.HORZ_CENTER
    # 上下居中
    if up_or_down:
        alignment.vert = xlwt.Alignment.VERT_CENTER

    style.alignment = alignment
    return style
