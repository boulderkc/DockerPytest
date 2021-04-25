from selenium import webdriver
from pytest import fixture
# from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@fixture(scope="function")
def chrome_browser():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                               command_executor=selenium_grid_url)
    return browser
