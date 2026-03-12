print("\n------ Salary Bonus Finder ------\n")
while True:
    try:
        salary = float(input("Enter Your Salary:\t"))
        bonus = salary * 0.1
        break
    except ValueError:
        print("\nInvalid Input. Try to input Numerical Value instead of words.\n")


final_salary = salary + bonus
print(f"\nYour bonus is {bonus}.\n")
print(f"\nYour final salary including bonus is {final_salary}\n")
    