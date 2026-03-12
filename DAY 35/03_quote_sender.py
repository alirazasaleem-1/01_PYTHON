# This program will send a quote to my phone ( it was my idea )
import csv
import random
import requests

quotes = []

with open("quotes.csv", 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        quotes.append(row['Quote'])

my_quote = random.choice(quotes)

topic = "ali_quotes_daily"
url = f"https://ntfy.sh/{topic}"

# Sending the Quote
response = requests.post(url, data = my_quote.encode(encoding='utf-8'))
if response.status_code == 200:
    print(f"Success! Quote Sent: {my_quote}")
else:
    print(f"Failed to send. Error Code: {response.status_code}")