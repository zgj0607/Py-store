import configparser
import json
from _datetime import datetime

from PyQt5 import QtWidgets

from Common.StaticFunc import get_order_id
from View.customer.ui.ui_return_visit_setting import Ui_MainWindow
from database.dao.customer import customer_handler
from database.dao.sale import sale_handler


class ReturnVisitSetting(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, next_visit_time, record_id, car_phone, car_id, car_user):
        super(ReturnVisitSetting, self).__init__()
        self.id = record_id
        self.car_phone = car_phone
        self.car_id = car_id
        self.car_user = car_user
        self.setupUi(self)
        self.next_visit_time = next_visit_time

        self.info_label.setText(
            '''您于<b>{}</b>要回访用户：<b>{}</b><br>联系方式为：<b>{}</b> < br>车牌号为：<b>{}</b> '''
                .format(next_visit_time, car_user, car_phone, car_id))

        self.submit_set.clicked.connect(self.change_state)
        self.do_set_next_date.stateChanged.connect(self.set_time)

    def change_state(self):
        remarks = self.remark.text().strip()
        if not remarks:
            QtWidgets.QMessageBox.information(self.submit_set, "提示", "请输入备注")
        else:
            today = datetime.now()
            get_data = {}
            order_no = sale_handler.get_order_no(today)
            get_data["orderNo"] = order_no
            get_data["createdTime"] = today
            get_data["carUser"] = self.car_user
            get_data["carId"] = self.car_id
            get_data["carPhone"] = self.car_phone

            car_user = get_data.get("carUser", '-')
            user_id = get_data.get("userId", '-')
            worker_id = get_data.get("workerId", "-")
            pc_id = get_data.get("pcId", "-")
            car_phone = get_data.get("carPhone", "-")
            car_model = get_data.get("carModel", "-")
            car_id = get_data.get("carId", "-")
            pc_sign = get_data.get("pcSign", '-')
            worker_name = get_data.get("workerName", '-')
            root = 'config.ini'
            basic_msg = configparser.ConfigParser()
            basic_msg.read(root)
            order_check_id = get_order_id()
            order_id = get_order_id()
            save_data = {
                'createdTime': get_data.get("createdTime").strftime("%Y-%m-%d %H:%M:%S"),
                'userId': user_id,
                'pcId': pc_id,
                'pcSign': pc_sign,
                'carId': car_id,
                'workerName': worker_name,
                'workerId': worker_id,
                'carUser': car_user,
                'carPhone': car_phone,
                'carModel': car_model,
                "orderNo": order_no,
                "orderCheckId": order_check_id,
                'code': basic_msg.get("msg", "code"),
                'attribute': json.dumps({"回访备注": remarks}),
                'project': get_data.get('project', '-'),
                'id': order_id
            }

            sale_handler.add_sale_detail(save_data)

            # 更新回访状态，标记已回访
            customer_handler.update_return_visit_state(self.id, '1')

            # 如果填写了二次回访时间，则写入一条待回访数据
            if self.do_set_next_date.isChecked():
                # 回访设置
                time_str = self.next_date.text()
                time_list = time_str.split('/')
                # XP上的时间是以-分割的
                if len(time_list) < 3:
                    time_list = time_str.split("-")
                # 有时候年份会在以后一个,如：03-25-2016，此时查询数据将出错，因此要判断一下
                if len(time_list[2]) == 4:
                    mon = time_list[0]
                    day = time_list[1]
                    time_list[0] = time_list[2]
                    time_list[1] = mon
                    time_list[2] = day

                time_str = ""
                for t in time_list:
                    if len(t) < 2:
                        t = "0" + t
                    time_str += t + "-"
                time_str = time_str[:-1]
                customer_handler.add_return_visit_data(time_str, car_phone, car_id, car_user, today)

            self.close()

    def set_time(self):
        if self.do_set_next_date.isChecked():
            self.next_date.setEnabled(True)
        else:
            self.next_date.setEnabled(False)
