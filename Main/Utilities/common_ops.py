import xml.etree.ElementTree as ET
import allure
from applitools.selenium import Eyes
from Test import conftest
from datetime import datetime
from datetime import datetime



eyes = Eyes()


class Common_Ops:
    print(str(datetime.now()))



    def get_data(node_name):
        root = ET.parse("C:\Automation\Hackaton python\Hackathon-Python\configuration.xml").getroot()
        return root.find(".//" + node_name).text

    @staticmethod
    def init_eyes():
        eyes.api_key = 'wLCwiZvtsfJZ1l4C1w2xEVUaCQqR5ZB8hwW8YECm107fE110'

        eyes.open(conftest.driver, "Applitools", "Batch run3")

    @staticmethod
    def close_eyes():
        eyes.close()
        eyes.abort()

    @staticmethod
    def attach_file():
        image = "C:/Automation/Hackaton python/Hackathon-Python/screen-shots/screen.png"  # need to create folder: screen-shot first
        conftest.driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
