from selenium.webdriver.common.by import By

from constants.article_page import ArticlesConstants
from constants.start_page import StartPageConstants
from helpers.base import BaseHelper

# need to add properties

class StartPage(BaseHelper):
    """Store helpers methods related to start page actions"""

    def accept_cookies(self):
        """Helper for accept cookies"""
        self.driver.wait_and_click(By.XPATH, StartPageConstants.COOKIES_BUTTON_XPATH)
        self.log.info ("Accept cookies")

    def news_columns(self):
        """Find columns element text and click"""
        self.driver.wait_and_click (By.XPATH, StartPageConstants.COLUMN_ELEMENT_XPATH)
        self.log.info ("Find article in news columns")


class NewsPage(BaseHelper):
    """Store helpers methods related to Articles page actions"""

    def find_and_compare(self):
        """Find tittle name in article and column name by.X method and compare them"""
        tittle_name=self.driver.wait_until_element_find (By.XPATH, ArticlesConstants.TITTLE_NAME_XPATH)
        column_tittle=self.driver.wait_until_element_find (By.XPATH, ArticlesConstants.COLUMN_ELEMENT_NEWS_XPATH)
        assert tittle_name.text == column_tittle.text
        self.log.info ("Find and compare both title`s texts")