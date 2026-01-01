from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        print(f"[Visit] {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def _click(self, locator: str):
        try:
            print(f"[Click] {locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"[Error] Cannot click on {locator}")
            raise

    def _fill(self, locator: str, text: str):
        print(f"[Fill] '{text}' in {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"[Assert] Check '{text}' to display")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _assert_element_visible(self, locator: str):
        print(f"[Assert] Check element visible")
        expect(self._get_locator(locator)).to_be_visible()