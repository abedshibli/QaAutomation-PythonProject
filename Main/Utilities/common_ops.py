import xml.etree.ElementTree as ET

class Common_Ops:

    def get_data(node_name):
        root = ET.parse("..\\configuration.xml").getroot()
        return root.find(".//"+node_name).text

