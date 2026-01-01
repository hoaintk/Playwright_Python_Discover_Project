from core.base_page import BasePage
from playwright.sync_api import expect
import time

class SideBarComponents(BasePage):
    TYPE_DEFAULT = "//p[text()='Type']/parent::div//div[text()='Movie']"
    TYPE_FILM = "//div[contains(@class, 'option') and text()='{type_film}']"
    GENRE_DROPDOWN = "//div[text()='Select...']"
    GENRE_FILM = "//div[contains(@class, 'option') and text()='{genre_film}']"
    START_YEAR_DROPDOWN = "//p[text()='Year']/parent::div//following-sibling::div//div[text()='1900']"
    START_YEAR_OPTION = "//div[contains(@class, 'option') and text()='{start_year}']"
    END_YEAR_DROPDOWN = "//p[text()='Year']/parent::div//following-sibling::div//div[text()='2025']"
    END_YEAR_OPTION = "//div[contains(@class, 'option') and text()='{end_year}']"
    RATING = "//ul[@role='radiogroup']//div[@aria-posinset = '{rating_number}']"


    def search_by_type(self, filter_option):
        self._click(self.TYPE_DEFAULT)
        self._click(self.TYPE_FILM.format(type_film=filter_option))


    def search_by_genre(self, filter_option):
        self._click(self.GENRE_DROPDOWN)
        self._click(self.GENRE_FILM.format(genre_film=filter_option))

    def search_by_start_year(self, filter_option):
        self._click(self.START_YEAR_DROPDOWN)
        self._click(self.START_YEAR_OPTION.format(start_year=filter_option))

    def search_by_end_year(self, filter_option):
        self._click(self.END_YEAR_DROPDOWN)
        self._click(self.END_YEAR_OPTION.format(end_year=filter_option))    

    def search_by_rating(self, filter_option):
        self._click(self.RATING.format(rating_number=filter_option))