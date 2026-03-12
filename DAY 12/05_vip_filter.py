guests = ["Ali", "Zainab", "Hamza", "Raza", "Abubakar"]

for name in guests:
    if len(name) > 4:
        print(f"You are invited, {name}!")
    else:
        print(f"{name}, Your name is too short for this party")