from __future__ import annotations

import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

import requests

from .scraper import scrape_catalog, save_csv, save_xlsx


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scrape the Books to Scrape practice catalog.")
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--pages", type=int, default=3, help="Number of catalog pages to scrape (default: 3).")
    scope.add_argument("--all", action="store_true", help="Follow pagination until the catalog ends.")
    parser.add_argument("--delay", type=float, default=0.8, help="Seconds between requests (default: 0.8).")
    parser.add_argument("--output-dir", default="data/output", help="Directory for CSV/XLSX output.")
    parser.add_argument("--no-xlsx", action="store_true", help="Only write CSV output.")
    parser.add_argument("--max-details", type=int, default=None, help="Optional cap on detail-page requests.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    pages = None if args.all else args.pages
    if pages is not None and pages < 1:
        raise SystemExit("--pages must be at least 1")
    if args.delay < 0:
        raise SystemExit("--delay must be >= 0")

    try:
        books = scrape_catalog(pages=pages, delay=args.delay, max_detail_pages=args.max_details)
    except (requests.RequestException, ValueError) as exc:
        raise SystemExit(f"Scrape failed: {exc}") from exc
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir)

    csv_path = save_csv(books, output_dir / f"books_{stamp}.csv")
    print(f"Saved {len(books)} records to {csv_path}")

    if not args.no_xlsx:
        xlsx_path = save_xlsx(books, output_dir / f"books_{stamp}.xlsx")
        print(f"Saved {len(books)} records to {xlsx_path}")


if __name__ == "__main__":
    main()
