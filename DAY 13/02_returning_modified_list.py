def apply_discount(prices_list):
    new_prices = []
    for price in prices_list:
        new_prices.append(price * 0.9) # Applies Discount
    return new_prices

original_prices = [100, 200, 300, 400]
sale_prices = apply_discount(original_prices)
print(sale_prices)