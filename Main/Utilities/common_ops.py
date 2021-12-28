import xml.etree.ElementTree as ET

class Common_Ops:

    def get_data(node_name):
        root = ET.parse("C:\Automation\Hackaton python\Hackathon-Python\configuration.xml").getroot()
        return root.find(".//"+node_name).text

