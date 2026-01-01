from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_movies_displayed_by_search(application):
    home, header, sidebar = application
    header.search_by_button_search("Avatar")
    home.assert_name_films_match("Avatar")