import logging

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class BaseHelper:
    """Store of Base helpers"""

    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait (self.driver, timeout=5)
        self.log=logging.getLogger (__name__)

    def wait_until_element_find(self, locator_type, locator):
        """Wait until element find and return it"""
        self.wait.until (EC.presence_of_element_located ((locator_type, locator)))
        return self.driver.find_element (by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until (EC.element_to_be_clickable ((locator_type, locator)))
        self.driver.find_element (by=locator_type, value=locator).click ()