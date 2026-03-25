from openpyxl import Workbook 

# Create a workbook
wb = Workbook()

# Select Active Sheet
ws = wb.active

# Add data
data = [
    ["Name", "Age", "City"],
    ["Ali", 18, "Faisalabad"],
    ["Junaid", 19, "Islamabad"],
    ["Jamshaid", 20, "Lahor"],
    ["Naseer", 21, "Karachi"]
]

# Save data
for row in data:
    ws.append(row)

# Save workbook
wb.save("Students.xlsx")

print("Excel File Created successfully")
