from selenium.webdriver.common.by import By


class Bank_Account_Page:

    def __init__(self, driver):
        self.driver = driver

    def get_next_btn(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Next']")

    def get_bank_name(self):
        return self.driver.find_element(By.ID, "bankaccount-bankName-input")

    def get_routing_number(self):
        return self.driver.find_element(By.ID, "bankaccount-routingNumber-input")

    def get_account_number(self):
        return self.driver.find_element(By.XPATH, "//input[@name='accountNumber']")

    def get_save_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

    def get_done_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary']")

