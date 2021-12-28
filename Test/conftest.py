import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Main.Utilities.common_ops import Common_Ops
from Main.Utilities.manage_pages import Manage_Pages

# web
driver = None
eyes = Eyes()

# MOBILE
dc = {}

# API
url_api = 'http://localhost:3000'
resource_api = '/posts/'
id_api = '/101'

# ELECTRON
edriver = None


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = Common_Ops.get_data("browserType")
    if browser_type.lower() == "chrome":
        request.cls.driver = init_chrome()
    elif browser_type.lower() == "firefox":
        request.cls.driver = init_firefox()
    elif browser_type.lower() == "edge":
        request.cls.driver = init_edge()
    else:
        raise Exception("This browser NOT supported")

    request.cls.driver.get(Common_Ops.get_data("url"))
    Manage_Pages.init_web_pages(request.cls.driver)
    eyes.api_key = '3fnq5ClnQO3SLJ5rWqb93GjNbn0Z5WyU2RjUaC8bMJ0110'
    eyes.open(request.cls.driver, "Applitools", "Batch run 1")

    yield
    eyes.close()
    eyes.abort()
    request.cls.driver.quit()


@pytest.fixture(scope='class')
def init_mobile(request):
    dc['udid'] = 'RF8N21R48PA'
    dc['appPackage'] = 'com.financial.calculator'
    dc['appActivity'] = '.FinancialCalculators'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)
    request.cls.driver = driver
    Manage_Pages.init_mobile_pages(request.cls.driver)

    yield
    request.cls.driver.quit()


@pytest.fixture(scope='class')
def init_api(request):
    request.cls.driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver.get(url_api)
    yield
    request.cls.driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = Common_Ops.get_data("app")
    desired_caps["platformName"] = Common_Ops.get_data("platformName")
    desired_caps["deviceName"] = Common_Ops.get_data("deviceName")
    request.cls.driver = webdriver.Remote(Common_Ops.get_data("serverDesktop"), desired_caps)
    request.cls.driver.implicitly_wait(3)
    Manage_Pages.init_desktop_page(request.cls.driver)
    yield
    request.cls.driver.quit()


@pytest.fixture(scope='class')
def init_electron(request):
    options = webdriver.ChromeOptions()
    options.binary_location = Common_Ops.get_data("binaryLocation")
    edriver = Common_Ops.get_data("edriver")
    request.cls.driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    request.cls.driver.implicitly_wait(5)
    Manage_Pages.init_electron_page(request.cls.driver)

    yield
    request.cls.driver.quit()


def init_chrome():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    return _driver


def init_firefox():
    _driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return _driver


def init_edge():
    _driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return _driver



