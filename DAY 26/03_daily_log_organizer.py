# This program organize notes and save them to backup.txt and clear the notes
import os
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    with open('notes.txt' , "r" , encoding = "utf-8") as file:
        lines = file.readlines()

    with open('backup.txt' , "a" , encoding = "utf-8") as new_file:
        new_file.writelines(f"\n--- Saved on {now}\n")
        new_file.writelines(line for line in lines)

    with open('notes.txt' , "w"):
        pass

    print("Data Archived and Notes reset. ")
except FileNotFoundError:
    print("Oops! File no found.")