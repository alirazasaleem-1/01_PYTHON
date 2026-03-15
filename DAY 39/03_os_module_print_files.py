# This prints all the files/folders inside a path
import os

folder = r"D:\03 BACKUP\Google Photos Backup"

files = os.listdir(folder)

for i, file in enumerate(files, 1):
    print(f"{i}: {file}")