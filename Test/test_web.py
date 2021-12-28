import time

import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.Utilities.DDT.manage_ddt import DDT
from Main.WorkFlows.web_wf import Web_WF


@pytest.mark.usefixtures('init_web')
class Test_web():

    # @allure.title("verify register successfully")
    # @allure.description("This test verify the site registration was successful")
    # def test_01(self):
    #     Web_WF.register("Yam", "Cohen", "yamiii", "123456")
    #     Web_WF.login("yamiii", "123456")
    #     Web_WF.new_bank_account("Leumi", "123456789", "123123123")
    #     connected_user = Web_WF.current_connected_user()
    #     Web_WF.logout_user()
    #     Verifications.verify_equals(connected_user, "@yamiii")

    # @allure.title("verify the balance of an exist user")
    # @allure.description("This test verify the balance of an exist user")
    # def test_02(self):
    #     time.sleep(3)
    #     Web_WF.login("Allie2", "s3cret")
    #     balance = Web_WF.get_balance_text()
    #     Web_WF.logout_user()
    #     Verifications.verify_equals(balance, "$1,648.67")

    @allure.title("verify login successfully")
    @allure.description("This test verify that multiple users have successfully logged on to the site")
    @pytest.mark.parametrize("username,password", DDT.write_to_list_from_csv())
    def test_03(self, username, password):
        Web_WF.login(username, password)
        connected_user = Web_WF.current_connected_user()
        Web_WF.logout_user()
        Verifications.verify_equals(connected_user, '@' + username)

    # @allure.title("verify the name of the bank")
    # @allure.description("This test verify the name of the bank in the account")
    # def test_04(self):
    #     Web_WF.register("Kuku21", "Choen1", "kuku21", "1234567")
    #     Web_WF.login("kuku21", "1234567")
    #     Web_WF.fill_bank()
    #     bank_name = Web_WF.check_bank_name()
    #     Web_WF.logout_user()
    #     Verifications.verify_equals(bank_name, "leumi")

    # @allure.title("verify the number of the notifications")
    # @allure.description("This test verify that the number of the notifications has change")
    # def test_05(self):
    #     Web_WF.login("Allie2", "s3cret")
    #     Web_WF.dismiss_notification()
    #     Web_WF.logout_user()
