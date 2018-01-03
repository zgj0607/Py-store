import os
from collections import defaultdict
from datetime import datetime

import xlrd
import xlwt

from Common.StaticFunc import set_style
from Common.time_utils import get_now
from Common.config import menuSavePath
from View.types import attribute, attribute_state
from database.dao.service.service_handler import get_all_second_level_service, get_all_first_level_service, \
    add_first_level_service, add_second_level_service


def import_service(file_name, must_set):
    bk = xlrd.open_workbook(file_name)
    sh = bk.sheet_by_name("菜单列表")
    rows = sh.nrows

    # 将表格中的一级和二级放入到字典[数组]的数据结构中
    first_service_from_file_dict = defaultdict(list)
    for i in range(1, rows):
        row_data = sh.row_values(i)
        first_service = row_data[0]
        second_service = row_data[1]
        if first_service not in first_service_from_file_dict:
            first_service_from_file_dict[first_service] = [second_service]
        else:
            first_service_from_file_dict[first_service].append(second_service)

    # 将数据库中一级服务项目汇总，并将一级服务项目的名称和ID建立字典
    first_service_in_db = get_all_first_level_service()
    all_first_service = list()
    first_service_in_db_dict = dict()
    for data in first_service_in_db:
        all_first_service.append(data[1])
        first_service_in_db_dict[data[1]] = data[0]

    # 循环增加一级服务项目和二级服务项目
    first_service_add_id = None
    for first_service_name_from_file in first_service_from_file_dict:
        if first_service_name_from_file not in all_first_service:
            # 一级服务类型不在全部列表中，则新增
            first_service_add_id = add_first_level_service(first_service_name_from_file)
        else:
            if first_service_in_db_dict.get(first_service_name_from_file):
                first_service_add_id = first_service_in_db_dict.get(first_service_name_from_file)

        if not first_service_add_id:
            continue

        # 循环增加二级服务项目
        for second_service_name in first_service_from_file_dict[first_service_name_from_file]:
            add_second_level_service(second_service_name, first_service_add_id, attribute, attribute_state)


def export_services():
    now = get_now()
    file_name = now + ".xls"
    title_list = ["一级菜单", "二级菜单"]
    all_table_len = len(title_list)

    # 整理参数
    services = get_all_second_level_service()

    if services:
        wb = xlwt.Workbook()
        ws = wb.add_sheet('菜单列表', cell_overwrite_ok=True)

        for i in range(all_table_len):
            # 设置单元格宽度
            ws.col(i).width = 265 * 20
            # 插入标题
            ws.write(0, i, title_list[i], set_style('Arial', 250, True, True))

        row = 1
        for service in services:
            # 插入信息
            ws.write(row, 0, service[1], set_style('SimSun', 180, True, True, True))
            ws.write(row, 1, service[3], set_style('SimSun', 180, True, True, True))
            row += 1

        if not os.path.exists(menuSavePath):
            os.mkdir(menuSavePath)
        wb.save(menuSavePath + file_name)
        return file_name
    else:
        return False
