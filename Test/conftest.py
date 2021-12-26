import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Main.Utilities.common_ops import Common_Ops

#web
from Main.Utilities.manage_pages import Manage_Pages

driver = None
action = None

browser_type = "chrome"

# MOBILE
reportDirectory = None
reportFormat = None
dc = {}
testName = None

# API
url = None
header = {'Content-type': 'application/json'}

# ELECTRON
electron_app = None
edriver = None


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = Common_Ops.get_data("browserType")
    if browser_type.lower() == "chrome":
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # globals()['driver'] = driver
    # request.cls.driver = driver
        globals()['driver'] = init_chrome()
        request.cls.driver = globals()['driver']
    elif browser_type.lower() == "firefox":
        globals()['driver'] = init_firefox()
        request.cls.driver = globals()['driver']
    elif browser_type.lower() == "edge":
        globals()['driver'] = init_edge()
        request.cls.driver = globals()['driver']
    else:
        raise Exception("This browser NOT supported")

    Manage_Pages.init_web_pages(request.cls.driver)
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

@pytest.fixture(scope='class')
def my_mobile_starter(request):
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = '16af5295'
    dc['appPackage'] = 'com.financial.calculator'
    dc['appActivity'] = '.FinancialCalculators'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4722/wd/hub', dc)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_api_starter(request):
    response = requests.get(url + 'categories')
    request.cls.action = response.json()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    globals()['driver'] = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    request.cls.driver = globals()['driver']
    request.cls.driver.implicitly_wait(3)
    Manage_Pages.init_desktop_page(request.cls.driver)
    yield
    request.cls.driver.quit()


@pytest.fixture(scope='class')
def my_electron_starter(request):
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    globals()['driver'] = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    globals()['driver'].implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()