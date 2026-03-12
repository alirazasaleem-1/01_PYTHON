print("\n------ Next Year Age Finder ------")

try:
    age = int(input("\nEnter Your Age:\t"))
    print(f"\n--- Next Year, You will be {age + 1} years old. ---\n")
except ValueError:
    print("\nInvalid input..!! Please enter numerical value like 18 , not words.\n")
