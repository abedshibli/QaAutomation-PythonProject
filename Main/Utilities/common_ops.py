import time
import xml.etree.ElementTree as ET
import allure
from applitools.selenium import Eyes
from Test import conftest


eyes = Eyes()


class Common_Ops:


    def get_data(node_name):
        root = ET.parse("C:\Automation\Hackaton python\Hackathon-Python\configuration.xml").getroot()
        return root.find(".//" + node_name).text

    @staticmethod
    def init_eyes():
        eyes.api_key = Common_Ops.get_data("eyesApiKey")

        eyes.open(conftest.driver, "Applitools", "Batch run341")

    @staticmethod
    def close_eyes():
        eyes.close()
        eyes.abort()

    @staticmethod
    def attach_file():
        image = "C:/Automation/Hackaton python/Hackathon-Python/screen-shots/screen.png"  # need to create folder: screen-shot first
        conftest.driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
