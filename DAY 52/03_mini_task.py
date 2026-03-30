# Task: Send your name to API, get reponse, print formatted output
import requests

name = input("Enter Your Name: ")
url = f"https://api.agify.io?name={name}"

response = requests.get(url)
data = response.json()

print("\n--- Result ---\n")
print(f"Name: {data['name']}")
print(f"Predicted Age: {data['age']}")
print(f"Count: {data['count']}")