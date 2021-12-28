import time
import pytest

from Main.Extensions.verfications import Verifications
from Main.Utilities.DDT.manage_ddt import DDT
from Main.WorkFlows.web_wf import Web_WF
from Test import conftest


@pytest.mark.usefixtures('init_web')
class Test_web():

    def test_01(self):
        Web_WF.register("Yoni", "Choen", "yonii", "123456")
        Web_WF.login("yonii", "123456")
        Web_WF.new_bank_account("Leumi", "123456789", "123123123")
        connected_user = Web_WF.current_connected_user()
        Web_WF.logout_user()
        Verifications.verify_equals(connected_user, "@yonii")

    def test_02(self):
        time.sleep(3)
        Web_WF.login("Allie2", "s3cret")
        balance = Web_WF.get_balance_text()
        Web_WF.logout_user()
        Verifications.verify_equals(balance, "$1,648.67")

    @pytest.mark.parametrize("username,password", DDT.write_to_list_from_csv())
    def test_03(self, username, password):
        Web_WF.login(username, password)
        connected_user = Web_WF.current_connected_user()
        Web_WF.logout_user()
        Verifications.verify_equals(connected_user, '@' + username)

    def test_04(self):
        Web_WF.register("Yoni1", "Choen1", "yooooooooo", "1234567")
        Web_WF.login("yooooooooo", "1234567")
        Web_WF.fill_bank()
        bank_name = Web_WF.check_bank_name()
        Web_WF.logout_user()
        Verifications.verify_equals(bank_name, "leumi")

    def test_05(self):
        Web_WF.login("Allie2", "s3cret")
        Web_WF.dismiss_notification()
        Web_WF.logout_user()
