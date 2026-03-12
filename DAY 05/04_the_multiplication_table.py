# Asks the number and then print the table of that number

num = int(input("Enter the Number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")