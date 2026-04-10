import requests
from bs4 import BeautifulSoup

url = r"https://en.wikipedia.org/wiki/List_of_Money_Heist_episodes"
response = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_ = "wikitable")
print(len(tables))
print(tables[0].text[:500])