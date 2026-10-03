from pathlib import Path

from src.scraper import parse_detail_page, parse_listing_page, parse_price, parse_rating


FIXTURE_DIR = Path(__file__).parent / "fixtures"


def test_parse_price():
    assert parse_price("£51.77") == 51.77


def test_parse_rating():
    assert parse_rating(["star-rating", "Four"]) == 4


def test_parse_listing_page():
    html = (FIXTURE_DIR / "listing.html").read_text(encoding="utf-8")
    books, next_url = parse_listing_page(html, "https://example.test/catalogue/page-1.html")
    assert len(books) == 1
    assert books[0].title == "A Test Book"
    assert books[0].price_gbp == 12.34
    assert books[0].rating == 5
    assert books[0].availability == "In stock"
    assert books[0].product_url == "https://example.test/catalogue/a-test-book.html"
    assert next_url == "https://example.test/catalogue/page-2.html"


def test_parse_detail_page():
    html = (FIXTURE_DIR / "detail.html").read_text(encoding="utf-8")
    book_html = (FIXTURE_DIR / "listing.html").read_text(encoding="utf-8")
    books, _ = parse_listing_page(book_html, "https://example.test/catalogue/page-1.html")
    result = parse_detail_page(books[0], html)
    assert result.upc == "1234567890"
    assert result.category == "Books"
    assert result.stock_count == 7
    assert "test description" in result.description
