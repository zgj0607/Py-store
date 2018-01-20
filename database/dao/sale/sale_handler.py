from common import common
from database.db_connection import execute


def get_sale_detail(start_time, end_time, YeJi=False, Table=True):
    start_time = common.format_time(start_time)
    end_time = common.format_time(end_time, True)
    if Table:
        sql_text = '''
                    SELECT orderNo,
                           createdTime,
                           pcSign,
                           carId,carUser,
                           carPhone,
                           carModel,
                           workerName,
                           project,
                           attribute,
                           orderCheckId
                      FROM Sales
                     WHERE createdTime BETWEEN \'{}\' and \'{}\'
                     ORDER BY createdTime DESC ''' \
            .format(start_time, end_time)
    else:
        sql_text = '''
                    SELECT orderCheckId,
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
                      FROM Sales
                     WHERE createdTime BETWEEN \'{}\' and \'{}\'
                     ORDER BY createdTime DESC ''' \
            .format(start_time, end_time)
    data = execute(sql_text)
    return data


# 插入消费信息
def add_sale_detail(save_data):
    sql_text = '''
                  INSERT INTO Sales(id,
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
                  VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')''' \
        .format(
        save_data.get('id'),
        save_data.get('orderNo', ""),
        save_data.get('carId', ""),
        save_data.get('pcId', ""),
        save_data.get('workerId', ""),
        save_data.get('userId', ""),
        save_data.get('workerName', ""),
        save_data.get('code', ""),
        save_data.get('carUser', ""),
        save_data.get('attribute', ""),
        save_data.get('pcSign', ""),
        save_data.get('carPhone', ""),
        save_data.get('carModel', ""),
        save_data.get('project', ""),
        save_data.get('createdTime', ""),
        save_data.get('orderCheckId', "")
    )
    execute(sql_text)


def get_order_no(today):
    month = str(today.month)
    day = str(today.day)
    year = today.year
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day

    start_time = '{}-{}-{} 00:00:00'.format(year, month, day)
    end_time = '{}-{}-{} 23:59:59'.format(year, month, day)

    sql_text = '''SELECT count(1) FROM Sales WHERE createdTime BETWEEN \'{}\' AND \'{}\''''.format(start_time, end_time)
    data = execute(sql_text)
    number = str(len(data) + 1)

    # number格式为百位数，如001，002，100，120
    if len(number) < 2:
        number = "00" + number
    elif len(number) < 3:
        number = "0" + number

    order_no = "{}{}{}{}".format(year, month, day, number)
    return order_no


def get_sale_info_by_one_key(key, value, remote=False):
    if remote:
        sql_str = '''
                    SELECT createdTime,
                           orderNo,
                           carId,
                           carUser,
                           carPhone,
                           carModel,
                           workerName,
                           project,
                           attribute,
                           pcId,
                           orderCheckId,
                           pcSign,
                           unit_price,
                           unit,
                           number,
                           subtotal,
                           total,
                           note,
                           id
                      FROM Sales
                     WHERE {}='{}'
                       AND userId != ''
                       AND userId IS NOT NULL
                     ORDER BY createdTime DESC''' \
            .format(key, value)
    else:
        sql_str = '''SELECT createdTime,
                           orderNo,
                           carId,
                           carUser,
                           carPhone,
                           carModel,
                           workerName,
                           project,
                           attribute,
                           pcId,
                           orderCheckId,
                           pcSign,
                           unit_price,
                           unit,
                           number,
                           subtotal,
                           total,
                           note,
                           id
                      FROM Sales
                     WHERE {}='{}'
                    ORDER BY createdTime DESC''' \
            .format(key, value)
    data = execute(sql_str)
    return data


def get_sale_order_no(today):
    month = str(today.month)
    day = str(today.day)
    year = today.year
    month = month.ljust(2, "0")
    day = day.ljust(2, "0")

    start_time = '{}-{}-{} 00:00:00'.format(year, month, day)
    end_time = '{}-{}-{} 23:59:59'.format(year, month, day)

    sql_str = '''SELECT count(1) FROM Sales WHERE createdTime BETWEEN '{}' and '{}' group by OrderNo''' \
        .format(start_time, end_time)

    data = execute(sql_str)
    number = str(len(data) + 1)
    # number格式为百位数，如001，002，100，120
    if len(number) < 2:
        number = "00" + number
    elif len(number) < 3:
        number = "0" + number

    order_no = "{}{}{}{}".format(year, month, day, number)
    return order_no


# 插入消费信息
def add_sale_info(save_data):
    sqlStr = '''INSERT INTO Sales(id,
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
                                  orderCheckId,
                                  unit,
                                  unit_price,
                                  number,
                                  subtotal,
                                  total,
                                  note,
                                  service_id)
                VALUES ('{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        {:.2f},
                         {},
                        {:.2f},
                        {:.2f},
                        '{}',
                         {}
                        )''' \
        .format(save_data.get('id'), save_data.get('orderNo', ""), save_data.get('carId', ""),
                save_data.get('pcId', ""), save_data.get('workerId', ""), save_data.get('userId', ""),
                save_data.get('workerName', ""), save_data.get('code', ""), save_data.get('carUser', ""),
                save_data.get('attribute', ""), save_data.get('pcSign', ""), save_data.get('carPhone', ""),
                save_data.get('carModel', ""), save_data.get('project', ""), save_data.get('createdTime', ""),
                save_data.get('orderCheckId', ""), save_data.get('unit', ''), save_data.get('unit_price', 0.0),
                save_data.get('number', 0), save_data.get('subtotal', 0.0), save_data.get('total', 0.0),
                save_data.get('note', ''), save_data.get('serviceId', 0),
                )
    return execute(sqlStr)
