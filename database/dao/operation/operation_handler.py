from database import db_common_handler


def get_performance_by_time(time: dict):
    start_time = time['start_time']
    end_time = time['end_time']
    sql_text = '''SELECT
                       first.name  AS first_service,
                       second.name AS second_service,
                       count(1)    AS total_num,
                       sum(price)  AS total_price
                  FROM Sales sale, service second, service first
                 WHERE sale.createdTime BETWEEN '{}' AND '{}'
                   AND sale.serviceId = second.id
                   AND second.father = first.id AND first.father = -1
                 GROUP BY first_service, second_service
                 ORDER BY first_service, second_service
                 '''\
        .format(start_time, end_time)
    result = db_common_handler.execute(sql_text)
    return result
