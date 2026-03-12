# This program is practice of previous program
import os

try:
    with open('tasks.txt' , "r" , encoding="utf-8") as file:
        lines = file.readlines()

    processed_data = [line.strip() + "- Done ✅\n" for line in lines]

    with open('tasks.txt' , "w" , encoding="utf-8") as new_file:
        new_file.writelines(processed_data)

    print("Automation Successful! ✅ Report Generated 📁")
except FileNotFoundError:
    print("Oope! Try to create tasks.txt first. ")
