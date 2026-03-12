# DICTIONARY
ages = {
    "Ali": 16,
    "Junaid": 21,
    "Jamshaid": 25
}

# MODIFYING USING LOOP
for name, age in ages.items():
    if age < 18:    # gives +1 birthday bost to all younger than 18
        ages[name] = age + 1

# ITEMS IS USED TO TAKE BOTH KEYS AND VALUES
for name, age in ages.items():
    print(f"{name} is {age} years old")

# KEYS IS USED TO TAKE ONLY KEYS
for name in ages.keys():
    print(f"The name is {name}")

# VALUES IS USED TO TAKE ONLY VALUES
for age in ages.values():
    print(f"The age is {age}")