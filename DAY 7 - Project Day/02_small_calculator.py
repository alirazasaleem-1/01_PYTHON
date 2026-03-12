def calc(action, n1, n2):
    if action == "add":
        return f"Their Sum is {n1+n2}"
    elif action == "subtract":
        return f"Their difference is {n1-n2}"
    elif action == "multiply":
        return f"Their product is {n1*n2}"
    elif action == "divide":
        return f"Their division is {n1/n2}"
    else:
        return "Invalid Action"
    
n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the Second Number: "))
action = input("Enter the action: ")
print(calc(action, n1, n2)) 
    