def smart_calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    else:
        return "Invalid Operation"
    
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
operation = input("Enter the operation (add/sub/mul): ").lower().strip()

print(f"Your result is {smart_calculator(num1, num2, operation)}")