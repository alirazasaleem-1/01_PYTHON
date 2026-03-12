# Setup variables to chagne after without worrying about order
# Example 1: Basic Usage
def greet(name, age):
    print(f"Hello {name}, You are {age} years old.")

greet(age = 18, name = "Ali") # we can define age before and name later using keyword parameter
# Example 2: Mixing Types
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(name = "Buddy", animal = "Golden Retriever")
# Example 3: Default Values
def make_coffee(size, sugar = 1):
    print(f"Making a {size} coffee with {sugar} sugar(s).")

make_coffee(size = "Large")