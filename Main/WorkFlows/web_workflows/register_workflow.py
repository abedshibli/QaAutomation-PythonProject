from Main.PageObject.web import register_page
from Main.PageObject.web.register_page import RegisterPage
from Main.Utilities.common_ops import Common_Ops


class Register_Workflow(Common_Ops):

    def create_new_account(self, first_name, last_name, username, password):
        #check
        register_page.get_first_name.send_keys(first_name)
        register_page.send_keys(first_name)
        register_page.get_last_name().send_keys(last_name)
        register_page.get_username().send_keys(username)
        register_page.get_password().send_keys(password)
        register_page.get_confirm_password().send_keys(password)
        register_page.get_signup_btn().click()
