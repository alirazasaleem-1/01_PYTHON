# This program makes a folder
import os

folder = r"D:\01_PYTHON\DAY 45\TestFolder"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("Folder Created")
else:
    print("Folder Already Exists.")