# This program gets 5 headlines from bbc news website
import requests
from bs4 import BeautifulSoup

# Gets url
url = r"https://www.bbc.com/news"
response = requests.get(url)

# Parse html
soup = BeautifulSoup(response.text, "html.parser")

# Get Headlines
headlines = soup.find_all('h2')

# Intro
print("--- Ali's News Scraper ---")

# Prints frist 5 headlines
for i, headline in enumerate(headlines[:10], start = 1):
    print(f"{i}. {headline.get_text(strip=True)}")