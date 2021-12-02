import logging
import random

import pytest

from constants.base import BaseConstants
from selenium import webdriver
from page.start_page import StartPage


def pytest_runtest_setup(item):
    item.cls.log=logging.getLogger (item.name)
    item.cls.variety=random.choice (range (100000, 999999))


class BaseTest:
    log=logging.getLogger (__name__)
    variety=random.choice (range (100000, 999999))


@pytest.fixture (scope='class')
def driver():
    driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
    # driver.implicitly_wait (5)
    yield driver
    driver.close ()

@pytest.fixture (scope='function')
def start_page(driver):
    driver.get (BaseConstants.START_PAGE_URL)
    return StartPage(driver)

# StartPage return - check
