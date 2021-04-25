from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class TrainingGroundPage(BasePage):
    url = 'https://techstepacademy.com/training-ground'

    @property
    def input1(self):
        locator = Locator(by=By.ID, value='ipt1')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select1(self):
        locator = (By.ID, 'sel1')
        return BaseElement(driver=self.driver, locator=locator)
