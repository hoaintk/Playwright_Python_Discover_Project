from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents
from mappers.film_mapper import load_films_from_json
from pages.home_page import HomePage

def test_popular_movies_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_action/movies/popular_movies.json")
    header.search_by_category("Popular")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    home.assert_films_match(expected, n=3)

def test_trend_movies_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_action/movies/trend_movies.json")
    header.search_by_category("Trend")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    header.search_by_category("Trend")
    home.assert_films_match(expected, n=3)

def test_newest_movies_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_action/movies/newest_movies.json")
    header.search_by_category("Newest")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    home.assert_films_match(expected, n=3)

def test_top_rated_movies_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_action/movies/top_rated_movies.json")
    header.search_by_category("Top rated")
    sidebar.search_by_type("Movie")
    sidebar.search_by_genre("Action")
    home.assert_films_match(expected, n=3)

def test_popular_tvshows_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_comedy/tv_shows/popular_tvshows.json")
    header.search_by_category("Popular")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    home.assert_films_match(expected, n=3)

def test_trend_tvshows_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_comedy/tv_shows/trend_tvshows.json")
    header.search_by_category("Trend")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    home.assert_films_match(expected, n=3)

def test_newest_tvshows_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_comedy/tv_shows/newest_tvshows.json")
    header.search_by_category("Newest")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    home.assert_films_match(expected, n=3)

def test_top_rated_tvshows_by_genre(application):
    home, header, sidebar = application
    expected = load_films_from_json("data/genre_comedy/tv_shows/top_rated_tvshows.json")
    header.search_by_category("Top rated")
    sidebar.search_by_type("TV Shows")
    sidebar.search_by_genre("Comedy")
    home.assert_films_match(expected, n=3)    