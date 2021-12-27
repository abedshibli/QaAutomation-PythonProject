from selenium.webdriver.common.by import By


class TMV_Page():

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def go_back_btn(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@content-desc='Navigate up']")