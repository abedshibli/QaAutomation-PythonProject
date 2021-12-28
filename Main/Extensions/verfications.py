import allure


class Verifications:
    @staticmethod
    @allure.step("verify actual and expected")
    def verify_equals(actual, expected):
        assert actual == expected

