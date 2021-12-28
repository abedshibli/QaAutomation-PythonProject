import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Main.Utilities.common_ops import Common_Ops
from Main.Utilities.manage_pages import Manage_Pages

# web
driver = None

# MOBILE
dc = {}

# API
url_api = 'http://localhost:3000'
resource_api = '/posts/'
id_api = '/101'

# ELECTRON
edriver = None


@pytest.fixture(scope='class')
def init_web():
    browser_type = Common_Ops.get_data("browserType")
    if browser_type.lower() == "chrome":
        driver = init_chrome()
    elif browser_type.lower() == "firefox":
        driver = init_firefox()
    elif browser_type.lower() == "edge":
        driver = init_edge()
    else:
        raise Exception("This browser NOT supported")
    globals()["driver"] = driver
    driver.get(Common_Ops.get_data("url"))
    Manage_Pages.init_web_pages(driver)

    yield

    driver.quit()


@pytest.fixture(scope='class')
def init_mobile():
    dc['udid'] = Common_Ops.get_data("phoneName")
    dc['appPackage'] = Common_Ops.get_data("packageName")
    dc['appActivity'] = Common_Ops.get_data("activityName")
    dc['platformName'] = Common_Ops.get_data("mobileOs")
    driver = webdriver.Remote(Common_Ops.get_data("appiumServer"), dc)

    Manage_Pages.init_mobile_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_api():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url_api)
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop():
    desired_caps = {}
    desired_caps["app"] = Common_Ops.get_data("app")
    desired_caps["platformName"] = Common_Ops.get_data("platformName")
    desired_caps["deviceName"] = Common_Ops.get_data("deviceName")
    driver = webdriver.Remote(Common_Ops.get_data("serverDesktop"), desired_caps)
    driver.implicitly_wait(3)
    Manage_Pages.init_desktop_page(driver)
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_electron():
    options = webdriver.ChromeOptions()
    options.binary_location = Common_Ops.get_data("binaryLocation")
    edriver = Common_Ops.get_data("edriver")
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(5)
    Manage_Pages.init_electron_page(driver)

    yield
    driver.quit()


def init_chrome():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def init_firefox():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


def init_edge():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver
