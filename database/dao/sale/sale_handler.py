from Common import Common
from database.db_connection import execute


def get_sale_detail(start_time, end_time, YeJi=False, Table=True):
    start_time = Common.format_time(start_time)
    end_time = Common.format_time(end_time, True)
    if Table:
        sql_text = '''SELECT orderNo,
                           createdTime,
                           pcSign,
                           carId,carUser,
                           carPhone,
                           carModel,
                           workerName,
                           project,
                           attribute,
                           orderCheckId
                      FROM XiaoFei
                     WHERE createdTime BETWEEN \'{}\' and \'{}\'
                     ORDER BY createdTime DESC ''' \
            .format(start_time, end_time)
    else:
        sql_text = '''SELECT orderCheckId,
                           orderNo,
                           createdTime,
                           pcSign,
                           carId,
                           carUser,
                           carPhone,
                           carModel,
                           workerName,
                           project,
                           attribute
                      FROM XiaoFei
                    WHERE createdTime BETWEEN \'{}\' and \'{}\'
                    ORDER BY createdTime DESC ''' \
            .format(start_time, end_time)
    data = execute(sql_text)
    return data


# 插入消费信息
def add_sale_detail(save_data):
    sql_text = '''INSERT INTO XiaoFei(id,
                                      orderNo,
                                      carId,
                                      pcId,
                                      workerId,
                                      userId,
                                      workerName,
                                      code,
                                      carUser,
                                      attribute,
                                      pcSign,
                                      carPhone,
                                      carModel,
                                      project,
                                      createdTime,
                                      orderCheckId)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''\
        .format(
        save_data.get('id'), save_data.get('orderNo', ""), save_data.get('carId', ""), save_data.get('pcId', ""),
        save_data.get('workerId', ""), save_data.get('userId', ""), save_data.get('workerName', ""),
        save_data.get('code', ""),
        save_data.get('carUser', ""), save_data.get('attribute', ""), save_data.get('pcSign', ""),
        save_data.get('carPhone', ""),
        save_data.get('carModel', ""), save_data.get('project', ""), save_data.get('createdTime', ""),
        save_data.get('orderCheckId', "")
    )
    execute(sql_text)
