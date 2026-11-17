import asyncio
import sys

sys.path.append("src")

from playwright.async_api import async_playwright

from config import BASE_URL, DELAY_SECONDS, HEADLESS, MAX_PAGES
from extract_books import extract_books
from logger import setup_logger
from retry_fetch import retry_fetch
from robots_checker import can_scrape
from save_csv import save_csv
from save_json import save_json



async def main():
    logger = setup_logger()
    all_books = []

    first_url = f"{BASE_URL}/catalogue/page-1.html"
    if not can_scrape(first_url):
        logger.error("robots.txt Not Allow!")
        print("robots.txt Not Allow!")
        return

    async with async_playwright()as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        try:
            page = await browser.new_page()

            for number in range(1, MAX_PAGES + 1):
                url = f"{BASE_URL}/catalogue/page-{number}.html"

                if not await retry_fetch(page, url):
                    logger.error(f"Page number:{number} Skipped: {url}")
                    continue
                books = await extract_books(page)
                all_books.extend(books)
                logger.info(f"Page number: {number} | Total books: {len(books)}")
                print(f"Page number: {number} | Total books: {len(books)}")

                await asyncio.sleep(DELAY_SECONDS)

        finally:
            await browser.close()

    save_csv(all_books)
    save_json(all_books)
    print(f"Successfully saved [{len(all_books)} books] (title, price, rating, stock) to CSV and JSON. ")

if __name__ == "__main__":
    asyncio.run(main())