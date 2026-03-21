# This program organizes files
import os
import shutil

path = r"D:\01_PYTHON\DAY 45"

folders = {
    "Text Files": ['.txt'],
    "Data Sheets": ['.csv']
}

for folder in folders:
    exact_folder = os.path.join(path, folder)
    if not os.path.exists(exact_folder):
        os.makedirs(exact_folder)
        print("Folders Created Successfylly. ")
    else:
        print("Folders Already Exists. ")
    
files = os.listdir(path)
for file in files:
        item_path = os.path.join(path, file)
        if os.path.isfile(item_path):
            name, extension = os.path.splitext(file)
            for folder, exts in folders.items():
                if extension.lower() in exts:
                    source = os.path.join(path, file)
                    destination = os.path.join(path, folder, file)
                    shutil.move(source, destination)
                    print("Files Organized Successfully. ")