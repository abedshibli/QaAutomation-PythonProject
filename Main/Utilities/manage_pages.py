from Main.PageObject.web.login_page import LoginPage
from Main.PageObject.web.register_page import RegisterPage

login_page = None
register_page = None

class Manage_Pages:

    @staticmethod
    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['register_page'] = RegisterPage(driver)