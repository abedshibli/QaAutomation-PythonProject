import allure
from Main import Utilities
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.desktop_actions import Desktop_Actions


class Desktop_WF:

    @staticmethod
    @allure.step("Perform an arithmetic operation")
    def two_numbers_to_calculate(num1, operator, num2):
        Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_clear_btn())
        Desktop_WF.number_to_webElement(num1)
        Desktop_WF.operators(operator)
        Desktop_WF.number_to_webElement(num2)
        return Desktop_WF.get_calc_result()

    @staticmethod
    @allure.step("number to webElemnt")
    def number_to_webElement(number):
        if number == 0:
            Utilities.manage_pages.calc_page.get_zero().click()
        elif number == 1:
            Utilities.manage_pages.calc_page.get_one().click()
        elif number == 2:
            Utilities.manage_pages.calc_page.get_two().click()
        elif number == 3:
            Utilities.manage_pages.calc_page.get_three().click()
        elif number == 4:
            Utilities.manage_pages.calc_page.get_four().click()
        elif number == 5:
            Utilities.manage_pages.calc_page.get_five().click()
        elif number == 6:
            Utilities.manage_pages.calc_page.get_six().click()
        elif number == 7:
            Utilities.manage_pages.calc_page.get_seven().click()
        elif number == 8:
            Utilities.manage_pages.calc_page.get_eight().click()
        elif number == 9:
            Utilities.manage_pages.calc_page.get_nine().click()
        else:
            raise ValueError('"Unexpected value')

    @staticmethod
    @allure.step("operator to webElemnt")
    def operators(operator):
        if operator == '+':
            Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_plus())
        elif operator == '-':
            Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_minus())
        elif operator == '*':
            Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_multiply())
        elif operator == '/':
            Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_divide())
        else:
            raise ValueError('"Unexpected value')

    @staticmethod
    @allure.step("get result")
    def get_calc_result():
        Desktop_Actions.click_action(Utilities.manage_pages.calc_page.get_equal())
        return int(Utilities.manage_pages.calc_page.get_result().text[10:])

