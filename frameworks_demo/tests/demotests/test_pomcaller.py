from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.trialofstonespage import TrialPage

@mark.trialpage
def test_pom_chrome():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                               command_executor=selenium_grid_url)

    trial_page = TrialPage(driver=browser)
    trial_page.go()
    trial_page.stone_input.input_text('rock')
    trial_page.stone_button.click
    trial_page.secrets_input.input_text('bamboo')
    trial_page.secrets_button.click
    trial_page.wealthiest_merchant_input.input_text(trial_page.first_merchant_name_span.text)
    trial_page.merchant_answer_button.click
    trial_page.check_answer_button.click
    check_answer_div_style = trial_page.check_answer_result_div.getattribute("style")

    print('All questions answered on https://techstepacademy.com/trial-of-the-stones, checking to see if Trial Complete banner displayed')
    assert check_answer_div_style == 'display: block;'
    print('If you are seeing this, that means the assertion that the Trial Complete banner is displayed passed.')
    browser.quit()
