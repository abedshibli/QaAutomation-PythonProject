from selenium.webdriver.common.by import By

class CalcPage:

    def __init__(self, driver):
        self.driver = driver

    def get_clear_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='clearButton']")

    def get_zero(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num0Button']")

    def get_one(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num1Button']")

    def get_two(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num2Button']")

    def get_three(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num3Button']")

    def get_four(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num4Button']")

    def get_five(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num5Button']")

    def get_six(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num6Button']")

    def get_seven(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num7Button']")

    def get_eight(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num8Button']")

    def get_nine(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='num9Button']")

    def get_plus(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='plusButton']")

    def get_minus(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='minusButton']")

    def get_multiply(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='multiplyButton']")

    def get_divide(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='divideButton']")

    def get_equal(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='equalButton']")

    def get_result(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")




