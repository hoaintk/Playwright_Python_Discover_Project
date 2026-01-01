# Playwright Python Discover – UI Automation Project

This project is a **UI automation test framework** built with:
- **Playwright (Python)**
- **Pytest**
- **Allure Report**
- **GitHub Actions (CI)**

The target website is a **movie discovery web app (TMDB-style UI)** where users can:
- Browse movies / TV shows
- Filter by category, type, genre, year, rating
- Navigate via pagination

---

## 1. Project Structure

PLAYWRIGHT_PYTHON_DISCOVER
├── .github/
│   └── workflows/
│       └── tests.yml                # CI pipeline (GitHub Actions)
├── components/
│   ├── header_components.py         # Header actions (category filter)
│   ├── sidebar_components.py        # Sidebar filters (type, genre, year, rating)
├── core/
│   └── base_page.py                 # BasePage with common UI actions
├── data/
│   └── movies/
│       ├── popular_movies.json
│       ├── trend_movies.json
│       └── ...
├── mappers/
│   └── film_mapper.py               # Map JSON data → Film model
├── models/
│   └── film.py                      # Film domain object (name, genre, year)
├── pages/
│   └── home_page.py                 # HomePage object (film list & pagination)
├── reports/
│   └── allure-results/              # Allure raw results (ignored in git)
├── tests/
│   ├── test_film_list_by_genre.py
│   ├── test_film_list_by_rating.py
│   ├── test_film_list_by_search.py
│   ├── test_film_list_by_type.py
│   ├── test_film_list_by_year.py
│   └── test_pagination.py
├── venv/                            # Python virtual environment (ignored)
├── conftest.py                      # Pytest fixtures (browser, pages, components)
├── pytest.ini                       # Pytest + Allure configuration
├── .gitignore
└── README.md

## 2. Virtual Environment (macOS)
- Create virtual environment: python3 -m venv venv 
- Activate virtual environment: source venv/bin/activate
- Upgrade pip: pip install --upgrade pip
- Install Playwright browsers: playwright install

## 3. Allure Report Configuration
- Create file pytest.ini
- Install Allure plugin: pip install allure-pytest

## 4. Generate & View Allure Report (Local)
- Run tests and collect Allure results: pytest
- Open full Allure report in local: allure serve ./reports/allure-results
- (If you want to clean allure report, using this command: rm -rf ./reports/allure-results/*)

## 5. CI Configuration (GitHub Actions)
- Detail in file .github/workflows/tests.yml, including:
+ Checkout source code
+ Setup Python
+ Install dependencies
+ Install Playwright browsers
+ Run Pytest with Allure
+ Upload Allure results as artifact

## 6. Synchronization & Waiting Strategy
Because UI has no API hooks, the framework relies on:
- expect(locator).to_be_visible() to ensure element rendered on UI
- Avoid static waits unless debugging
- Wait for UI visibility, not only DOM presence