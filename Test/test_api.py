import time

import allure
import pytest
from Main.Extensions.api_actions import API_ACTIONS
from Main.Extensions.verfications import Verifications


@pytest.mark.usefixtures('init_api')
class Test_API_Requests:

    @allure.title("verify if the post action success")
    @allure.description("This test verify if the post action success")
    def test_01(self):
        Verifications.verify_equals(API_ACTIONS.post(5, 1, "java hackathon", 23), 201)

    @allure.title("verify if the put action success")
    @allure.description("This test verify if the put action success")
    def test_02(self):
        API_ACTIONS.post(7, 12, "java hackathon", 3)
        Verifications.verify_equals(API_ACTIONS.put(7, 12, "python hackathon", 5), 200)

    @allure.title("verify if the delete action success")
    @allure.description("This test verify if the delete action success")
    def test_03(self):
        Verifications.verify_equals(API_ACTIONS.delete(5), 200)
