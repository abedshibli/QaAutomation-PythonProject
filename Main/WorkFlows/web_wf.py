import time

from Main import Utilities
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.web_actions import Web_Actions

class Web_WF:

    @staticmethod
    def create_new_account(first_name, last_name, username, password):
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

