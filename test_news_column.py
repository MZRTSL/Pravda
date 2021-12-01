"""Comparison new columns tittles and tittles in them articles"""

from conftest import BaseTest
from page.news_page import NewsPage

class TestPravda(BaseTest):

    def test_compare_texts(self, start_page):
        start_page.accept_cookies()
        start_page.news_columns()
        news = NewsPage(start_page.driver)
        news.find_and_compare()

# import pytest
# from selenium import webdriver
#
# from conftest import BaseTest
# from constants.base import BaseConstants
# # from page.start_page import StartPage
# # from conftest import start_page
# # from page.news_page import ArticlesPage
#
# from selenium.webdriver.common.by import By
# from constants.start_page import StartPageConstants
# from constants.article_page import ArticlesConstants
# from helpers.base import BaseHelper
# # from page.news_page import ArticlesPage
#
# class TestPravda(BaseTest):
#
#     @pytest.fixture (scope='class')
#     def driver(self):
#         driver=webdriver.Chrome (BaseConstants.DRIVER_PATH)
#         # driver.implicitly_wait (5)
#         yield driver
#         driver.close ()
#
#     def test_compare_texts(self, driver):
#
#         """
#         - Open URL https://www.pravda.com.ua/;
#         - Accept cookies;
#         - Find column element and tap on it;
#         - Find title name and column name and compare them;
#         """
#         # start_helper = StartPage (driver)
#         # news_helper = ArticlesPage(driver)
#         base_helper=BaseHelper (driver)
#
#         # # 1. Open start page and accept cookies
#         # start_page.accept_cookies()
#         #
#         # # 3. Find columns element text and click
#         # driver.news_columns()
#         #
#         # # 4. Compare both texts
#         # driver.find_and_compare()
#
#         # 1. Open start page
#         driver.get (BaseConstants.START_PAGE_URL)
#         self.log.info ("Open start page")
#
#         # 2. Accept cookies
#         base_helper.wait_and_click (By.XPATH, StartPageConstants.COOKIES_BUTTON_XPATH)
#         self.log.info ("Accept cookies")
#
#         # 3. Find columns element text and click
#         base_helper.wait_and_click (By.XPATH, StartPageConstants.COLUMN_ELEMENT_XPATH)
#         self.log.info ("Find article in news columns")
#
#         # 4. Compare both texts
#         tittle_name=base_helper.wait_until_element_find (By.XPATH, ArticlesConstants.TITTLE_NAME_XPATH)
#         column_tittle=base_helper.wait_until_element_find (By.XPATH, ArticlesConstants.COLUMN_ELEMENT_NEWS_XPATH)
#         assert tittle_name.text == column_tittle.text
#         self.log.info ("Find and compare both title`s texts")
#
#         driver.back ()
