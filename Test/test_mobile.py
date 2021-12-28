import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.WorkFlows.mobile_wf import Mobile_WF


@pytest.mark.usefixtures('init_mobile')
class Test_Mobile:

    @allure.title("verify the title")
    @allure.description("This test verify the title of an app")
    def test_1(self):
        Mobile_WF.search("TVM Calculator")
        Mobile_WF.click_on_waanted_result("'TVM Calculator'")
        actual_result = Mobile_WF.get_app_title("'TVM Calculator'")
        Mobile_WF.navigate_to_home_page()
        Verifications.verify_equals(actual_result, "TVM Calculator")

    @allure.title("verify the result of calculate")
    @allure.description("This test verify the result of multiply 2 numbers")
    def test_2(self):
        Mobile_WF.calculate("'4'", "'×'", "'6'")
        Verifications.verify_equals(Mobile_WF.get_result_text(), "24")
