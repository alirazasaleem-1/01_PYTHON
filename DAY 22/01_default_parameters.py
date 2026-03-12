# default paramters are used in case the user didn't give input, they can also run in that case
# Examples
# 1: The Classic Greeting
def welcome(name = "Guest"):
    print(f"\nWelcome to Our Home , {name}")

welcome("Ali")
welcome() 

# 2: Simple Calculation
def add(a, b=10):
    return a + b

print(add(5,4))
print(add(5)) # uses default value of b

# 3: Online Order Status
def status(item, carrier = "Standard Shipping"):
    print(f"Shipping {item} via {carrier}")

status("Books")