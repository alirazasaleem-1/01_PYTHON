# OS module allows python to talk to your operating System
import os

# Tells the location in which python is working
print(os.getcwd())

# tells the files inside the folder / location
files = os.listdir()
print(files)

# Creating a folder
os.mkdir("Test Folder") 

# Removing a folder
os.rmdir("Test Fodler") 

# change directory
os.chdir(r"D:\01_PYTHON\DAY 39")

# Remane file/ Folder
os.rename("old.txt", "new.txt")

