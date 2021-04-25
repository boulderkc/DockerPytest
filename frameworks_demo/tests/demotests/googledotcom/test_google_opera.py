from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

def test_googleopens_opera():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browserOpera = webdriver.Remote(desired_capabilities=DesiredCapabilities.OPERA.copy(),
                                    command_executor=selenium_grid_url)

    listofBrowsers = [browserOpera]

    for browser in listofBrowsers :
        print("hi i am browser: " + browser.name)
        resp = requests.get("http://www.google.com")
        assert resp.status_code == 200, "google.com failed to return response status 200"

        browser.quit()