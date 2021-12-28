import time

import allure
import pytest
from Main.Extensions.api_actions import API_ACTIONS
from Main.Extensions.verfications import Verifications
from Main.Utilities.common_ops import Common_Ops


@pytest.mark.usefixtures('init_api')
class Test_API_Requests:

    @allure.title("verify if the post action success")
    @allure.description("This test verify if the post action success")
    def test_01(self):
        Verifications.verify_equals(API_ACTIONS.post(Common_Ops.get_data("userId1"),
                                                     Common_Ops.get_data("id1"),
                                                     Common_Ops.get_data("title1"),
                                                     Common_Ops.get_data("body1")),
                                                     Common_Ops.get_data("status1"))

    @allure.title("verify if the put action success")
    @allure.description("This test verify if the put action success")
    def test_02(self):
        API_ACTIONS.post(Common_Ops.get_data("userId2"),
                         Common_Ops.get_data("id2"),
                         Common_Ops.get_data("title2"),
                         Common_Ops.get_data("body2"))
        Verifications.verify_equals(API_ACTIONS.put(Common_Ops.get_data("userId2"),
                         Common_Ops.get_data("id2"),
                         Common_Ops.get_data("title3"),
                         Common_Ops.get_data("body2")), Common_Ops.get_data("status2"))

    @allure.title("verify if the delete action success")
    @allure.description("This test verify if the delete action success")
    def test_03(self):
        Verifications.verify_equals(API_ACTIONS.delete(5),  Common_Ops.get_data("status3"))
