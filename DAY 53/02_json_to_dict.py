import json

data = {"Task": "Study Python", "Status": "Pending"}

# Converts dict to json string
json_string = json.dumps(data)
print(type(json_string))

# Converts json string to dict
new_data = json.loads(json_string)
print(type(new_data))