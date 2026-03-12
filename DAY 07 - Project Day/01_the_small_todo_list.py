# Function of Smart to do List
tasks = []
def manage_tasks(action, item): # Function to create to do list
    if action == "add":
        tasks.append(item) # append is used to add items in a list
        return f"{item} is add to the tasks."
    elif action == "remove":
        if item in tasks:
            tasks.remove(item) # remove is used to remove items from list
            return f"{item} is removed from the tasks."
        else:
            return "Item is not in tasks"
    elif action == "view":
        return f"Current Tasks: {tasks}" # it will simply print list of tasks
    elif action == "clear":
        return tasks.clear() # clear function removes all items in a list
    else:
        return "Invalid Choice"
    
    # The user interface
while True: # This program will allow the program to run until user wants to exit
    action = input("\nWhat do you want to do: (add/remove/view/clear/exit): ").strip().lower()
    if action == "exit": # This will end the loop and program will stop
        print("Good Bye")
        break
    if action == "add" or action == "remove": # This will ask about item if user wants to add or remove items
        item = input("Enter the task Name: ").strip().lower()
        print(manage_tasks(action, item))
    elif action == "view": # Viewing items in a list doesn't require an item paramter so it is None
        print(manage_tasks(action, None))
    elif action == "clear": # Clearing items doesn't require an item paramter so it is None
        print(manage_tasks(action, None))
        print("All tasks are removed")
    else: 
        print("Invalid choice, please try again. ")
    


