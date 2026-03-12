# the mega mall discount
total_bill = int(input("Enter Total Bill Amount: "))
premium = input("Are a Premium Member (Yes/No): ").capitalize().strip()

if total_bill > 10000 and premium == "Yes":
    discount = total_bill * 0.30
    bill = total_bill - discount
elif total_bill > 10000 or premium == "Yes":
    discount = total_bill * 0.15
    bill = total_bill - discount
else :
    print("You can't get any discount. Your bill is " , total_bill)
