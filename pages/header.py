from playwright.sync_api import Page

class Header:
    def __init__(self, page: Page):
        self.page = page

        #Headers links
        self.logo_link = page.get_by_role("link", name="Practice Software Testing -")
        self.home_link = page.locator("[data-test=\"nav-home\"]")
        self.categories_dropdown = page.locator("[data-test=\"nav-categories\"]")
        self.contact_link = page.locator("[data-test=\"nav-contact\"]")
        self.sign_in_link = page.locator("[data-test=\"nav-sign-in\"]")
        self.language_link = page.locator("[data-test=\"language-select\"]")
        self.cart_link = page.locator("[data-test=\"nav-cart\"]")

        #Categories links
        self.hand_tools_link = page.locator("[data-test=\"nav-hand-tools\"]")
        self.power_tools_link = page.locator("[data-test=\"nav-power-tools\"]")
        self.other_tools_link = page.locator("[data-test=\"nav-other\"]")
        self.special_tools_link = page.locator("[data-test=\"nav-special-tools\"]")
        self.rentals_tools_link = page.locator("[data-test=\"nav-rentals\"]")

    #Clicking main headers links
    def click_logo(self) -> None:
        #Click on logo
        self.logo_link.click()

    def click_home(self) -> None:
        #click on Home btn
        self.home_link.click()

    def click_categories(self) -> None:
        #click on Home btn
        self.categories_dropdown.click()

    def click_contact(self) -> None:
        #click on Home btn
        self.contact_link.click()

    def click_sign_in(self) -> None:
        #click on Home btn
        self.sign_in_link.click()

    def click_language(self) -> None:
        #click on Home btn
        self.language_link.click()

    # Clicking categories links
    def click_rentals_tools_link(self) -> None:
        #click on Home btn
        self.rentals_tools_link.click()