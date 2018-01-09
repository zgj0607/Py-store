import configparser
import json
import os
import re
from collections import defaultdict

import xlrd
import xlwt
from PyQt5.QtWidgets import QProgressDialog

from Common.Common import SocketServer
from Common.StaticFunc import GetOrderId
from Common.time_utils import get_now, format_time
from Common.config import savePath
from Controller import DbHandler
from View.utils.excel_utils import MakeTempMsg, set_style


class ExcelProcess:
    database_handler = DbHandler.DB_Handler()

    def import_sale_detail(self, file_name, widget):
        bk = xlrd.open_workbook(file_name)
        try:
            sh = bk.sheet_by_name("消费列表")
        except Exception as e:
            print(e)
            sh = bk.sheet_by_name("Sheet1")
        rows = sh.nrows
        temp = list()
        title_list = ['检索ID', 'orderNo', 'createdTime', "pcSign", "carId", "carUser", "carPhone", "carModel",
                      "workerName", "project"]
        user_list = ["carId", "carUser", "carPhone", "carModel"]
        must_len = len(title_list)
        title = sh.row_values(1)

        match_result = self._is_from_export(str(sh.row_values(0)[0]))

        progress_dialog = QProgressDialog(widget)
        progress_dialog.setWindowTitle("导入中")
        from PyQt5.QtCore import Qt
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setMinimumDuration(4)
        progress_dialog.setWindowTitle(widget.tr("请等待"))
        progress_dialog.setLabelText(widget.tr("导入中..."))
        progress_dialog.setCancelButtonText(widget.tr("取消"))
        progress_dialog.setRange(0, rows - 3)
        progress_dialog.show()
        if True:
            p = 0
            msg_list = list()
            for i in range(2, rows):
                # 用正则表达式判断第一行数据内容，从而判断是否用软件导出的EXCEL文档
                if match_result:
                    # 若是用软件导出的则
                    if progress_dialog.wasCanceled():
                        break
                    progress_dialog.setValue(p)
                    p += 1
                    try:
                        # if True:
                        save_data = dict()
                        row_data = sh.row_values(i)
                        if i < rows - 1:
                            temp2 = sh.row_values(i + 1)
                        else:
                            temp2 = None

                        if not temp2 and temp2[0] == '':
                            # 合并了单元格则合并内容是空，将后面不是空的内容进行缓存，合并的内容会在最后一条信息中显示，
                            # 此时一并进行录入
                            temp.append(row_data)
                        else:

                            # if row_data[0] != '':
                            if temp:
                                order_check_id = temp[0][0]
                            else:
                                order_check_id = row_data[0]
                            check_order = self.database_handler.GetXiaoFeiByKey("orderCheckId", order_check_id)
                            # 有此订单的就不保存了
                            if not check_order:
                                if temp:
                                    temp.append(row_data)
                                    all_msg = temp[0]
                                    # 接入信息后录入
                                    for j in range(len(temp)):
                                        if j != 0:
                                            msg = temp[j]
                                            attribute = {}
                                            for ki in range(len(title)):

                                                all_msg[ki] = str(all_msg[ki])
                                                msg[ki] = str(msg[ki])
                                                if ki < must_len:
                                                    temp_key = title_list[ki]
                                                    if temp_key in ['orderNo', 'carPhone']:
                                                        all_msg[ki] = all_msg[ki].replace('.0', "")
                                                        msg[ki] = msg[ki].replace('.0', "")
                                                    if title_list[ki] in ["project"]:
                                                        save_data[temp_key] = msg[ki]
                                                    else:
                                                        if temp_key == "检索ID":
                                                            temp_key = "orderCheckId"
                                                        save_data[temp_key] = all_msg[ki]
                                                else:
                                                    if row_data[ki] == "" or row_data[ki] == "-":
                                                        continue
                                                    attribute[title[ki]] = msg[ki]

                                            save_data['attribute'] = json.dumps(attribute)
                                            save_data['id'] = GetOrderId()
                                            self.database_handler.InsertXiaoFei(save_data)

                                        row_data = all_msg
                                attribute = {}
                                user_save = {}
                                for ki in range(len(title)):
                                    row_data[ki] = str(row_data[ki])
                                    if ki < must_len:
                                        if title_list[ki] in ['orderNo', 'carPhone']:
                                            row_data[ki] = row_data[ki].replace('.0', "")
                                        key = title_list[ki]
                                        if key == "检索ID":
                                            key = "orderCheckId"
                                        save_data[key] = row_data[ki]
                                        # 保存用户信息
                                        if key in user_list:
                                            user_save[key] = row_data[ki]

                                    else:
                                        if row_data[ki] == "" or row_data[ki] == "-":
                                            continue
                                        attribute[title[ki]] = row_data[ki]

                                user = self.database_handler.CheckUser(user_save.get("carPhone"),
                                                                       user_save.get("carId"))
                                if not user:
                                    # 没有此用户则添加
                                    key = "userName,carPhone,carModel,carId,createdTime"
                                    value = "'{}','{}','{}','{}','{}'".format(user_save.get("carUser"),
                                                                              user_save.get("carPhone"),
                                                                              user_save.get("carModel"),
                                                                              user_save.get("carId"), get_now())
                                    try:
                                        self.database_handler.InsertData("User", key, value)
                                    except Exception as e:
                                        print(e)
                                        pass

                                save_data['attribute'] = json.dumps(attribute)
                                save_data['id'] = GetOrderId()
                                self.database_handler.InsertXiaoFei(save_data)

                            # 清空缓存
                            temp = list()

                    except Exception as e:
                        print(e)
                        continue
                else:
                    # 若不是用软件导出的EXCEL文档则
                    # 先整理参数，全部变成列表，列表里面是字典，字典的key就是title
                    try:
                        row_data = sh.row_values(i)
                        temp_data = dict()

                        for k in range(len(title)):
                            temp_data[title[k]] = row_data[k]
                        msg_list.append(temp_data)
                    except Exception as e:
                        print(e)
                        continue

            if not match_result:
                save_list = defaultdict(list)
                for msg in msg_list:
                    if not msg.get("消费时间") or not msg.get("车牌号"):
                        continue

                    key = msg.get("消费时间") + msg.get("车牌号")
                    save_list[key].append(msg)

                # 插入信息
                must = ["订单号", "接待门店", "车牌号", "车主姓名", "联系电话", "车型", "操作人员", "消费项目", "消费时间"]
                for k, v in save_list.items():
                    if progress_dialog.wasCanceled():
                        break
                    progress_dialog.setValue(p)
                    p += 1
                    order_check_id = GetOrderId()
                    # 对同一个订单进行录入
                    user_save = {}
                    for tempDict in v:
                        order_no = str(tempDict.pop("订单号")) if tempDict.get("订单号", "") != "" else "-"
                        pc_sign = tempDict.pop("接待门店", "") if tempDict.get("接待门店", "") != "" else "-"
                        car_id = tempDict.pop("车牌号") if tempDict.get("车牌号") != "" else "-"
                        car_user = tempDict.pop("车主姓名", "") if tempDict.get("车主姓名", "") != "" else "-"
                        car_phone = str(tempDict.pop("联系电话", "-")).replace(".0", "") if tempDict.get("联系电话",
                                                                                                     "") != "" else "-"
                        car_model = tempDict.pop("车型", "") if tempDict.get("车型", "") != "" else "-"
                        worker_name = tempDict.pop("操作人员", "") if tempDict.get("操作人员", "") != "" else "-"
                        project = tempDict.pop("消费项目", "") if tempDict.get("消费项目", "") != "" else "-"
                        created_time = str(tempDict.pop("消费时间")).replace(".", "-")
                        # 保存用户信息
                        user_save["carId"] = car_id if car_id != '-' else ""
                        user_save["carUser"] = car_user if car_user != '-' else ""
                        user_save["carPhone"] = (car_phone if car_phone != '-' else "").replace(".0", "")
                        user_save['carModel'] = car_model if car_model != '-' else ""

                        if order_no != "-":
                            check_order = self.database_handler.GetXiaoFeiByKey("orderNo", order_no)
                            if check_order:
                                break

                        save_data = {
                            "orderNo": order_no.replace(".0", ""),
                            "createdTime": created_time,
                            "pcSign": pc_sign,
                            "carId": car_id,
                            "carUser": car_user,
                            "carPhone": car_phone,
                            "carModel": car_model,
                            "workerName": worker_name,
                            "project": project,
                            "orderCheckId": order_check_id,
                            "id": GetOrderId(),
                        }
                        temp_attribute = tempDict

                        attribute = dict()
                        for key, value in temp_attribute.items():
                            if k not in must:
                                if value == "":
                                    continue
                                attribute[key] = str(value)
                        try:
                            gsf = float(attribute.get("工时费")) if attribute.get("工时费") != "" else 0
                            sl = float(attribute.get("数量")) if attribute.get("数量") != "" else 0
                            dj = float(attribute.get("单价")) if attribute.get("单价") != "" else 0
                            attribute["总价"] = gsf + sl * dj
                        except Exception as e:
                            print(e)
                            pass
                        save_data["attribute"] = json.dumps(attribute)
                        self.database_handler.InsertXiaoFei(save_data)

                    if user_save.get("carId") and user_save.get("carPhone"):
                        # 当有用户信息的时候判断是否需要自动添加
                        user = self.database_handler.CheckUser(user_save.get("carPhone"), user_save.get("carId"))
                        if not user:
                            # 没有此用户则添加
                            key = "userName,carPhone,carModel,carId,createdTime"
                            value = "'{}','{}','{}','{}','{}'".format(user_save.get("carUser"),
                                                                      user_save.get("carPhone"),
                                                                      user_save.get("carModel"), user_save.get("carId"),
                                                                      get_now())
                            try:
                                self.database_handler.InsertData("User", key, value)
                            except Exception as e:
                                print(e)
                                pass
            # 最后全部导入
            progress_dialog.setValue(rows - 3)
            progress_dialog.close()

    def export_sale_detail(self, start_time, end_time, remote=False):
        now = get_now()
        file_name = now + ".xls"

        # 获取消费信息
        sale_detail_list = []
        if remote:
            # 获取远程信息
            root = 'config.ini'
            basic_msg = configparser.ConfigParser()
            basic_msg.read(root)
            code = basic_msg.get('msg', 'code')
            keyword = "xiaofei {} {} {}".format(code, start_time, end_time)
            # python3传递的是bytes，所以要编码
            try:
                sale_detail_list = SocketServer(keyword)
            except Exception as e:
                print(e)
        else:
            sale_detail_list = self.database_handler.GetXiaoFeiTable(start_time, end_time, Table=False)

        # 填入数据
        if sale_detail_list:
            # 插入信息
            sale_detail_list.sort(key=lambda obj: obj[2], reverse=True)
            order_check_id = None
            merge_list = list()
            temp_msg = dict()
            temp = list()
            # 设置表头
            title_list = ["检索ID", '订单号', u'消费时间', "消费门店", u"车牌号", u"车主姓名", u"联系电话", u"车型", u"操作人员",
                          u"消费项目"]

            table_len = len(title_list)
            header = ['数量', '单价', '小计', '总价', '单位', '备注']
            for data in sale_detail_list:
                try:
                    attribute = json.loads(data[10])
                    for k, v in attribute.items():
                        if k not in header:
                            header.append(k)
                except Exception as e:
                    print(e)
                    continue
            title_list = title_list + header
            all_table_len = len(title_list)

            wb = xlwt.Workbook()
            ws = wb.add_sheet('消费列表', cell_overwrite_ok=True)
            title = set_style('Arial', 250, True, True)
            default = set_style('SimSun', 180, True, True, True)
            top = set_style('Times New Roman', 350, True, True)
            # 前两个参数表示需要合并的行范围，后两个参数表示需要合并的列范围
            # 合并单元格作为大标题，水平居中即可
            start_time = format_time(start_time)[:10]
            end_time = format_time(end_time)[:10]
            ws.write_merge(0, 0, 0, all_table_len - 1, '门店系统:{}至{}'.format(start_time, end_time), top)

            # 设置标题
            for i in range(all_table_len):
                # 设置单元格宽度
                ws.col(i).width = 265 * 20
                # 插入标题
                ws.write(1, i, title_list[i], title)

            # 从第二行开始插
            row = 2

            for data in sale_detail_list:
                if order_check_id:
                    # 如果记录的订单号与当前数据的订单号不同，则进行录入并修改记录订单号
                    if order_check_id != data[0]:
                        order_check_id = data[0]

                        # 因为订单号变了所以之前的缓存清空，换成这个订单号的索引
                        temp = [row]
                    else:
                        # 若已经缓存了2个索引则代表此订单号有>2个商品，所以更新第二个索引保留第一个索引
                        if len(temp) >= 2:
                            temp[1] = row
                        else:
                            temp.append(row)
                else:
                    # 若第一次进来，此时订单号是None，进行录入
                    order_check_id = data[0]
                    temp.append(row)

                # 插入信息
                for j in range(table_len):
                    ws.write(row, j, data[j], default)
                    if j == table_len - 1:
                        # 最后一个的时候遍历填入数据
                        try:
                            j += 1
                            attribute = json.loads(data[j])
                            for k in header:
                                ws.write(row, j, attribute.get(k, ""), default)
                                j += 1
                        except Exception as e:
                            print(e)
                            continue
                row += 1
                # 如果已经缓存了2个数字，则代表有重复的订单号，所以此时进行记录并合并
                if len(temp) >= 2:
                    temp_msg[temp[0]] = MakeTempMsg(data)
                    merge_list.append(temp)

            if len(temp) >= 2:
                merge_list.append(temp)
                temp_msg[temp[0]] = MakeTempMsg(data)
            for hb in merge_list:
                ws.write_merge(hb[0], hb[1], 0, 0, temp_msg[hb[0]].get("checkOrderId"), default)
                ws.write_merge(hb[0], hb[1], 1, 1, temp_msg[hb[0]].get("orderNo"), default)
                ws.write_merge(hb[0], hb[1], 2, 2, temp_msg[hb[0]].get("createdTime"), default)
                ws.write_merge(hb[0], hb[1], 3, 3, temp_msg[hb[0]].get("pcSign"), default)
                ws.write_merge(hb[0], hb[1], 4, 4, temp_msg[hb[0]].get("carId"), default)
                ws.write_merge(hb[0], hb[1], 5, 5, temp_msg[hb[0]].get("carUser"), default)
                ws.write_merge(hb[0], hb[1], 6, 6, temp_msg[hb[0]].get("carPhone"), default)
                ws.write_merge(hb[0], hb[1], 7, 7, temp_msg[hb[0]].get("carModel"), default)
                ws.write_merge(hb[0], hb[1], 8, 8, temp_msg[hb[0]].get("workerName"), default)

            if not os.path.exists(savePath):
                os.mkdir(savePath)
            wb.save(savePath + file_name)

            return file_name
        else:
            return False

    # 用于正则判断是否是用软件导出的excel文档
    @staticmethod
    def _is_from_export(first_cell_str):
        pattern = re.compile(r"^门店系统:\d{4}[-/]\d{2}[/-]\d{2}至\d{4}[-/]\d{2}[/-]\d{2}$")
        return pattern.match(first_cell_str)
