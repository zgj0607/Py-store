import configparser
import json
from collections import OrderedDict

import requests
from PyQt5.QtCore import QSizeF, Qt
from PyQt5.QtGui import QTextOption, QTextDocument
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter

from Common.Common import cncurrency
from Common.config import domain
from Controller.DbHandler import DB_Handler


def do_print(main_windows, order_no):
    try:
        printer = QPrinter(QPrinter.HighResolution)
        # /* 打印预览 */
        preview = QPrintPreviewDialog(printer, main_windows)
        preview.paintRequested.connect(printHtml)
        global selectOrderNo
        selectOrderNo = order_no
        preview.exec_()
        return True

    except Exception as e:
        print(e)
        return False


def printHtml(printer):
    root = 'config.ini'
    basic_msg = configparser.ConfigParser()
    basic_msg.read(root)
    try:
        if not myconnect:
            raise TimeoutError
        code = basic_msg.get("msg", 'code')
        url = domain + "store/api/detail?code={}".format(code)
        req = requests.get(url=url)
        result_data = json.loads(req.text)
    except Exception as e:
        print(e)

        fp = open("pc.conf", 'rb')
        pc_data = fp.readline().decode()
        fp.close()
        pc_data = pc_data.split(',')

        if len(pc_data) < 4:
            pc_data = [pc_data[0], "", "", ""]

        result_data = {
            'data': {
                "pcId": pc_data[0],
                "pcPhone": pc_data[1],
                "pcAddress": pc_data[2],
                "pcSign": pc_data[3],
            },
            'code': 200
        }
    must_set = ['数量', '单价', '小计', '总价', '单位', '备注']

    if result_data.get("code") != 200:
        store_name = ""
        pc_address = ""
        pc_phone = ""
    else:
        store_name = result_data.get("data").get("pcSign", "")
        pc_address = result_data.get("data").get("pcAddress", "")
        pc_phone = result_data.get("data").get("pcPhone", "")
    result = DB_Handler.GetXiaoFeiByKey("orderCheckId", selectOrderNo)

    fp = open("printer.txt", 'rb')
    data = fp.readline().decode().replace("\n", "").replace("\r", "").replace("\ufeff", "")
    fp.close()
    font_size = 7
    if data:
        try:
            font_size = int(data)
        except Exception as e:
            print(e)
            font_size = 7

    # *{font-size:65px;}
    if result:
        header = """<html>
            <style>
            table{
                background-color:#000000;
            }

            .linetd{
                text-align: center;
                width: 820px;
                color: red;
                height: 30px;
            }

            .halftd{
                width: 410px;
            }

            #content{
                text-align: center;
                position: relative;
                top: 50%;
                transform: translateY(-50%);
            }

            td{
                padding:2px;
                align:center;
                border:1px solid black;
                background-color:#ffffff
            }

        """ + "*{font-size:" + str(font_size) + "pt;}" + ".bigWord{font-size:" + str(
            font_size * 1.5) + "pt;}" + "</style><head></head>"
        # *{font-size:50px;}
        td_width = 19
        body = """
            <body style="text-align: center;">
                <table width=100% CELLPADDING="0" CELLSPACING="1" border="0">
                    <tr>
                        <td class="bigWord" align="center" colspan="100" width="100%">
                            {storeName}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="50">车牌号：{carId}</td>
                        <td colspan="50">销售日期：{createdTime}</td>
                    </tr>
                    <tr>
                        <td colspan="50">客户电话：{carPhone}</td>
                        <td colspan="50">销售单号：<span style="">{orderNo}</span></td>
                    </tr>
                    <tr>
                        <td colspan="100" height="20px"> </td>
                    </tr>

                    """.format(storeName=store_name, carId=result[0][2], createdTime=result[0][0],
                               carPhone=result[0][4],
                               orderNo=result[0][1])

        content = ""
        seq = 1
        total_price = 0
        page = 0
        page_height = 100
        for order in result:
            page += 1
            attribute = json.loads(order[8])
            base_height = 180
            # 手动排序
            # mustSet = ['数量','单价','小计','总价','单位','备注']
            # 去除mustset后的必然顺序为："品牌","型号","工时费","更换里程"
            # 后面用字符串排序key来排序
            temp_key_list2 = ["品牌", "型号", "工时费", "更换里程"]
            temp_key_list = list()
            for t in temp_key_list2:
                if attribute.get(t) and attribute.get(t) != '-':
                    temp_key_list.append(t)

            for k, v in attribute.items():
                if k not in must_set + ["品牌", "型号", "工时费", "更换里程"] and v != "-" and v != "" and k != "检索ID":
                    temp_key_list.append(k)
            temp_key_list.sort()
            no_must_set = OrderedDict()
            for k in temp_key_list:
                no_must_set[k] = attribute.get(k)
            # 总长度要减去备注和名称，因为名称长度另外设置，备注不打印
            td = ""
            key_dict = dict()
            i = 0
            j = 0
            td_list = list()
            key_list = list()
            page_height += int(len(no_must_set.keys()) / 5 + 1) * 60 + base_height
            for k, v in no_must_set.items():
                # if k not in mustSet and v != "-"  and v != "" and k!="检索ID" :
                td += "<td colspan=\"{tdWidth}\" align=\"center\"><b>{key}</b></td>".format(tdWidth=td_width, key=k)
                key_list.append(k)
                if i >= 4:
                    i = 0
                    td_list.append(td)
                    td = ""
                    key_dict[j] = key_list
                    key_list = list()
                    j += 1
                else:
                    i += 1

            # 补齐
            if key_list:
                if len(key_list) < 5:
                    num = len(key_list)
                    for i in range(5 - num):
                        key_list.append("")
                        td += "<td colspan=\"{tdWidth}\" align=\"center\"></td>".format(tdWidth=td_width)
                td_list.append(td)
                key_dict[j] = key_list
            # 序号合并列数
            merge_num = len(td_list) * 2 + 2
            # createdTime,orderNo,carId,carUser,carPhone,carModel,workerName,project,brand," \
            # "model,huawen,number,unitPrice,xiaoji,gongshi,ghlc,remark,totalPrice,pcId,unit
            content += """
                <tr>
                        <td colspan="5" align="center"><b>序</b></td>
                        <td colspan="{tdWidth}" align="center"><b>名称</b></td>
                        <td colspan="{tdWidth}" align="center"><b>单位</b></td>
                        <td colspan="{tdWidth}" align="center"><b>数量</b></td>
                        <td colspan="{tdWidth}" align="center"><b>单价</b></td>
                        <td colspan="{tdWidth}" align="center"><b>小计</b></td>
                    </tr>
                <tr>
                    <td rowspan="{xuNum}" colspan="5" align="center"><br/>{xuhao}</td>
                    <td colspan="{tdWidth}" align="center">{project}</td>
                    <td colspan="{tdWidth}" align="center">{unit}</td>
                    <td colspan="{tdWidth}" align="center">{number}</td>
                    <td colspan="{tdWidth}" align="center">{unitPrice}</td>
                    <td colspan="{tdWidth}" align="center">{xiaoji}</td>
                </tr>

            """.format(xuNum=merge_num, xuhao=seq, unit=attribute.get("单位", ""), number=attribute.get("数量", ""),
                       unitPrice=attribute.get("单价", ""),
                       xiaoji=attribute.get('小计', ""), project=order[7], tdWidth=td_width)

            more_content = ""
            ii = 0
            for td in td_list:
                # 先放入表头
                more_content += "<tr>" + td + "</tr>"
                # 再放入内容
                more_content += """
                    <tr>
                    <td colspan="{tdWidth}" align="center">{one}</td>
                    <td colspan="{tdWidth}" align="center">{two}</td>
                    <td colspan="{tdWidth}" align="center">{three}</td>
                    <td colspan="{tdWidth}" align="center">{four}</td>
                    <td colspan="{tdWidth}" align="center">{five}</td>
                    </tr>
                """.format(tdWidth=td_width, one=attribute.get(key_dict[ii][0], ""),
                           two=attribute.get(key_dict[ii][1], ""),
                           three=attribute.get(key_dict[ii][2], ""), four=attribute.get(key_dict[ii][3], ""),
                           five=attribute.get(key_dict[ii][4], ""))

                ii += 1
            fenge = """
            <tr>
                <td colspan="100" height="20px"> </td>
            </tr>
                """

            zongjiaconetent = """
                <tr>
                    <td colspan="95">总价：{zongjia}</td>
                </tr>
            """.format(zongjia=attribute.get('总价', ""))
            content += more_content + zongjiaconetent + fenge
            seq += 1
            try:
                total_price += float(attribute.get('总价', 0))
            except Exception as e:
                print(e)
                total_price = 0

        total_price = str(total_price)
        cn = cncurrency(total_price)

        foot = """
            <tr>
                <td style="height:35px" colspan="70">合计人名币（大写）：{cn}</td>
                <td style="height:35px"  colspan="30">小写：{zongjia}</td>
            </tr>
            <tr>
                <td colspan="30">{storeName}</td>
                <td colspan="35">地址：{pcAddress}</td>
                <td colspan="35">联系电话：{pcPhone}</td>
            </tr>
        </table>
        </body>
        </html>
        """.format(cn=cn, zongjia=total_price, storeName=store_name, pcPhone=pc_phone, pcAddress=pc_address)

        html = header + body + content + foot
        text_document = QTextDocument()
        text_document.setHtml(html)
        text_document.setDocumentMargin(35)
        printer.setPageSize(QPrinter.Custom)
        # height = baseHeight+((page-1)*150)
        # printer.setPaperSize(QSizeF(printer.logicalDpiX()*(86/25.4),height),QPrinter.Point)
        # textDocument.setPageSize(QSizeF(printer.logicalDpiX()*(86/25.4),height))
        printer.setPaperSize(QSizeF(581, page_height), QPrinter.Point)
        text_document.setPageSize(QSizeF(581, page_height))
        textOp = QTextOption()
        textOp.setWrapMode(QTextOption.WrapAnywhere)
        textOp.setAlignment(Qt.AlignCenter)
        text_document.setDefaultTextOption(textOp)
        printer.setOutputFormat(QPrinter.NativeFormat)
        text_document.print(printer)
