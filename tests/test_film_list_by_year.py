from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_popular_movies_by_year(application):
    home, header, sidebar = application
    header.search_by_category("Popular")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    sidebar.search_by_start_year("2000")
    sidebar.search_by_end_year("2010")
    home.assert_all_years_in_range(2000, 2010)

def test_trend_tv_shows_by_year(application):
    home, header, sidebar = application
    header.search_by_category("Trend")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    sidebar.search_by_start_year("2015")
    sidebar.search_by_end_year("2020")
    home.assert_all_years_in_range(2015, 2020)