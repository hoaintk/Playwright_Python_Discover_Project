import pytest
from pages.home_page import HomePage
from components.header_components import HeaderComponents
from components.sidebar_components import SideBarComponents

@pytest.fixture
def application(page):
    home = HomePage(page)
    header = HeaderComponents(page)
    sidebar = SideBarComponents(page)

    home.goto()

    return home, header, sidebar
