import pytest
from aiola.xyz_bank.commons.globals import USER, DEPOSIT, WITHDRAWEL
from aiola.xyz_bank.commons.welcome_buttons import welcomeButtons


class TestBankXyz():
    @pytest.mark.flaky(reruns=2)
    def test_transactions_main(self, setup_browser):
        page, login_page, users_page, welcome_page, transactions_page = setup_browser

        login_page.login()
        users_page.select_user(USER)
        welcome_page.click_on_welcome_button(welcomeButtons.TRANSACTIONS)
        transactions_page.reset_table_and_back()
        exp_deposit = welcome_page.set_deposit(DEPOSIT)
        exp_withdrawel = welcome_page.set_withdrawel(WITHDRAWEL)
        welcome_page.click_on_welcome_button(welcomeButtons.TRANSACTIONS)
        act_deposit = transactions_page.get_table_row_data(1)
        act_withdrawel = transactions_page.get_table_row_data(2)
        assert exp_deposit == act_deposit, "One or more Deposit data is not as define"
        assert exp_withdrawel == act_withdrawel, "One or more Withdrawel data is not as define"
