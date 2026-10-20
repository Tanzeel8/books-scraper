# Books Scraper

A Python web scraper that collects book data from
[Books to Scrape](https://books.toscrape.com/) and saves it to CSV and Excel files.

## Features
- Scrapes all 50 pages (about 1000 books) by following the "next" button
- Extracts title, price, star rating and product URL
- Converts the price text into a numeric value
- Removes duplicate books
- Polite delay between requests
- Optional page limit for quick testing

## Tools used
Python, Requests, BeautifulSoup, lxml, pandas, openpyxl

## How to run
```bash
# 1. Install the libraries
pip install -r requirements.txt

# 2. Run the scraper
python books_scraper.py
```

## Output
The script creates an `output` folder with `books.csv` and `books.xlsx`.
A short sample is included in [`sample_output.csv`](sample_output.csv).

| title | price_text | price | rating | url |
|-------|-----------|-------|--------|-----|
| A Light in the Attic | £51.77 | 51.77 | 3 | https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html |
| Tipping the Velvet | £53.74 | 53.74 | 1 | https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html |

## License
MIT
