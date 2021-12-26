from pkgutil import get_data

import pytest
import requests
from account.api.api_v1.endpoints import login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Main.Utilities.common_ops import Common_Ops

#web
driver = None
action = None

login_page = None
main_page = None
new_bank_account_page = None
register_page = None

browser_type = "chrome"

# MOBILE
reportDirectory = 'reports'
reportFormat = 'xml'
dc = {}
testName = 'Untitled'

# API
url = 'https://api.chucknorris.io/jokes/'
header = {'Content-type': 'application/json'}

# ELECTRON
electron_app = "C:\\Automation\\Electrons\\Electron API Demos.exe"
edriver = "C:\\electrondriver.exe"


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = Common_Ops.get_data("browserType")
    if browser_type.lower() == "chrome":
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
    Common_Ops.init_web_pages()

    yield
    driver.quit()


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
def my_desktop_starter(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    globals()['driver'] = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    globals()['driver'].implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


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