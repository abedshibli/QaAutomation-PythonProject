from selenium.webdriver.common.by import By


class Financial_Page():

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def get_search_btn(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@id='search']")

    def get_search_input(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@id='search_src_text']")

    def go_search(self):
        return self.appium_driver.find_element(By.XPATH, "//*[@id='search_go_btn']")

    def get_calc_app(self):
        return self.appium_driver.find_element(By.XPATH, "//*[text()='Calculator']")


