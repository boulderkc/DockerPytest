from selenium import webdriver 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.traininggroundspage import TrainingGroundPage
from pages.trialofstonespage import TrialPage

def test_pageobjects_chrome():

    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy(), command_executor=selenium_grid_url)

    trial_page = TrialPage(driver=browser)
    trial_page.go()
    trial_page.stone_input.input_text('rock')
    trial_page.stone_button.click


    # tester_page = TrainingGroundPage(
    #     driver=browser
    # )
    # tester_page.go()
    # tester_page.input1.input_text('texty baby')
    # assert tester_page.input1.getinputtext == 'texty baby', 'faily waily'

    # tester_page.select1.chooseoption(2)
    # print(tester_page.select1.getselectedoptiontext())

    assert True
    browser.quit()
