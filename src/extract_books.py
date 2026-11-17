from playwright.async_api import Page


async def extract_books(page: Page) -> list[dict]:
    books = []
    cards = await page.query_selector_all("article.product_pod")

    for card in cards:
        title_el = await card.query_selector("h3 a")
        price_el = await card.query_selector("p.price_color")
        rating_el = await card.query_selector("p.star-rating")
        stock_el = await card.query_selector("p.availability")


        title = await title_el.get_attribute("title")
        price = await price_el.inner_text()
        rating_class = await rating_el.get_attribute("class")
        stock_text = await stock_el.inner_text()


        books.append(
            {"title": title,
             "price": price,
             "rating": rating_class.split()[-1],
             "in_stock": "In stock" in stock_text,}
        )

    return books


if __name__ == "__main__":
    import asyncio
    from playwright.async_api import Error as error
    from playwright.async_api import async_playwright
    from fetch_page import fetch_page

    async def demo():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            try:
                page = await browser.new_page()
                url = "https://books.toscrape.com/catalogue/page-1.html"
                if await fetch_page(page, url):
                    books = await extract_books(page)
                    print(f"Total books: {len(books)}")
                    print(books[0])
                else:
                    print("Anything wrong!")
            except error as e:
                print(f"Problem: {e}")
            finally:
                await browser.close()

    asyncio.run(demo())
