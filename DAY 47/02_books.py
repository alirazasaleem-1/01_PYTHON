# This program print books names
import requests
from bs4 import BeautifulSoup

# Gets url
url = r"https://books.toscrape.com/"
response = requests.get(url)

# Parse html
soup = BeautifulSoup(response.text, "html.parser")

# Gets book titles
books = soup.find_all("h3")

print("--- Ali's Books Titles Scraper ---")

# Print book titles
for i, book in enumerate(books[:5], start=1):
    print(f"{i}. {book.get_text(strip=True)}")