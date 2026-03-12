# Grocery List Manager
grocery_list = ["Milk", "Bread", "Eggs"]

# Function to show items 
def show_items():
    print("\n--- Grocery List ---")
    if not grocery_list: # This will help when list will be empty
        print("Your list is empty")
    else:
      for index, item in enumerate(grocery_list, start = 1):
        print(f"{index}: {item}")
    print("-------------------------------")

# Function to add items 
def add_items(item):
    grocery_list.append(item.capitalize()) # ''' append is used to add items in a list'''
    print(f"{item} is added")

# Function to remove items 
def remove_items(item):
    item = item.capitalize() # it will capitalize first letter so no mistake can occur regarding case
    if item in grocery_list:
      grocery_list.remove(item) # remove is used to remove items from the list
      print(f"{item} is removed")
    else:
       print(f"{item} not found in the list.") 

# Functon to clear all items 
def clear_items():
   grocery_list.clear() # Clear functioin removes all the items in a list
   print("All items are cleared")

# Testing our Manager 
add_items("apple")
remove_items("milk")
show_items()

# Testing clear function
add_items("mango")
add_items("shake")
clear_items()
show_items() 