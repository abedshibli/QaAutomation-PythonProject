from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_signin_btn(self):
        return self.driver.find_element(By.XPATH, "//span[@class='MuiButton-label']")

    def get_signup_page(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/signup']")

    def signup_page(self):
        return self.get_signup_page().click()


    def login(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_signin_btn().click()


