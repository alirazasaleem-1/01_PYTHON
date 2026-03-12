"""
Function for showing tasks and creating / updating tasks.txt
"""
def show_tasks():
    with open("tasks.txt" , "a+") as f:
        tasks = f.readlines()
        print("--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i} : {task}")
# It will keep the program running until the user asks to exit
while True:
    choice = int(input("\n1 for view , 2 for add, 3 for exit").strip().lower())
    
    if choice == 1:
        try:
            show_tasks()
        except FileNotFoundError: # it will run if there is no task in tasks file
            print("No tasks yet.")
    elif choice == 2:
        task = input("Enter your task: ")
        with open("tasks.txt" , "a") as f:
            f.write(task)
        print("task added")

    elif choice == 3: # it will end the loop and ends the program
        print("keep up the good work")
        break