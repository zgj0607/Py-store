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



# 写excel
def write_excel():
    f = xlwt.Workbook()  # 创建工作簿

    '''
    创建第一个sheet:
      sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预订', u'出票', u'退票', u'业务小计']

    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    # 生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', 220, True))  # 第一列
        sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))

    # 生成第二列
    i = 0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + i + 1, 1, status[j])
        i += 4

    f.save('demo1.xlsx')  # 保存文件
