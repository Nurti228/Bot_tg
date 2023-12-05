from parsel import Selector
import httpx
from db.queries import parser_db, init_db, create_tables

MAIN_URL = "https://www.house.kg/snyat"


def get_html(url):
    response = httpx.get(url)
    # print(response.text[:1000])
    print(response.status_code)
    return response.text


def get_all_catalog_items(selector: Selector):
    items = selector.css(".listings-wrapper div.main-wrapper")
    return items


def clean_text(text):
    if text is None:
        return ''
    result = text.strip().replace("\n", "").replace("\t", "")
    result = ' '.join(result.split())
    if result and result[-1] == ",":
        result = result[:-1]
    return result


def main():
    html = get_html(MAIN_URL)
    selector = Selector(text=html)
    items = get_all_catalog_items(selector)
    for item in items:
        flat_type = clean_text(item.css(".title::text").get())
        address = clean_text(item.css(".address::text").get())
        price = clean_text(item.css(".price::text").get())
        parser_db({"flat_type": flat_type, "address": address, "price": price})
        print(item)


if __name__ == "__main__":
    init_db()
    create_tables()
    main()
