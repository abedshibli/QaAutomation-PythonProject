from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='firstName']")

    def get_last_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lastName']")

    def get_username(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_confirm_password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='confirmPassword']")

    def get_signup_btn(self):
        return self.driver.find_element(By.XPATH, "//button")

