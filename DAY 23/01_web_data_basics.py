import requests

url = "https://api.adviceslip.com/advice"
response = requests.get(url)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    advice = data['slip']['advice']

    print("-" * 30)
    print("Ali! Here is Your Advice\n")
    print(f"{advice}")
    print("-" * 30)
else:
    print("Oops! Something Went Wrong in the connection.")