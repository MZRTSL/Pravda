import logging

from helpers.base import BaseHelper
from constants.start_page import StartPageConstants

class StartPage(BaseHelper):
    """Store helpers methods related to start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constants=StartPageConstants

    def accept_cookies(self):
        """Helper for accept cookies"""
        self.driver.wait_and_click(self.constants.COOKIES_BUTTON_XPATH)
        self.log.info ("Accept cookies")

    def news_columns(self):
        """Find columns element text and click"""
        self.driver.wait_and_click (self.constants.COLUMN_ELEMENT_XPATH)
        self.log.info ("Find article in news columns")