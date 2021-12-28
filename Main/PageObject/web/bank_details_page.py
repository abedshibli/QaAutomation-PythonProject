from selenium.webdriver.common.by import By


class Bank_Details_Page:

    def __init__(self, driver):
        self.driver = driver

    def get_bank_name(self):
        return self.driver.find_element(By.XPATH, "//p")
