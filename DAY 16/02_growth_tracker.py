# Growth Tracker
def growth_tracker():
    file_name = "daily_growth.txt"

with open("file_name.txt", "a") as file:
    new_item = input("What did you achieve for your growth today: ")
    file.write("-" + new_item + "\n")
    print("\nItem added successfully..!!\n")

print("\n------ Your progress So Far ------\n")
try:
  with open("file_name.txt", "r") as file:
     print(file.read())
except FileNotFoundError:
   print("Your list is currently empty.")

