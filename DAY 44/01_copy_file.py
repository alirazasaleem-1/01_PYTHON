# This program copies the file
import shutil

# Create file first
with open("TestFile1.txt", 'w') as f:
    f.write("Hello Ali ")

source = "TestFile1.txt"
destination = "copy_TestFile1.txt"

shutil.copy(source, destination)
print("Success! TestFile1.txt is is copies.")