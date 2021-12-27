import time

import pytest
from Main.Extensions.api_actions import API_ACTIONS

@pytest.mark.usefixtures('init_api')
class Test_API_Requests:

    def test_01(self):
        API_ACTIONS.post(5,1,"java hackathon",23)

    def test_02(self):
        API_ACTIONS.post(7,12,"java hackathon",3)
        API_ACTIONS.put(7,12,"python hackathon",5)

    def test_03(self):
        API_ACTIONS.delete(5)