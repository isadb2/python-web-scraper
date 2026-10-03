# Portfolio Description

## Python Web Scraper — Paginated Product Catalog to CSV/XLSX

Built a reusable Python scraper for a public practice bookstore catalog. The tool follows pagination, extracts product listings, visits product detail pages for richer metadata, handles transient HTTP failures with retries, applies request delays, validates parsed values, and exports clean CSV/XLSX files.

### Stack

Python, requests, BeautifulSoup, openpyxl, pytest

### Key features

- Pagination-aware crawling
- Detail-page enrichment
- Price/rating/stock parsing
- Retry + timeout handling
- Polite request pacing
- CSV and Excel export
- Automated parser tests using local fixtures

### Result

A client-ready foundation that can be adapted to other permitted public catalog/data-extraction projects by changing selectors and field mappings.
