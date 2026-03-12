password = input("Enter 6 characters password: ")
first_2 = password[:2]
last_2 = password[-2:]
stars = "*" * (len(password) - 4)
print(f"{first_2}{stars}{last_2}")