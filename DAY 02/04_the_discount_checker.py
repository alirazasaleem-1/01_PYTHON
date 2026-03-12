total_bill = input("Enter total bill:\n")
bill = int(total_bill)
if bill > 5000:
    discount = bill * 0.10
    bill = bill - discount
    print("Congratulations: You have got the discount\n")
    print(f"Your bill is {bill}")
else:
    print("You can't get discount\n")
    print(f"You need to pay {bill}")