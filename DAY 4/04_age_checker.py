# Tell user if he/she is adul/child/teenager
age = int(input("Enter Your Age: "))

if age >= 20:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
elif age > 0:
    print("You are a child")
else : 
    print("Invalid Age Entered")