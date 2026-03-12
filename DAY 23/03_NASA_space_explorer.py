import requests
import time
import webbrowser

new_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1"
response = requests.get(new_url)

if response.status_code == 200:
    data = response.json()[0]
    title = data.get('title')
    explanation = data.get('explanation')
    image_url = data.get('url')
    print(f"🌎 TODAY'S SPACE DISCOVERY: {title}")
    print(f"=" * 40)

    time.sleep(2)

    print(f"📖 Explanation: {explanation}")
    print("=" * 40)
    webbrowser.open(image_url)
else:
    print("There was a problem while Connecting")