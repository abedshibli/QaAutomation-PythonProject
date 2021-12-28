import allure
import pytest

from Main.Extensions.verfications import Verifications
from Main.WorkFlows.electron_wf import Electron_WF


@pytest.mark.usefixtures('init_electron')
class Test_electron:

    @allure.title("verify the resolution")
    @allure.description("This test verify the size of the screen")
    def test01_verify_screen_resloution(self):
        Verifications.verify_equals(Electron_WF.check_screen_size(), 'Your screen is: 1536px x 864px')
