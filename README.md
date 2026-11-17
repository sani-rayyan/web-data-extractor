# Website Data Extractor

An async, ethical web scraper built with Python and Playwright. It collects book data (title, price, rating, stock status) from a public practice site and saves it to CSV and JSON.

## Features

- Checks `robots.txt` before scraping
- Retries failed pages with increasing delay
- Waits between requests to avoid overloading the site
- Logs every step to a file
- Saves results in CSV and JSON

## Tech Stack

Python, Playwright (async), asyncio

## Project Structure

```
web-data-extractor/
├── main.py
├── requirements.txt
└── src/
    ├── config.py
    ├── logger.py
    ├── robots_checker.py
    ├── fetch_page.py
    ├── retry_fetch.py
    ├── extract_books.py
    ├── save_csv.py
    └── save_json.py
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

(On Mac/Linux, activate with `source .venv/bin/activate`.)

## Usage

```bash
python main.py
```

Settings such as the number of pages and delay are in `src/config.py`.

## Output

- `output/books.csv`
- `output/books.json`
- `logs/scraper.log`

## Sample Result

```json
{
  "title": "A Light in the Attic",
  "price": "£51.77",
  "rating": "Three",
  "in_stock": true
}
```

## Ethical Scraping

This project scrapes [books.toscrape.com](https://books.toscrape.com), a sandbox site made for practice. It respects `robots.txt` and uses delays between requests.