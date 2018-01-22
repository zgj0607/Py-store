from controller.view_service.table_service import xiaofeiTableSet
from view.sale.sale_base import SaleBase


class AllSale(SaleBase):
    def __init__(self):
        super(AllSale, self).__init__()
        self.setWindowTitle('全店销售')
        self.details_query_button.clicked.connect(self._all_store_sale_search)

    def _all_store_sale_search(self):
        start_date = self.start_date.text()
        end_date = self.end_date.text()
        result_str = xiaofeiTableSet(self.sales_details_result_table, start_date, end_date, True)
        self.sales_details_result_table.resizeColumnsToContents()
        self._result_process(result_str)
