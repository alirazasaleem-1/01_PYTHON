# Joke generator using API
import requests
import time

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    setup = data['setup']
    punchline = data['punchline']
    
    print(f"\n❓ {setup}")

    time.sleep(2)

    print(f"💡 {punchline}")
    print(f"\n😂 Success Code: 200. Humour Successful")
else:
    print("Oops! The comedian is on a Break. ( Connection Error )")