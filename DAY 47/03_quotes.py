# This program scrapes quotes from quotes to scrape website
import requests
from bs4 import BeautifulSoup

# Gets url
url = r"https://quotes.toscrape.com/"
response = requests.get(url)

# Parse html
soup = BeautifulSoup(response.text, "html.parser")

# Gets quotes
quotes = soup.find_all("span", class_ = "text")

# Prints Quotes
print("--- Ali's Quotes Scraper ---")

for i, quote in enumerate(quotes, start=1):
    print(f"{i}. {quote.get_text()}")