from selenium.webdriver.common.by import By


class Electron_Page:

    def __init__(self, driver):
        self.driver = driver

    def system_info(self):
        return self.driver.find_element(By.ID, "button-app-sys-information")

    def get_screen_info(self):
        return self.driver.find_element(By.XPATH, "//*[@id='screen-info-demo-toggle']")

    def get_demobtn(self):
        return self.driver.find_element(By.XPATH, "//*[@id='screen-info']")

    def get_screen_resloution(self):
        return self.driver.find_element(By.ID, "got-screen-info")