# This program takes first and last name from the user and print the full name and print the initials 
first = input("Enter Your First Name: \n")
second = input("Enter Your last Name: \n")
full_name = first + second
initials  = first[0].upper() + second[0].upper()
print(full_name , "\n")
print(initials)
