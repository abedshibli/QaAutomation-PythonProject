from selenium.webdriver.common.by import By


class Search_Page():

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def search_result(self, reslut_text):
        return self.appium_driver.find_element(By.XPATH, "// *[contains(text()," + reslut_text + ")]")

    def go_back_btn(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@content-desc='Navigate up']")

