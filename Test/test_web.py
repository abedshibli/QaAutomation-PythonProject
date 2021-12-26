import pytest

from Main.WorkFlows.web_wf import Web_WF

@pytest.mark.usefixtures('init_web')
class Test_web:

    def test_01(self):
        self.driver.get('http://localhost:3000/')
        Web_WF.create_new_account("kuku2", "kuku2", "k", "123456")
