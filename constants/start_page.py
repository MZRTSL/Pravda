class StartPageConstants:
    COOKIES_BUTTON_XPATH = './/*[@id="checkUPcookies"]/div/div/div[2]/div/a/div'

    """Column element in Start page"""
    # [n] - can add index of serial number (news column)
    COLUMN_ELEMENT_XPATH = ".//*[@class='container_sub_news_wrapper']/div['data-vr-contentbox'][contains(text(),'')]//span"