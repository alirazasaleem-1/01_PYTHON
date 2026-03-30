import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "Name": "Ali",
    "Skill": "Python"
}

response = requests.post(url, json=data)

print(response.json())