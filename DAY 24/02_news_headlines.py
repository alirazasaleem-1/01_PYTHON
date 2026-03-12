# This program gives 5 headlines from news websites
from bs4 import BeautifulSoup
import requests

url = "https://www.pakistantoday.com.pk/category/national/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')
    
    for i, headline in enumerate(headlines[:5], 1):
        clean_text = headline.text.strip()
        print(f"{i}: {clean_text}")

else:
    print("Failed to connect with the News Server.")