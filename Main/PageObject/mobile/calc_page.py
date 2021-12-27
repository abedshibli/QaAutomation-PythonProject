from selenium.webdriver.common.by import By


class Calc_Page():

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def get_whatEver(self, number):
        return self.appium_driver.find_element(By.XPATH, "//*[contains(text()," + number + ")]")

    def get_result(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@id='result']")

