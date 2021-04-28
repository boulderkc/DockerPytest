from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = Wait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    @property
    def click(self):
        element = Wait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    @property
    def getinputtext(self):
        text = self.web_element.get_attribute('value')
        return text

    def chooseoption(self, index):
        Select(self.web_element).select_by_index(index)
        return None

    def getselectedoptiontext(self):
        text = Select(self.web_element).first_selected_option.text
        return text

    def getattribute(self, attribute_name):
        text = self.web_element.get_attribute(attribute_name)
        return text
