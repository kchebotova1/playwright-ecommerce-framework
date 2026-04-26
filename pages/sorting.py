from playwright.sync_api import Page

class Sorting:
    def __init__(self, page: Page):
        self.page = page

        self.search_heading = page.get_by_role("heading", name="Sort")
        self.abc_sort = page.locator("[data-test=\"sort\"]")

        #Search
        self.search_query = page.locator("[data-test=\"search-query\"]")
        self.search_reset = page.locator("[data-test=\"search-reset\"]")
        self.search_submit = page.locator("[data-test=\"search-submit\"]")

        # Search results
        self.search_caption = page.locator("[data-test=\"search-caption\"]")
        self.no_results = page.locator("[data-test=\"no-results\"]")


    # Clicking sorting
    def click_search_query(self) -> None:
        # Click on search_query
        self.search_query.click()

    def click_search_reset(self) -> None:
        # Click on search_reset
        self.search_reset.click()

    def click_search_submit(self) -> None:
        # Click on search_submit
        self.search_submit.click()