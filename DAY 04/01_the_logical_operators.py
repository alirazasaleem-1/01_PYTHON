# The Price Comparison
my_budget = 5000
item_price = int(input("Enter the price of item: "))
print(f"Is it Exactly my Budget: " , {my_budget == item_price})
print(f"Can I afford it? : " , {item_price <= my_budget})
print(f"Is it overprices? : " , {item_price > my_budget})
                 