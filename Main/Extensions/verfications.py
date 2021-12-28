from Main.Extensions.api_actions import API_ACTIONS
from Main.WorkFlows.desktop_wf import Desktop_WF
from Main.WorkFlows.electron_wf import Electron_WF
from Main.WorkFlows.mobile_wf import Mobile_WF
class verifications:
    #Api verifications
    @staticmethod
    def verify_post_response():
        assert API_ACTIONS.post(3, 12, "java hackathon", 230) == 201
    @staticmethod
    def verify_put_response():
        assert API_ACTIONS.put(3,12,"python hackathon",235) == 200
    @staticmethod
    def verify_delete_response():
        assert API_ACTIONS.delete(3) == 200
    #desktop verifications
    @staticmethod
    def verify_multiplication():
        assert Desktop_WF.two_numbers_to_calculate(3, "*", 2) == 6
    @staticmethod
    def verify_division():
        assert Desktop_WF.two_numbers_to_calculate(9, "/", 3) == 3
    @staticmethod
    def verify_addition():
        assert Desktop_WF.two_numbers_to_calculate(1, "+", 8) == 9
    @staticmethod
    def verify_subtraction():
        assert Desktop_WF.two_numbers_to_calculate(9, "-", 2) == 7
    # electron verifications
    @staticmethod
    def verify_screen_size():
        assert Electron_WF.check_screen_size() == 'Your screen is: 1536px x 864px'
    # mobile verifications
    @staticmethod
    def verify_mobile_app():
        assert Mobile_WF.get_app_title("'TVM Calculator'") == "TVM Calculator"
    @staticmethod
    def verify_mobile_reults():
        assert Mobile_WF.get_result_text() == "30"
