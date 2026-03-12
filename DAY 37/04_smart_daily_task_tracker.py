# Smart Daily Task Tracker
import datetime
import random

info = ("User: Ali Raza", "| Age = 18 |", "City: Faisalabad") # Tuple to stor user info
print(info)
date_time = datetime.datetime.now()
print(f"Current Date and Time: {date_time}")

motivation = [
    "We suffer more in Imagination than in Reality",
    "The Secret to Success is a secret, Work Hard and Find Out. ",
    "The more you know, the more you realize you don't know."
]

print(random.choice(motivation))

productivity = {
    "10 Pushups": 20,
    "Coding for 10 min": 30,
    "Namaz": 50
}


completed = set()
task_list = list(productivity.keys())

while True:
    for i,row in enumerate(productivity, 1):
        print(f"{i}: {row}")
    choice = input("Enter the task number you completed/ exit: ").strip().lower()
    if choice == "exit":
        break
    choice = int(choice)
    choice -= 1
    selected_task = task_list[choice]
    
    # Check if task is already in completed
    if selected_task in completed:
        print("This task is already in Completed Tasks. ")
    else:
        completed.add(selected_task)
    total_score = 0
    for task in completed:
        total_score += productivity[task]
    print(f"Completed Tasks: {completed}")
    print(f"Total Score: {total_score}")


