from playwright.sync_api import Page

class Container:
    def __init__(self, page: Page):
        self.page = page

        self.product_name = page.locator("[data-test=\"product-name\"]")