import time

task = input("What task are you doing? ")
min = int(input("How many minutes will you focus? "))

print(f"Focus on {task} , Time is starting Now")

sec = min * 60

for i in range(5):
    print(f"Be focused on Your task Reminder {i+1}")
    time.sleep(sec)
    print(f"{i+1} Session Completed Champ! 🏆✅")
    i+=1
    

result = input("Did You Stay Focused? (yes/no): ")
with open(r"D:\01_PYTHON\DAY 55\focus_results.txt", 'w') as file:
    file.write(f"\n{time.gmtime}: {result}\n")
    print("Result saved in focus_results.txt")