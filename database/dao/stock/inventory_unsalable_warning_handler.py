from database.db_connection import execute
from domain.stock_detail import StockDetail

def get_negative_on_hand():
    sql_text = '''
                  select
                       si.brand_name,
                       si.model_name,
                       sum(left_number) as sum,
                       max(julianday(date('now'))-julianday(bi.buy_date))
                from
                       buy_info bi,
                       stock_info si
                where   bi.stock_id=si.id
                  and  julianday(date('now'))-julianday(bi.buy_date)>90          
                  GROUP BY  si.model_id''' \
        .format(StockDetail.by_bought())

    result = execute(sql_text)
    return result