from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_by_paging_number(application):
    home, header, sidebar = application
    header.search_by_category("Popular")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    sidebar.search_by_rating("5")
    home.search_by_paging_number("4")
    home.search_by_paging_number("2")
    home.search_by_paging_number("Next")
    home.assert_current_page(3)
    home.search_by_paging_number("Previous")
    home.assert_current_page(2)