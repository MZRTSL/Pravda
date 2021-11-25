"""Comparison new columns tittles and tittles in them articles"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants.start_page import StartPageConstants
from constants.article_page import ArticlesConstants
from helpers.base import BaseHelper


class TestPravda (BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (r'C:\Users\Helen\PycharmProjects\Pravda\drivers\chromedriver.exe')
        driver.implicitly_wait (5)
        yield driver
        driver.close ()

    def test_compare_texts(self, driver):
        """
        - Open URL https://www.pravda.com.ua/;
        - Accept cookies;
        - Find column element and tap on it;
        - Find title name and column name and compare them;
        """
        base_helper=BaseHelper (driver)

        # 1. Open start page
        driver.get ("https://www.pravda.com.ua/")
        self.log.info ("Open start page")

        # 2. Accept cookies
        base_helper.wait_and_click (By.XPATH, StartPageConstants.COOKIES_BUTTON_XPATH)
        self.log.info ("Accept cookies")

        # 3. Find columns element text and click
        base_helper.wait_and_click (By.XPATH, StartPageConstants.COLUMN_ELEMENT_XPATH)
        self.log.info ("Find article in news columns")

        # 4. Compare both texts
        tittle_name=base_helper.wait_until_element_find (By.XPATH, ArticlesConstants.TITTLE_NAME_XPATH)
        column_tittle=base_helper.wait_until_element_find (By.XPATH, StartPageConstants.COLUMN_ELEMENT_XPATH)
        assert tittle_name.text == column_tittle.text
        self.log.info ("Find and compare both title`s texts")

        driver.back ()
