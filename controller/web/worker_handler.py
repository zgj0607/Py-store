from tornado.concurrent import run_on_executor

from common import config
from common.exception import ApiException
from common.static_func import ErrorCode, set_return_dicts
from controller.web.base_handler import BaseHandler
from database.dao.users import user_handler
from remote import store_pc_info


class WorkerHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(WorkerHandler, self).__init__(application, request, **kwargs)
        self.func = self.worker

    @run_on_executor
    def worker(self, keyword, get_data):
        try:
            if self.request.method == 'POST':
                if keyword == "code":
                    code = get_data.get("code", "").strip()

                    local_code = config.get_local_register_code()
                    if code != "" and local_code == code:
                        # 请求获取门店信息
                        data = store_pc_info.get_store_detail()
                        if not self.connect or not data:
                            store = config.get_local_store_info()
                            data = {
                                'data': {
                                    "pcId": store.id(),
                                    "pcPhone": store.phone(),
                                    "pcAddress": store.address(),
                                    "pcSign": store.name(),
                                },
                                'code': 200
                            }
                        if data.get('code') == 200:
                            result = data.get("data")
                        else:
                            raise ApiException(ErrorCode.CodeError)
                    else:
                        raise ApiException(ErrorCode.CodeError)

                    return set_return_dicts(result)

                elif keyword == "ip":
                    return set_return_dicts(True)

                else:
                    raise ApiException(ErrorCode.ErrorRequest)

            elif self.request.method == "GET":
                if keyword == "list":
                    worker = user_handler.get_all_staff()
                    worker_list = list()
                    for data in worker:
                        worker_list.append({
                            "workerId": data[0],
                            "workerName": data[1]
                        })
                    return set_return_dicts(worker_list)
                else:
                    raise ApiException(ErrorCode.ErrorRequest)

        except ApiException as e:
            return set_return_dicts(forWorker=e.error_result['forWorker'],
                                    code=e.error_result['errorCode'],
                                    forUser=e.error_result['forUser'])
