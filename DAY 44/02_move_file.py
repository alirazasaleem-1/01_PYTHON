# This program moves files
import shutil
import os

os.mkdir(r"D:\01_PYTHON\DAY 44\TestFolder01")

source = r"D:\01_PYTHON\TestFile1.txt" 
source2= r"D:\01_PYTHON\copy_TestFile1.txt"
destination = r"D:\01_PYTHON\DAY 44\TestFolder01"
shutil.move(source2, destination)
print("Folder Created and File Moved Successfully")