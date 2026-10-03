# AI Freelance Scraper

A portfolio-ready Python web scraper that extracts a public practice bookstore catalog, follows pagination, visits detail pages, cleans the data, and exports CSV/Excel files.

## What this demonstrates

- HTTP requests with timeouts and retries
- HTML parsing with BeautifulSoup
- CSS selectors
- Pagination by following the site's `next` link
- Detail-page extraction
- Data cleaning and type conversion
- Polite request delays
- Structured logging
- CSV and XLSX exports
- Automated tests without hitting the network
- A clean CLI suitable for client customization

## Safe target

The demo target is `https://books.toscrape.com/`, a fictional bookstore site created for scraping practice. Before adapting this project to a real production website, check that site's terms, robots.txt, access controls, and applicable law.

## Setup

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

Scrape the first 3 pages and save CSV + Excel:

```bash
python -m src.cli --pages 3
```

Scrape the full catalog:

```bash
python -m src.cli --all
```

Choose a custom output directory:

```bash
python -m src.cli --pages 2 --output-dir data/output
```

## Output

The CSV/XLSX contains:

- title
- price_gbp
- availability
- rating
- upc
- stock_count
- category
- product_url
- description

## Project structure

```text
ai_freelance_scraper/
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   └── cli.py
├── tests/
│   └── test_scraper.py
├── data/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Portfolio pitch

> Built a reusable Python scraper that collects paginated product listings and detail-page metadata, handles transient HTTP failures with retries, respects request pacing, validates extracted records, and exports clean CSV/XLSX datasets.

## Important scope note

This project is intentionally built for public practice data. It does not attempt to bypass CAPTCHAs, login controls, paywalls, rate limits, robots restrictions, or other access controls.
