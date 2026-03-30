import json

tasks = []

while True: 
    task_name = input("Enter the name of the Task / exit: ")
    if task_name.lower().strip() == "exit":
        break

    task = {
        "task": task_name,
        "status": "Pending"
    }
    tasks.append(task)

# Save tasks json file
with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)
        print("Task saved Successfully. ✅")

# Read and display tasks
with open("tasks.json", 'r') as file:
     saved_tasks = json.load(file)

print("\nYour Tasks")
for t in saved_tasks:
     print(f"- {t['task']} {t['status']}")
     
