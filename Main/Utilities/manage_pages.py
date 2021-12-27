from Main.PageObject.desktop.calc_page import CalcPage
from Main.PageObject.web.login_page import LoginPage
from Main.PageObject.web.main_page import MainPage
from Main.PageObject.web.new_bank_account_page import Bank_Account_Page
from Main.PageObject.web.register_page import RegisterPage

class Manage_Pages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['register_page'] = RegisterPage(driver)
        globals()['bank_account_page'] = Bank_Account_Page(driver)
        globals()['main_page'] = MainPage(driver)

    @staticmethod
    def init_desktop_page(driver):
        globals()['calc_page'] = CalcPage(driver)
