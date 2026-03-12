# This program is for practice of previous program
from bs4 import BeautifulSoup
import requests

url = "https://www.pakistantoday.com.pk/category/national/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('h3')
    for i, new in enumerate(news[:5], 1):
        clean_text = new.text.strip()
        print(f"{i}: {clean_text}")
else:
    print("Failed to Connect with the news server.")
