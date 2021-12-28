import time

import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.Utilities.DDT.manage_ddt import DDT
from Main.Utilities.common_ops import Common_Ops
from Main.WorkFlows.web_wf import Web_WF


@pytest.mark.usefixtures('init_web')
class Test_web():

    @allure.title("verify register successfully")
    @allure.description("This test verify the site registration was successful")
    def test_01(self):
        Verifications.verify_equals(Web_WF.register_check(), "@" + Common_Ops.get_data("userName1"))

    @allure.title("verify the balance of an exist user")
    @allure.description("This test verify the balance of an exist user")
    def test_02(self):
        Verifications.verify_equals(Web_WF.check_balance(), Common_Ops.get_data("expextedResult"))

    @allure.title("verify login successfully")
    @allure.description("This test verify that multiple users have successfully logged on to the site")
    @pytest.mark.parametrize("username,password", DDT.write_to_list_from_csv())
    def test_03(self, username, password):
        Web_WF.login(username, password)
        connected_user = Web_WF.current_connected_user()
        Web_WF.logout_user()
        Verifications.verify_equals(connected_user, '@' + username)

    @allure.title("verify the name of the bank")
    @allure.description("This test verify the name of the bank in the account")
    def test_04(self):
        Verifications.verify_equals(Web_WF.check_bank_name_flow(), Common_Ops.get_data("expectedBankName4"))

    @allure.title("verify the number of the notifications")
    @allure.description("This test verify that the number of the notifications has change")
    def test_05(self):
        Web_WF.login(Common_Ops.get_data("existUser"), Common_Ops.get_data("existPassword"))
        Web_WF.dismiss_notification()
        Web_WF.logout_user()
