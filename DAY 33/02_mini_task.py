# Taske: Create a dict of 2 friends - each has age + city - print formatted info

friends = {
    "Jack" : {
        "age" : 20 ,
        "city" : "New York",
        "skill" : "Python"
    },
    "James" : {
        "age" : 21 ,
        "city" : "Islamabad",
        "skill" : "Gaming" 
    }
}

for name, info in friends.items():
    print(name, "is", info["age"], "years old living in", info["city"], "learning", info["skill"])