from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_popular_movies_by_rating(application):
    home, header, sidebar = application
    header.search_by_category("Popular")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    sidebar.search_by_rating("5")

def test_trend_tv_shows_by_rating(application):
    home, header, sidebar = application
    header.search_by_category("Trend")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    sidebar.search_by_rating("2")