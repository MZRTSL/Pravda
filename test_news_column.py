"""Comparison new columns tittles and tittles in them articles"""
from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest

class TestPravda(BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome(r'C:\Users\Helen\PycharmProjects\Pravda\drivers\chromedriver.exe')
        yield driver
        driver.close ()

    def test_compare_texts(self, driver):

        # 1. Open start page
        driver.get ("https://www.pravda.com.ua/")
        self.log.info ("Open start page")

        # 2. Accept cookies
        cookies = driver.find_element_by_xpath('.//*[@id="checkUPcookies"]/div/div/div[2]/div/a/div')
        cookies.click()
        self.log.info ("Accept cookies")

        # 3. Find columns element text and click
        column_element= driver.find_element_by_xpath(".//*[@class='container_sub_news_wrapper']/div['data-vr-contentbox'][1][contains(text(),'')]")
        #[n] - index of serial number (news column)
        column_element.get_attribute(f'{column_element.text}')
        self.log.info("Find in news columns tittle`s name")
        sleep (1)
        print (column_element.text)
        column_element.click()
        sleep (1)

        # 4. In article page find tittle text and tittle text
        tittle_name = driver.find_element_by_xpath(".//h1[@class='post_title']")
        sleep (1)
        tittle_name.get_attribute (f'{tittle_name.text}')
        print (tittle_name.text)
        self.log.info ("Find tittles name in article")
        sleep(1)

        # 5. Compare both texts
        assert column_element.text == tittle_name.text
        self.log.info ("Compare both texts")



