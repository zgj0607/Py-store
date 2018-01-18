from database import db_common_handler
from domain.stock_detail import StockDetail


def get_performance_by_time(time: dict):
    start_time = time['start_time']
    end_time = time['end_time']
    sql_text = '''SELECT
                       first.name  AS first_service,
                       second.name AS second_service,
                       count(1)    AS total_num,
                       sum(unit_price)  AS total_price
                  FROM Sales sale, service second, service first
                 WHERE sale.createdTime BETWEEN '{}' AND '{}'
                   AND sale.service_id = second.id
                   AND second.father = first.id AND first.father = -1
                 GROUP BY first_service, second_service
                 ORDER BY first_service, second_service
                 ''' \
        .format(start_time, end_time)
    result = db_common_handler.execute(sql_text)
    return result


def get_operation_by_time(start_date: str, end_date: str):
    sql_text = '''
                SELECT
                       first_srv.name                                   AS first_name,
                       second_srv.name                                  AS second_name,
                       count(1)                                         AS order_count,
                       count(1)                                         AS car_count,
                       sum(sal.number)                                  AS salnumber,
                       sum(sal.number * sal.unit_price)                 AS total_price,
                       sum(sal.number * sal.unit_price) - buy.total_buy AS gross_profit
                  FROM Sales sal,
                       service second_srv,
                       service first_srv,
                       (SELECT b.changed_money AS total_buy,
                               changed_id
                          FROM stock_detail b
                         WHERE b.type in ({},{},{})) buy
                 WHERE sal.service_id = second_srv.id
                   AND sal.createdTime BETWEEN '{}' AND '{}'
                   AND second_srv.father = first_srv.id
                   AND buy.changed_id = sal.sale_id
                 GROUP BY sal.project''' \
        .format(StockDetail.by_sold(), StockDetail.by_negative(), StockDetail.by_write_off(), start_date, end_date)
    result = db_common_handler.execute(sql_text)
    return result


def get_total_operation_by_time(start_date: str, end_date: str):
    sql_text = '''
                SELECT
                       count(1)                                         AS car_count,
                       sum(sal.number * sal.unit_price)                 AS total_price,
                       sum(sal.number * sal.unit_price) - buy.total_buy AS gross_profit
                  FROM Sales sal,
                       service second_srv,
                       service first_srv,
                       (SELECT b.changed_money AS total_buy,
                               changed_id
                          FROM stock_detail b
                         WHERE b.type in ({},{},{})) buy
                 WHERE sal.service_id = second_srv.id
                   AND sal.createdTime BETWEEN '{}' AND '{}'
                   AND second_srv.father = first_srv.id
                   AND buy.changed_id = sal.sale_id
                 GROUP BY sal.project''' \
        .format(StockDetail.by_sold(), StockDetail.by_negative(), StockDetail.by_write_off(), start_date, end_date)
    result = db_common_handler.execute(sql_text)
    return result
