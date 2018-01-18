from database.db_connection import execute
from domain.stock_detail import StockDetail


def get_unsalable_warning():
    sql_text = '''
                  SELECT
                         si.brand_name,
                         si.model_name,
                         sum(left_number) AS sum,
                         max(julianday(date('now'))-julianday(bi.buy_date))
                    FROM buy_info bi,
                         stock_info si
                   WHERE bi.stock_id=si.id
                     AND bi.left_number > 0
                     AND julianday(date('now'))-julianday(bi.buy_date) >= 90          
                   GROUP BY si.model_id''' \
        .format(StockDetail.by_bought())

    result = execute(sql_text)
    return result
