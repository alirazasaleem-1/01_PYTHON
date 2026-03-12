# Email Domain Extractor
import csv

domain = set()

with open("users.csv", 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        email = row['Domain']

        parts = email.split('@')
        domain_name = parts[1]
        domain.add(domain_name)

print("Unique Email Domains found: ")
for d in domain:
    print(f"Domain : {d}")