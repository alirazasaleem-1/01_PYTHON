# Finally block is "no matter what" block.

try:
    file = open("tasks.txt", 'r')
    # Performs operatons
except FileNotFoundError:
    print("File Not Found. ")
finally:
    print("Closing Resources...")