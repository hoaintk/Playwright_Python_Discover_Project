from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_popular_movies(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/movies/popular_movies.json")
    header.search_by_category("Popular")
    sidebar.search_by_type("Movie")
    home.assert_films_match(expected, n=3)

def test_trend_movies(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/movies/trend_movies.json")
    header.search_by_category("Trend")
    sidebar.search_by_type("Movie")
    home.assert_films_match(expected, n=3)

def test_newest_movies(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/movies/newest_movies.json")
    header.search_by_category("Newest")
    sidebar.search_by_type("Movie")
    home.assert_films_match(expected, n=3)

def test_top_rated_movies(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/movies/top_rated_movies.json")
    header.search_by_category("Top rated")
    sidebar.search_by_type("Movie")
    home.assert_films_match(expected, n=3)

def test_popular_tvshows(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/tv_shows/popular_tvshows.json")
    header.search_by_category("Popular")
    sidebar.search_by_type("TV Shows")
    home.assert_films_match(expected, n=3)

def test_trend_tvshows(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/tv_shows/trend_tvshows.json")
    header.search_by_category("Trend")
    sidebar.search_by_type("TV Shows")
    home.assert_films_match(expected, n=3)

def test_newest_tvshows(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/tv_shows/newest_tvshows.json")
    header.search_by_category("Newest")
    sidebar.search_by_type("TV Shows")
    home.assert_films_match(expected, n=3)

def test_top_rated_tvshows(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/type/tv_shows/top_rated_tvshows.json")
    header.search_by_category("Top rated")
    sidebar.search_by_type("TV Shows")
    home.assert_films_match(expected, n=3)    