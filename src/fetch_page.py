from playwright.async_api import Page
from playwright.async_api import Error as playwrightError



async def fetch_page(page: Page, url: str, timeout_ms: int = 15000) -> bool:
    try:
        await page.goto(url, timeout= timeout_ms)
        await page.wait_for_selector("article.product_pod", timeout=timeout_ms)
        return True
    except playwrightError:
        return False



if __name__ == "__main__":
    import asyncio
    from playwright.async_api import async_playwright

    async def demo():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            try:
                page = await browser.new_page()
                url = "https://books.toscrape.com/catalogue/page-1.html"
                result = await fetch_page(page, url)
                if result:
                    print(f"Successful! {result}")
                else:
                    print(f"Try again {result}")
            finally:
                await browser.close()

    asyncio.run(demo())
