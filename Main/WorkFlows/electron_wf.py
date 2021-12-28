import time

import allure
from Main import Utilities
from Main.Utilities.manage_pages import Manage_Pages
from Main.Extensions.electron_actions import Electron_Actions


class Electron_WF:

    @staticmethod
    @allure.step("check screen resolution")
    def check_screen_size():
        Electron_Actions.click_action(Utilities.manage_pages.electron_page.system_info())
        Electron_Actions.click_action(Utilities.manage_pages.electron_page.get_screen_info())
        Electron_Actions.click_action(Utilities.manage_pages.electron_page.get_screen_info())
        Electron_Actions.click_action(Utilities.manage_pages.electron_page.get_demobtn())
        time.sleep(2)
        return Electron_Actions.get_text(Utilities.manage_pages.electron_page.get_screen_resloution())


