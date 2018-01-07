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


def get_operation_by_time(start_date: str, end_date: str):
    sql_text = '''select   srv.name as faname,
                           serv.name,
                           count(*) as ordercount,
                           count(*) as carcount,
                           sum(sal.number) as salnumber,
                           sum(sal.number*sal.price) as totalprice,
                           sum(sal.number*sal.price)-buyp.totalby
                    from   Sales sal ,
                           service serv,
                           service srv,
                          (select sum(b.buy_price) as totalby,
                                  b.sale_id
                           from sales a,
                                stock_detail b
                           where a.id=b.sale_id 
                                 and a.sale_date BETWEEN '{}' AND '{}'
                           group by b.sale_id) buyp
                    where  sal.project=serv.id
                           and buyp.sale_id=sal.id
                           and sal.sale_date BETWEEN '{}' AND '{}'
                           and serv.father=srv.id GROUP BY  sal.project;
                 '''\
        .format(start_date, end_date,start_date, end_date)
    result = db_common_handler.execute(sql_text)
    return result
