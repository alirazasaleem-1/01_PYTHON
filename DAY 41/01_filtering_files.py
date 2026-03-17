# This programs checks and prints the txt files present at a locaiton
import os

source_folder = r"D:\01_PYTHON\DAY 41"

files = os.listdir(source_folder)

for file in files:
    if file.endswith(".txt"):
        file_path = os.path.join(source_folder, file)
        print(f"{file} - PATH: {file_path}")