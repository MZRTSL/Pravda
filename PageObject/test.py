from PageObject.page_objects import StartPage, NewsPage


def test_ukr_pravda(start_page):
    StartPage(start_page).accept_cookies()
    StartPage(start_page).news_columns()
    NewsPage(start_page).find_and_compare()