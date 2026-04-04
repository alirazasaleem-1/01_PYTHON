import time

print("-"*128)
print("--- Welcome to Ali's Auto Reminder ⏰ --- ")
print("-"*128)

while True:
    task = input("You want to focus on which Task / (exit/quite): ").lower().strip()
    
    if task == "exit" or task == "quit":
        break
    min = int(input("How many Minutes do you want to focus? ").strip())
    sec = min * 60
    print(f"Focus on {task} Reminder")
    for second in range(sec, 0):
        print(f"{second} seconds left.")
        time.sleep(1)
    print("Session Completed. ✅ You can take break. ")
    print("You're building discipline.")
    print("Take 5 min break. ")