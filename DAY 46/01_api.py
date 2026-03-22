# This program get a joke from the website and prints it
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

if response.status_code == 200:
    data = response.json()
    print(f"Setup: {data['setup']}\n")
    print(f"Punchline: {data['punchline']}")
else:
    print("Internet Issue or Server Down.")   