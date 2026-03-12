# Alers when stock is low
import csv
with open("inventory.csv", 'r') as file:
    reader = csv.DictReader(file)

    print("--- Low Stock Report ---")

    for row in reader:
        current_stock = int(row['Quantity'])
        minimum_required = int(row['Threshold'])
        product_name = row['Product']

        if current_stock < minimum_required:
            print(f"Alert! {product_name} is {current_stock} , less than needed {minimum_required}.")