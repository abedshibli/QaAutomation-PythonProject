import time

import allure

from Main import Utilities
from Main.Utilities.common_ops import Common_Ops, eyes
from Main.Utilities.jdbc import JDBC
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.web_actions import Web_Actions


class Web_WF:

    @staticmethod
    @allure.step("register to the web")
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
    @allure.step("login to the web")
    def login(username, password):
        Common_Ops.attach_file()
        Web_Actions.insert_value(username, Utilities.manage_pages.login_page.get_username())
        Web_Actions.insert_value(password, Utilities.manage_pages.login_page.get_password())
        Web_Actions.click_action(Utilities.manage_pages.login_page.get_signin_btn())
        time.sleep(2)
        Common_Ops.attach_file()

    @staticmethod
    @allure.step("create new bank account")
    def new_bank_account(bank_name, routing_num, account_num):
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_next_btn())
        Web_Actions.insert_value(bank_name, Utilities.manage_pages.bank_account_page.get_bank_name())
        Web_Actions.insert_value(routing_num, Utilities.manage_pages.bank_account_page.get_routing_number())
        Web_Actions.insert_value(account_num, Utilities.manage_pages.bank_account_page.get_account_number())
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_save_btn())
        time.sleep(3)
        Web_Actions.click_action(Utilities.manage_pages.bank_account_page.get_done_btn())

    @staticmethod
    @allure.step("check the username of current connected user")
    def current_connected_user():
        return Web_Actions.get_text(Utilities.manage_pages.main_page.get_current_connected_user())

    @staticmethod
    @allure.step("logout from the web")
    def logout_user():
        return Web_Actions.click_action(Utilities.manage_pages.main_page.get_logout_btn())

    @staticmethod
    @allure.step("get the balance")
    def get_balance_text():
        return Web_Actions.get_text(Utilities.manage_pages.main_page.get_balance())

    @staticmethod
    @allure.step("insert details of new bank account from DB")
    def fill_bank():
        JDBC.connect_db()
        Web_WF.new_bank_account(JDBC.get_bank_list_details()[0][0], JDBC.get_bank_list_details()[0][1],
                                JDBC.get_bank_list_details()[0][2])
        JDBC.connect_db().close()

    @staticmethod
    @allure.step("dismiss any notification")
    def dismiss_notification():
        Common_Ops.init_eyes()
        eyes.check_window("start")
        Web_Actions.click_action(Utilities.manage_pages.main_page.get_notifications())
        eyes.check_window("before dismiss notification")
        Web_Actions.click_action(Utilities.manage_pages.notification_page.get_dismiss_btn())
        eyes.check_window("after dismiss notification")
        Common_Ops.close_eyes()

    @staticmethod
    @allure.step("check the name of the bank in the account")
    def check_bank_name():
        Web_Actions.click_action(Utilities.manage_pages.main_page.get_bank_account())
        return Web_Actions.get_text(Utilities.manage_pages.bank_details_page.get_bank_name())
