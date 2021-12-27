from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_connected_user(self):
        return self.driver.find_element(By.XPATH, "//h6[@data-test='sidenav-username']")

    def get_logout_btn(self):
        return self.driver.find_element(By.XPATH, "(//div[@role='button'])[1]")

    def get_balance(self):
        return self.driver.find_element(By.XPATH, "//h6[@data-test='sidenav-user-balance']")

