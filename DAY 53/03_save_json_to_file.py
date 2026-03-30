import json

data = {"task": "Study Python", "status": "Pending"}

with open("tasks.json", 'w') as file:
    json.dump(data, file)
    print("✅ Json saved as file Successfully. ")