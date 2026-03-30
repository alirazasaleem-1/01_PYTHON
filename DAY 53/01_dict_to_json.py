import json

data = {
    "Task": "Study Python",
    "Status": "Pending"
}


json_data = json.dumps(data)
print(json_data)
