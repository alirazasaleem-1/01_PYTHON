item = {
    "name": "Laptop",
    "stock": 10,
    "price": 50000
}

print(f"We have {item['stock']} {item['name']}s in our shop")  # print dictionary itme
item["price"] = 55000 # modify item in dictionary
item["brand"] = "dell" # add item in dictionary
del item["stock"] # delete item from dictionary
print(f"Updated item: {item}") 