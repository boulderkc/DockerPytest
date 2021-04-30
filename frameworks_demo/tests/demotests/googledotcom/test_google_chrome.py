from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

def test_googleopens_chrome():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browserChrome = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy(), command_executor=selenium_grid_url)


    try:

        print("hi i am browser: " + browserChrome.name)
        resp = requests.get("http://www.google.com")
        assert resp.status_code == 200, "google.com failed to return response status 200"

    finally:

        browserChrome.quit()
