from core.base_page import BasePage
from playwright.sync_api import expect
import time

class HomePage(BasePage):
    URL = "https://tmdb-discover.surge.sh/"
    CARD_LIST = "(//div[@class='flex flex-col items-center'])[1]"
    TEXT_FILMNAME = "(//div[@class='flex flex-col items-center'])[{indexFilm}]//p[1]"
    TEXT_FILMNAME_ALTERNATIVE = "//div[@class='flex flex-col items-center']//p[1]"
    TEXT_GENRE_AND_YEAR = "(//div[@class='flex flex-col items-center'])[{indexFilm}]//p[2]"
    TEXT_GENRE_AND_YEAR_ALTERNATIVE = "//div[@class='flex flex-col items-center']//p[2]"
    PAGING_NUMBER = "//div[@id='react-paginate']//li//a[text()='{page_number}']"
    CURRENT_PAGE_NUMBER = "//a[@aria-label=\"Page {number} is your current page\"]"

    def goto(self):
        self._visit(self.URL)

    def ui_film_name(self, index_film: int) -> str:
        locator = self.page.locator(self.TEXT_FILMNAME.format(indexFilm=index_film))
        return (locator.text_content() or "").strip()

    def ui_genre_year(self, index_film: int) -> tuple[str, int]:
        locator = self.page.locator(self.TEXT_GENRE_AND_YEAR.format(indexFilm=index_film))
        raw = (locator.text_content() or "").strip() 
        parts = [p.strip() for p in raw.split(",")]
        if len(parts) != 2:
            raise AssertionError(f"Genre/Year format unexpected at index {index_film}: '{raw}'")
        genre = parts[0]
        year = int(parts[1])
        return genre, year

    def assert_films_match(self, expected_films, n: int = 3):
        expect(self.page.locator(self.CARD_LIST)).to_be_visible()
        self.page.wait_for_timeout(1000)
        for i in range(1, n + 1):  
            exp = expected_films[i - 1]

            ui_name = self.ui_film_name(i)
            ui_genre, ui_year = self.ui_genre_year(i)

            assert ui_name == exp.name, f"Index {i} name mismatch: UI='{ui_name}' vs JSON='{exp.name}'"
            assert ui_genre == exp.genre, f"Index {i} genre mismatch: UI='{ui_genre}' vs JSON='{exp.genre}'"
            assert ui_year == exp.year, f"Index {i} year mismatch: UI='{ui_year}' vs JSON='{exp.year}'"

    def assert_all_years_in_range(self, start_year: int, end_year: int): 
        self.page.wait_for_timeout(1000)
        count = self.page.locator(self.TEXT_GENRE_AND_YEAR_ALTERNATIVE).count() 
        if count == 0: 
            raise AssertionError("No films found to check year range.") 
        
        for i in range(1, count + 1): 
            _, ui_year = self.ui_genre_year(i) 
            assert start_year <= ui_year <= end_year, ( f"Index {i} year out of range: UI='{ui_year}' " f"Expected between {start_year} and {end_year}" )

    def assert_name_films_match(self, film_name: str):
        self.page.wait_for_timeout(1000)
        count = self.page.locator(self.TEXT_FILMNAME_ALTERNATIVE).count() 
        if count == 0: 
            raise AssertionError("No films found to check name.") 
        
        for i in range(1, count + 1): 
            ui_name = self.ui_film_name(i) 
            assert film_name in ui_name, ( f"Index {i} name mismatch: UI='{ui_name}' " f"Expected to contain '{film_name}'" )

    def search_by_paging_number(self, page_number: str):
        self._click(self.PAGING_NUMBER.format(page_number=page_number))

    def assert_current_page(self, expected_page: int):
        active_page_locator = self.page.locator(self.CURRENT_PAGE_NUMBER.format(number=expected_page))
        expect(active_page_locator).to_have_text(str(expected_page))