# Function that takes name , age and returns formatted string + age category


def greet_user(name, age):
    message = f"Hello {name}, Welcome to this program"
    if age >= 18:
        category = "Adult"
    else:
        category = "Minor"
    return message , category

welcome_text , age_group = greet_user("Ali", 18)
print(welcome_text)
print(f"Category: {age_group}")