# This program moves a file
import shutil

source = r"D:\01_PYTHON\DAY 45\test.txt"
destination = r"D:\01_PYTHON\DAY 45\TestFolder\test.txt"

shutil.move(source , destination)
print("File Moved Successfully.")