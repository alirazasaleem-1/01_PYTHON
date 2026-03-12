with open("test.txt", "w") as file:
    file.write("Assalamu Alaikum!, This is my First File!")

with open("test.txt", "r") as file:
    content = file.read()
    print(content)