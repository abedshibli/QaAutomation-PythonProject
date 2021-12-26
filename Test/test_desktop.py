import pytest
from Main.WorkFlows.desktop_wf import Desktop_WF

@pytest.mark.usefixtures('init_desktop')
class Test_desktop:

    def test_01(self):
        Desktop_WF.two_numbers_to_calculate(3, "*", 2)