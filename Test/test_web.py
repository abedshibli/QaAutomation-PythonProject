import pytest

from Main.WorkFlows.web_workflows.register_workflow import Register_Workflow

@pytest.mark.usefixtures('init_web')
class Test_web:

    def test_01(self):
        self.driver.get('http://localhost:3000/')
        Register_Workflow.create_new_account("kuku2", "kuku2", "k", "123456")
