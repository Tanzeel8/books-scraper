import os
import time, re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Safari/537.36"}

RATING_MAP = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

# ✅ make sure "output" folder exists
if not os.path.exists("output"):
    os.makedirs("output")

def scrape_books(max_pages=None, delay=0.5):
    url = BASE
    rows, page = [], 1

    while True:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        for card in soup.select("article.product_pod"):
            title = card.h3.a["title"].strip()
            rel = card.h3.a["href"]
            product_url = urljoin(url, rel)
            price = card.select_one(".price_color").get_text(strip=True)  # e.g. "£51.77"
            rating_cls = card.select_one(".star-rating")["class"]
            rating_word = next((c for c in rating_cls if c in RATING_MAP), None)
            rating = RATING_MAP.get(rating_word)

            rows.append({
                "title": title,
                "price_text": price,
                "price": float(re.sub(r"[^\d.]", "", price)),
                "rating": rating,
                "url": product_url
            })

        nxt = soup.select_one("li.next a")
        if not nxt: break
        url = urljoin(url, nxt["href"])
        page += 1
        if max_pages and page > max_pages: break
        time.sleep(delay)  # polite

    return rows

if __name__ == "__main__":
    data = scrape_books(max_pages=None)  # scrape all pages (~1000 books)
    df = pd.DataFrame(data)
    # basic cleaning examples
    df = df.drop_duplicates(subset=["url"]).reset_index(drop=True)
    # save
    df.to_csv("output/books.csv", index=False, encoding="utf-8")
    df.to_excel("output/books.xlsx", index=False)
    
    print(f"✅ Saved {len(df)} rows -> output/books.csv & output/books.xlsx")