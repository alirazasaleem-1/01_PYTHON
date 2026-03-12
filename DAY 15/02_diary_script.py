with open("note", "w") as file:
    file.write("Today I learned File Handling in python\n----------------")

with open("note", "a") as file:
    file.write("\nI am becoming a better programmer everyday\n--------------------")

with open("note", "r") as file:
    content = file.read()
    print(content)