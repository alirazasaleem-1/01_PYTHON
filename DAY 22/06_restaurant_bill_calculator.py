#  3 Concepts : 
# default parameters, keyword arguments, returning multiple values
def calculate_bill(food_price, drink_price, tax_rate = 0.05):
    sub_total = food_price + drink_price
    tax_amount = sub_total * tax_rate
    total = sub_total + tax_amount
    return tax_amount, total

# Default Method
actual_tax, total_price = calculate_bill(20,5)
print(f" The tax is {actual_tax:.2f}.\nTotal bill is {total_price:.2f}")

# Keywork Method
actual_tax, total_price = calculate_bill(drink_price = 10, food_price = 50)
print(f" The tax is {actual_tax:.2f}.\nTotal bill is {total_price:.2f}")

# Custom Method
actual_tax, total_price = calculate_bill(100, 20, 0.15)
print(f" The tax is {actual_tax:.2f}.\nTotal bill is {total_price:.2f}")
