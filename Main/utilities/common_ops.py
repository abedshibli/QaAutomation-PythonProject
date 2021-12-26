import xml.etree.ElementTree as ET

import pytest

from Main.PageObject.web import new_bank_account_page, register_page
from Main.PageObject.web.login_page import LoginPage
from Main.PageObject.web.main_page import MainPage
from Main.PageObject.web.new_bank_account_page import Bank_Account_Page
from Main.PageObject.web.register_page import RegisterPage


#@pytest.fixture(scope='class')
class Common_Ops:
    def get_data(node_name):
        root = ET.parse("./configuration.xml").getroot()
        return root.find(".//"+node_name).text

    # def init_web_pages(self):
    #     my_login_page = LoginPage()
    #     globals()['login_page'] = LoginPage(globals()['driver'])
    #     globals()['register_page'] = RegisterPage(globals()['driver'])
    #     globals()['main_page'] = MainPage(globals()['driver'])
    #     globals()['new_bank_account_page'] = Bank_Account_Page(globals()['driver'])