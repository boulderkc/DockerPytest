from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests


def test_microsoft_opens_opera():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browserOpera = webdriver.Remote(desired_capabilities=DesiredCapabilities.OPERA.copy(),
                                    command_executor=selenium_grid_url)

    try:
        print("hi i am browser: " + browserOpera.name)
        resp = requests.get("http://www.microsoft.com")
        assert resp.status_code == 200, "google.com failed to return response status 200"

    finally:

        browserOpera.quit()
