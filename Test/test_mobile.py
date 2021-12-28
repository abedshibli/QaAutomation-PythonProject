import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.Utilities.common_ops import Common_Ops
from Main.WorkFlows.mobile_wf import Mobile_WF


@pytest.mark.usefixtures('init_mobile')
class Test_Mobile:

    @allure.title("verify the title")
    @allure.description("This test verify the title of an app")
    def test_1(self):
        Verifications.verify_equals(Mobile_WF.search_flow(), Common_Ops.get_data("expectedMobile1"))

    @allure.title("verify the result of calculate")
    @allure.description("This test verify the result of multiply 2 numbers")
    def test_2(self):
        Mobile_WF.calculate("'4'", "'×'", "'6'")
        Verifications.verify_equals(Mobile_WF.get_result_text(), Common_Ops.get_data("expectedMobile2"))
