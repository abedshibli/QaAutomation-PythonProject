import time

import pytest

from Main import Utilities
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.web_actions import Web_Actions

class Web_WF:

    @staticmethod
    def register(first_name, last_name, username, password):
        Web_Actions.click_action(Utilities.manage_pages.login_page.get_signup_page())
        Web_Actions.click_action(Utilities.manage_pages.login_page.get_signup_page())
        Web_Actions.insert_value(first_name, Utilities.manage_pages.register_page.get_first_name())
        Web_Actions.insert_value(last_name, Utilities.manage_pages.register_page.get_last_name())
        Web_Actions.insert_value(username, Utilities.manage_pages.register_page.get_username())
        Web_Actions.insert_value(password, Utilities.manage_pages.register_page.get_password())
        Web_Actions.insert_value(password, Utilities.manage_pages.register_page.get_confirm_password())
        Web_Actions.click_action(Utilities.manage_pages.register_page.get_signup_btn())
        time.sleep(3)

    @staticmethod
    def login(username, password):
        Web_Actions.insert_value(username, Utilities.manage_pages.login_page.get_username())
        Web_Actions.insert_value(password, Utilities.manage_pages.login_page.get_password())
        Web_Actions.click_action(Utilities.manage_pages.login_page.get_signin_btn())
        time.sleep(3)

    @staticmethod
    def new_bank_account(bank_name, routing_num, account_num ):
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_next_btn())
        Web_Actions.insert_value(bank_name, Utilities.manage_pages.bank_account_page.get_bank_name())
        Web_Actions.insert_value(routing_num, Utilities.manage_pages.bank_account_page.get_routing_number())
        Web_Actions.insert_value(account_num, Utilities.manage_pages.bank_account_page.get_account_number())
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_save_btn())
        time.sleep(3)
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_done_btn())


    @staticmethod
    def current_connected_user():
        return Web_Actions.get_text(Utilities.manage_pages.main_page.get_current_connected_user())

    @staticmethod
    def logout_user():
        return Web_Actions.click_action(Utilities.manage_pages.main_page.get_logout_btn())

    @staticmethod
    def get_balance_text():
        return Web_Actions.get_text(Utilities.manage_pages.main_page.get_balance())






