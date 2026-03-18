# This program create txt files

import os
folder_name = "TestFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created")
else:
    print("Folder already exists.")


os.chdir(folder_name)
for i in range(1,4):
    file_name = f"file {i}.txt"
    with open(file_name, 'w') as f:
        f.write(f"This is file {i}")
    print(f"{file_name} created.\n")

print("\nFiles inside Folder")
files = os.listdir()

for file in files:
    print(file)