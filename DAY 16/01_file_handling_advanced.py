with open("students.txt", "a") as file:
    name = input("\nEnter Your Name: \t").lower()
    file.write(name + "\n")

with open("students.txt", "r") as file:
    for line in file:
        clean_name = line.strip()
        if clean_name.startswith("a"):
            print(f"Found: {clean_name}")