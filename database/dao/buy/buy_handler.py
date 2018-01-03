from database.db_common_handler import execute

staff_table_name = "worker"
sys_user_table_name = 'Admin'


def get_all_stock():
    sql_text = '''SELECT
                      bi.id,
                      bi.buyDate,
                      gi.goodModel,
                      gi.goodBrand,
                      bi.number,
                      gi.goodUnit,
                      bi.price,
                      bi.price * bi.number,
                      sl.supplierName,
                      sr.name,
                      bi.payAmount,
                      bi.price * bi.number - bi.payAmount
                    FROM buyInfo bi, goodInfo gi, supplierInfo sl, service sr
                    WHERE bi.goodId = gi.id AND bi.supplierId = sl.supplierId AND sr.id = gi.goodProject'''
    return execute(sql_text)
