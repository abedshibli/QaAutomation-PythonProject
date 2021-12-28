from selenium.webdriver.common.by import By


class Notification_Page:

    def __init__(self, driver):
        self.driver = driver

    def get_dismiss_btn(self):
        return self.driver.find_element(By.XPATH, "(//span[@class='MuiButton-label'])[3]")