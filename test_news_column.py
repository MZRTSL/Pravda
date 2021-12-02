"""Comparison new columns tittles and tittles in them articles"""

from conftest import BaseTest
from page.news_page import NewsPage

class TestPravda(BaseTest):

    def test_compare_texts(self, start_page):
        start_page.accept_cookies()
        start_page.news_columns()
        news = NewsPage(start_page.driver)
        news.find_and_compare()
