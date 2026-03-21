# This program lists files in a folder.
import os
path = r"D:\01_PYTHON"

# This stores the files in a variable as a list
files = os.listdir(path)

# This loop prints each file 
for file in files:
    print(f"I found this file: {file}")
