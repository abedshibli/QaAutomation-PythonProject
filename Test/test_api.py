import time

import pytest
from Main.Extensions.api_actions import API_ACTIONS
from Main.Extensions.verfications import Verifications


@pytest.mark.usefixtures('init_api')
class Test_API_Requests:

    def test_01(self):
        Verifications.verify_equals(API_ACTIONS.post(5, 1, "java hackathon", 23), 201)

    def test_02(self):
        API_ACTIONS.post(7, 12, "java hackathon", 3)
        Verifications.verify_equals(API_ACTIONS.put(7, 12, "python hackathon", 5), 200)

    def test_03(self):
        Verifications.verify_equals(API_ACTIONS.delete(5), 200)
