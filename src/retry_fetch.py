import asyncio
import logging
from playwright.async_api import Page

from config import DELAY_SECONDS, RETRIES
from fetch_page import fetch_page


logger = logging.getLogger("extractor")

async def retry_fetch(page: Page, url: str) -> bool:
    for attempt in range(1, RETRIES + 1):
        if await fetch_page(page, url):
            logger.info(f"success: {url} | try:{attempt} times")
            return True
        logger.warning(f"Fail! {url} | Retry: {attempt}/{RETRIES}")
        if attempt < RETRIES:
            await asyncio.sleep(DELAY_SECONDS * attempt)

    logger.error(f" Fail! After: {attempt} times")
    return False


if __name__ == "__main__":
    from playwright.async_api import async_playwright

    from logger import setup_logger

    async def demo():
        setup_logger()
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            try:
                page = await browser.new_page()
                url = "https://books.toscrape.com/catalogue/page-1.html"
                result = await retry_fetch(page, url)
                print(f"result: {result}")
            finally:
                await browser.close()

    asyncio.run(demo())