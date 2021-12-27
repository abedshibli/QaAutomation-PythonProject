class Mobile_Actions:

    @staticmethod
    def click_action(elem):
        elem.click()

    @staticmethod
    def get_text(elem):
        return elem.text

    @staticmethod
    def insert_value(value, elem):
        elem.send_keys(value)