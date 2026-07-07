import pytest
from pages.header import Header
from playwright.sync_api import Page, expect

#Main Page Header display
def test_mainpage_header_display(page: Page) -> None:
    header = Header(page)
    # open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    # check logo displaying and click logo
    header.is_loaded()
    page.screenshot(path="page_after_goto.png")
    header.click_logo()
    expect(page).to_have_url("https://practicesoftwaretesting.com/")
    # check Home link displaying and click Home
    header.is_loaded()
    page.screenshot(path="page_after_goto2.png")
    expect(header.home_link).to_be_visible()
    header.click_home()
    expect(page).to_have_url("https://practicesoftwaretesting.com/")
    # check all buttons in the header
    header.is_loaded()
    page.screenshot(path="page_after_goto3.png")
    expect(header.categories_dropdown).to_be_visible()
    expect(header.sign_in_link).to_be_visible()
    expect(header.language_link).to_be_visible()
    # check empty cart is not in the header
    expect(header.cart_link).not_to_be_visible()

#Main Page Header - Categories
def test_mainpage_header_categories(page: Page) -> None:
    header = Header(page)
    #open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    #check Categories button
    expect(header.categories_dropdown).to_be_visible()
    header.click_categories()
    #check all categories
    expect(header.hand_tools_link).to_be_visible()
    expect(header.power_tools_link).to_be_visible()
    expect(header.other_tools_link).to_be_visible()
    expect(header.special_tools_link).to_be_visible()
    expect(header.rentals_tools_link).to_be_visible()
    #click to category
    header.click_rentals_tools_link()
    expect(page).to_have_url("https://practicesoftwaretesting.com/rentals")
    expect(page.locator("[data-test=\"page-title\"]")).to_contain_text("Rentals")

#Main Page Header  - Contact
def test_mainpage_header_contact(page: Page) -> None:
    header = Header(page)
    # open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    # check Contact displaying
    expect(header.contact_link).to_be_visible()
    header.click_contact()
    # check Contact page opens
    expect(page).to_have_url("https://practicesoftwaretesting.com/contact")
    expect(page.get_by_role("heading", name="Contact")).to_be_visible()

#Main Page Header  - Sign in
def test_mainpage_header_signin(page: Page) -> None:
    header = Header(page)
    # open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    # check Contact displaying
    expect(header.sign_in_link).to_be_visible()
    header.click_sign_in()
    # check Contact page opens
    expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

#Main Page Header  - Cart
def test_mainpage_header_cart(page: Page) -> None:
    header = Header(page)
    # open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    #check empty cart is visible
    expect(header.cart_link).not_to_be_visible()
    #add item to the cart
    page.locator("[data-test=\"product-name\"]").first.click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    expect(header.cart_link).to_be_visible(timeout=10000)
    header.click_home()
    #check non-empty cart is visible (with 1 item in)
    expect(header.cart_link).to_be_visible()
    expect(page.locator("[data-test=\"cart-quantity\"]")).to_contain_text("1")

#Main Page Header  - Language
def test_mainpage_header_language(page: Page) -> None:
    header = Header(page)
    #open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    #check languages button in the header
    expect(header.language_link).to_be_visible()
    header.click_language()
    expect(page.locator("[data-test=\"lang-de\"]")).to_be_visible()
    page.locator("[data-test=\"lang-es\"]").click()
    #check page in ES language
    expect(header.home_link).to_contain_text("Inicio")
    expect(page.locator("#filters")).to_contain_text("Ordenar")