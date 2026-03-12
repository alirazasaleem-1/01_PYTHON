total_bill = input("Enter the total bill:\n")
no_of_people = input("Enter the number of People:\n")
bill = int(total_bill)
people = int(no_of_people)

tip = bill * 0.15
actual_bill = tip + bill
individual_bill = actual_bill / people
print(f"Each person needs to pay {round(individual_bill)} PKR")