import pytest
from Get_products_names import get_all_product_names
from playwright.sync_api import Page, expect
from pytest_base_url.plugin import base_url
from pytest_playwright.pytest_playwright import new_context
from pages.sorting import Sorting
from pages.container import Container

#Main Page Sorting Alphabet
def test_mainpage_sort_alphabet(page: Page, new_context, base_url) -> None:
    sorting = Sorting(page)
    container = Container(page)

    #collecting all products names
    all_product_names = get_all_product_names(page)
    reference_initial_names = all_product_names[0:9]
    reference_names_asc = sorted(all_product_names)[0:9]
    reference_names_desc = sorted(all_product_names, reverse=True)[0:9]

    #open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    #check Sort option is displayed
    expect(sorting.search_heading).to_be_visible()
    expect(sorting.search_heading).to_contain_text("Sort")
    expect(sorting.abc_sort).to_be_visible()
    expect(sorting.abc_sort).to_contain_text("Name (A - Z)Name (Z - A)Price (High - Low)Price (Low - High)CO₂ Rating (A - E)CO₂ Rating (E - A)")

    #wait till at least 1 item on the page
    expect(container.product_name.first).to_be_visible()

    # check Sorting option itself
    #sorting ASC
    sorting.abc_sort.select_option("name,asc")
    #wait till first item will differ from first initial item
    expect(container.product_name.first).not_to_have_text(
        reference_initial_names[0], timeout=10000
    )
    # collecting ASC items
    item_names_asc = [name.strip() for name in container.product_name.all_inner_texts()]
    #checking ASC sorting is correct
    assert reference_names_asc == item_names_asc, \
        f"A-Z sorting doesn't work! Expected: {reference_names_asc}, actual: {item_names_asc}"

    # sorting DESC
    sorting.abc_sort.select_option("name,desc")
    # wait till first item will differ from first asc item
    expect(container.product_name.first.first).not_to_have_text(
        item_names_asc[0], timeout=10000
    )
    page.screenshot()
    # collecting DESC items
    item_names_desc = [name.strip() for name in container.product_name.all_inner_texts()]
    # checking DESC sorting is correct
    assert reference_names_desc == item_names_desc, \
        f"Z-A sorting doesn't work! Expected: {reference_names_desc}, actual: {item_names_desc}"

#Main Page Sorting Search
@pytest.mark.smoke
def test_mainpage_search_product(page: Page, new_context, base_url) -> None:
    sorting = Sorting(page)
    container = Container(page)
    # open Main Page
    page.goto("https://practicesoftwaretesting.com/")
    # check Sort option is displayed
    expect(sorting.search_query).to_be_visible()
    expect(sorting.search_reset).to_be_visible()
    expect(sorting.search_submit).to_be_visible()
    # enter text in the search field
    sorting.click_search_query()
    sorting.search_query.fill("abc")
    #reset search query
    sorting.click_search_reset()
    #search for existing item
    sorting.click_search_query()
    sorting.search_query.fill("bolt cutters")
    sorting.click_search_submit()
    expect(sorting.search_caption).to_be_visible()
    expect(sorting.search_caption).to_contain_text("Searched for: bolt cutters")
    expect(container.product_name.first.first).to_contain_text(
        "Bolt Cutters")
    # search for non-existing item
    sorting.click_search_query()
    sorting.search_query.fill("ducks")
    sorting.click_search_submit()
    expect(sorting.search_caption).to_be_visible()
    expect(sorting.no_results).to_be_visible()
    expect(sorting.search_caption).to_contain_text("Searched for: ducks")
    expect(sorting.no_results).to_contain_text("There are no products found.")