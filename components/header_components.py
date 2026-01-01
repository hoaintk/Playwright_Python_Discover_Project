from core.base_page import BasePage
from playwright.sync_api import expect
import time

class HeaderComponents(BasePage):
    LINK_FILTER_OPTION = "//a[text()='{filter_option}']"
    BUTTON_SEARCH = "//input[@name ='search']"


    def search_by_category(self, filter_option):
        self._click(self.LINK_FILTER_OPTION.format(filter_option=filter_option))

    def search_by_button_search(self, text):
        self._fill(self.BUTTON_SEARCH, text)
        self.page.keyboard.press("Enter")
        time.sleep(2) 