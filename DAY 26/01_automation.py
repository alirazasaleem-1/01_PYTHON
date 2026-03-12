import os
try:
    with open('tasks.txt' , "r") as file:
        lines = file.readlines()

    processed_data = [lines.strip() + "- Done ✅\n" for line in lines]

    with open('tasks.txt' , "w") as new_file:
        new_file.writelines(processed_data)

    print("Automation Successful! ✅ Report Generated 📁")
except FileNotFoundError:
    print("Oops! Try to create tasks.txt first.")