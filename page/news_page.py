import logging

from helpers.base import BaseHelper
from constants.article_page import ArticlesConstants

class NewsPage(BaseHelper):
    """Store helpers methods related to Articles page actions"""

    def __init__(self, driver):
        super ().__init__ (driver)
        self.log=logging.getLogger (__name__)
        self.constants=ArticlesConstants

    def find_and_compare(self):
        """Find tittle name in article and column name by.X method and compare them"""
        tittle_name=self.driver.find_element_by_xpath(self.constants.TITTLE_NAME_XPATH)
        column_tittle=self.driver.find_element_by_xpath(self.constants.COLUMN_ELEMENT_NEWS_XPATH)
        assert tittle_name.text == column_tittle.text
        self.log.info ("Find and compare both title`s texts")
