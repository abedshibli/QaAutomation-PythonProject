import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.Utilities.common_ops import Common_Ops
from Main.WorkFlows.desktop_wf import Desktop_WF


@pytest.mark.usefixtures('init_desktop')
class Test_desktop:

    @allure.title("verify multiply numbers")
    @allure.description("This test verify the result of multiply 2 numbers")
    def test_01(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(Common_Ops.get_data("num1"),
                                                                        Common_Ops.get_data("op1"),
                                                                        Common_Ops.get_data("num2")),
                                                                        Common_Ops.get_data("calculteResult1"))

    @allure.title("verify divide numbers")
    @allure.description("This test verify the result of divide 2 numbers")
    def test_02(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(Common_Ops.get_data("num3"),
                                                                        Common_Ops.get_data("op2"),
                                                                        Common_Ops.get_data("num4")),
                                                                        Common_Ops.get_data("calculteResult2"))

    @allure.title("verify addition numbers")
    @allure.description("This test verify the result of addition 2 numbers")
    def test_03(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(Common_Ops.get_data("num5"),
                                                                        Common_Ops.get_data("op3"),
                                                                        Common_Ops.get_data("num6")),
                                                                        Common_Ops.get_data("calculteResult3"))

    @allure.title("verify subtraction numbers")
    @allure.description("This test verify the result of subtraction 2 numbers")
    def test_04(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(Common_Ops.get_data("num7"),
                                                                        Common_Ops.get_data("op4"),
                                                                        Common_Ops.get_data("num8")),
                                                                        Common_Ops.get_data("calculteResult4"))
