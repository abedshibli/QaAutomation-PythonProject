import pytest

from Main.WorkFlows.electron_wf import Electron_WF

@pytest.mark.usefixtures('init_electron')
class Test_electron:
    def test01_verify_screen_resloution(self):
        assert Electron_WF.check_screen_size() == 'Your screen is: 1536px x 864px'
