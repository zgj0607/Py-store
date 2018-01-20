from controller.Interface.TableHandler import xiaofeiTableSet
from view.sale.sale_base import SaleBase


class LocalSale(SaleBase):
    def __init__(self):
        super(LocalSale, self).__init__()
        self.setWindowTitle('本店销售')
        self.details_query_button.clicked.connect(self._local_store_sale_search)

    def _local_store_sale_search(self):
        start_date = self.start_date.text()
        end_date = self.end_date.text()
        result_str = xiaofeiTableSet(self.sales_details_result_table, start_date, end_date, False)
        self.sales_details_result_table.resizeColumnsToContents()
        self._result_process(result_str)
