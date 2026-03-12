# A nested dictionary means a dictionary inside another dictionary

# Example Use-case : Think of it like - main dictionary - firends - inside each friends - details (age, city)

friends = {
    "Ali" : {
        "age" : 18 ,
        "city" : "Faisalabad" 
    },
    "Junaid" : {
        "age" : 23,
        "city": "Lahore"

    }
}

print(friends)

# Accessing Nested Values
print(friends["Ali"]["age"])
print(friends["Junaid"]["city"])

# Modifying Nested Values
friends["Ali"]["age"] = 23
friends["Junaid"]["city"] = "Islamabad"
print(friends)

# looping through nested dictionaries
for name, info in friends.items():
    print(f"Name is {name} and information is {info}")