from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class TrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

@property
def stone_input(self):
    locator = Locator(by=By.ID, value='r1Input')
    return BaseElement(driver=self.driver, locator=locator)

@property
def stone_button(self):
    locator = Locator(by=By.CSS_SELECTOR, value='button#r1Btn')
    return BaseElement(driver=self.driver, locator=locator)

@property
def secrets_input(self):
    locator = Locator(by=By.ID, value='r2Input')
    return BaseElement(driver=self.driver, locator=locator)

@property
def secrets_button(self):
    locator = Locator(by=By.ID, value='r2Bu')
    return BaseElement(driver=self.driver, locator=locator)

@property
def first_merchant_name_span(self):
    locator = Locator(
        by=By.XPATH, value='.//div/p[text()="3000"]/../span/b')
    return BaseElement(driver=self.driver, locator=locator)

@property
def wealthiest_merchant_input(self):
    locator = Locator(by=By.CSS_SELECTOR, value='input[id="r3Input"]')
    return BaseElement(driver=self.driver, locator=locator)

@property
def merchant_answer_button(self):
    locator = Locator(by=By.CSS_SELECTOR, value='button[id="r3Butn"]')
    return BaseElement(driver=self.driver, locator=locator)

@property
def check_answer_button(self):
    locator = Locator(by=By.CSS_SELECTOR, value='button[id="checkButn"]')
    return BaseElement(driver=self.driver, locator=locator)

@property
def check_answer_result_div(self):
    locator = Locator(by=By.CSS_SELECTOR, value='div[id="trialCompleteBanner"]')
    return BaseElement(driver=self.driver, locator=locator)
