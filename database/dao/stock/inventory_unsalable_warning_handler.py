from database.db_connection import execute
from domain.stock_detail import StockDetail

def get_negative_on_hand():
    sql_text = '''
                select 
                       si.brand_name,
                       si.model_name,
                       count(*) as sum,
                       max(julianday(date('now'))-julianday(bi.buy_date))
                from   stock_detail sd,
                       buy_info bi,
                       stock_info si
                where  sd.type={} 
                  and  sd.buy_id=bi.id 
                  and  si.id=sd.stock_id 
                  and  julianday(date('now'))-julianday(bi.buy_date)>90
                GROUP BY  si.model_id''' \
        .format(StockDetail.in_store())

    result = execute(sql_text)
    return result