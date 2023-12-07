from playwright.sync_api import expect
from retry import retry


class transactionsPage():
    def __init__(self, page):
        self.__page = page
        self.__reset_button = self.__page.get_by_text("Reset")
        self.__back_button = self.__page.get_by_text("Back")
        self.__table_locator = "table.table-bordered"
        self.__table_tr_locator = self.__table_locator+" tr"


    def reset_table_and_back(self):
        if (self.__reset_button.is_visible()):
            self.__reset_button.click()
        rows = self.__page.query_selector_all("tr")
        assert len(rows) == 0, "Rows are still appears into Transactions table after reset "
        self.__back_button.click()

    def get_table_row_data(self, row_index: int) -> dict:
        expect(self.__back_button).to_be_visible()
        row_data = {}
        rows = self.__page.locator(self.__table_tr_locator)
        row_text = rows.nth(row_index).inner_text()
        cols = row_text.split("\t")
        row_data["date"] = cols[0]
        row_data["amount"] = cols[1]
        row_data["type"] = cols[2]

        print(f"the following row data found {row_text}")
        return row_data
