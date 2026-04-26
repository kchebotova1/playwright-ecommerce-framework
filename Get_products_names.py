from playwright.sync_api import Page, expect

def get_all_product_names(page: Page) -> list:
    base_url = "https://api.practicesoftwaretesting.com/products?"
    all_product_names = []

    #checking how many pages do we have(last_page)
    response_api = page.request.get(
        "https://api.practicesoftwaretesting.com/products?page=1&between=price,1,100&is_rental=false")
    assert response_api.status == 200
    data = response_api.json()
    last_page = data['last_page']

    #taking all names from first page
    all_product_names.extend([item['name'] for item in data['data']])

    #if last_page>1, taking all other names
    if last_page > 1:
        for page_num in range(2, last_page+1):
            resp = page.request.get(f"{base_url}page={page_num}&between=price,1,100")
            assert resp.status == 200
            resp_data = resp.json()
            all_product_names.extend([item['name'] for item in resp_data['data']])

    #doublecheck that all names are in the list
    assert len(all_product_names) == data['total'], \
     f" Expected: {data['total']}, actual: {len(all_product_names)}"

    return all_product_names