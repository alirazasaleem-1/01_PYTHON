prices = [ 20, 30, 40, 60, 80, 90, 99, 110]
discounted_prices = []
for p in prices:
    if p >= 80:
        discounted_prices.append(p - 30)
    else:
        discounted_prices.append(p)

print(discounted_prices)
