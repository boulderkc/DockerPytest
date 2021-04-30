from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_techstep_academy_multi_browser():
    selenium_grid_url = 'http://selenium-hub:4444/wd/hub'
    browserChrome = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                                     command_executor=selenium_grid_url)

    try:

        browserChrome.get('https://techstepacademy.com/training-ground')

        input1_locator_css = browserChrome.find_element_by_css_selector('input[id="ipt1"]')
        input2_locator_css = browserChrome.find_element_by_css_selector('input[id="ipt2"]')

        input2_locator_css.send_keys("hey you")

        product1_p_inner_html = browserChrome.find_elements_by_xpath(
            "//div/span/b[text()='Product 1']/../../p")[0].get_attribute('innerHTML')

        input1_locator_css.send_keys(product1_p_inner_html)

        print("hi i am browser: " + browserChrome.name)

        print(
            "I have entered 'hey you' in the second input box. Now I will assert that the value of that text box "
            "is 'hey you'")

        assert input2_locator_css.get_attribute(
            "value") == "hey you", "input2_locator_css text was not expected 'hey you'"

        print("this is a print statement after the 'hey you' successful assertion")

        print("Next I will assert that the value of that text box is 'hey you2', which should fail.")

        assert input2_locator_css.get_attribute("value") == "hey you2", "input2_locator_css text was not expected " \
                                                                        "'hey you2' "

        print("this is a print statement after the 'hey you2' failed assertion. You will not see this because "
              "the assertion throws an exception which will end the function.")

    finally:

        print("this is the Finally block where we quit the browser even though an exception was thrown")
        browserChrome.quit()
