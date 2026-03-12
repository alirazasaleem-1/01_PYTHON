# This program combines the previous 2 projects and add comments to improve readability
grocery_list = ["Milk", "Bread", "Eggs"]
while True:
    print("\n--- Welcome to Ali's Python Suite ---\n")
    print("1: Grocery List Manager")
    print("2: Number Guessing Game")
    print("3: Exit")

    choice = input("Select an option (1-3)")
    if choice == "1":
        # Grocery List Manager
        # Function to show items
        def show_items():
             print("\n--- Grocery List Items ---\n")
             if not grocery_list:
                 print("Your list is empty.\n") 
             for index, item in enumerate(grocery_list, start = 1):
                 print(f"{index}: {item}")
             print("----------------")
    # Function to add items
        def add_items(item):
             grocery_list.append(item.capitalize())
             print(f"\n{item} is added")

        # Function to Remove items
        def remove_items(item):
             item = item.capitalize()
             if item in grocery_list:
                 grocery_list.remove(item)
                 print(f"\n{item} is removed.\n")
             else:
                 print("Item not found in list. \n")

    # Function to clear items
        def clear_items():
            grocery_list.clear()
            print("Grocery list all items are cleared.\n")
    # Testing our manager
        add_items("Apple")
        add_items("Mango")
        remove_items("Milk")
        show_items()

    # Testing Clear Function
        add_items("Banana")
        clear_items()
        show_items()
    elif choice == "2":
         # Second Project : Number Guessing Game
         # Variables Declaration
         import random
         number = random.randint(1,15)
         guess = 0
         attempts = 0
         # Starter
         print("------ Number Guessing Game ------")
         # Loop and Conditions
         while True:
                 try:
                     guess = int(input("Guess the Number:\t"))
                     attempts += 1
                     if guess > number:
                         print("\nToo High! Guess a Lower Number. \n")
                     elif guess < number:
                         print("\nToo Low! Guess a Higher Number.\n")
                     elif guess == number:
                         print("\nCongratulations! You guess the Correct Number. Here is Your Candy 🍬\n")
                         print(f"You guess the Right Number after {attempts} attempts.\n")
                         break
                 except ValueError:
                         print("\n Please Enter a Numeric value instead of words. \n")

    elif choice == "3":
         print("See You Next Time. Allah Hafiz! 👋")
         break
    else:
         print("Invalid Choice. ")
    