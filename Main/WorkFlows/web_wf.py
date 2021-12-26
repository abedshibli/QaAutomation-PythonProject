import time

from Main import utilities
from Main.utilities.manage_pages import Manage_Pages

class Web_WF:

    @staticmethod
    def create_new_account(first_name, last_name, username, password):
        time.sleep(4)
        utilities.manage_pages.login_page.get_signup_page().click()
        utilities.manage_pages.login_page.get_signup_page().click()
        time.sleep(4)
        utilities.manage_pages.register_page.get_first_name().send_keys(first_name)
        utilities.manage_pages.register_page.get_last_name().send_keys(last_name)
        utilities.manage_pages.register_page.get_username().send_keys(username)
        utilities.manage_pages.register_page.get_password().send_keys(password)
        utilities.manage_pages.register_page.get_confirm_password().send_keys(password)
        utilities.manage_pages.register_page.get_signup_btn().click()

    @staticmethod
    def login(username, password):
        utilities.manage_pages.login_page.get_username().send_keys(username)
        utilities.manage_pages.login_page.get_password().send_keys(password)
        utilities.manage_pages.login_page.get_signin_btn().click()
