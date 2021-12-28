import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.WorkFlows.desktop_wf import Desktop_WF


@pytest.mark.usefixtures('init_desktop')
class Test_desktop:

    @allure.title("verify multiply numbers")
    @allure.description("This test verify the result of multiply 2 numbers")
    def test_01(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(3, "*", 2), 6)

    @allure.title("verify divide numbers")
    @allure.description("This test verify the result of divide 2 numbers")
    def test_02(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(9, "/", 3), 3)

    @allure.title("verify addition numbers")
    @allure.description("This test verify the result of addition 2 numbers")
    def test_03(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(1, "+", 8), 9)

    @allure.title("verify add numbers")
    @allure.description("This test verify the result of subtraction 2 numbers")
    def test_04(self):
        Verifications.verify_equals(Desktop_WF.two_numbers_to_calculate(9, "-", 2), 7)
