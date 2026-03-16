# A Personal Diary

import datetime
def diary():
    while True:
        choice = input("\n1 for Adding\n2 for Reading\n3 for Exit\n")
        if choice == "1":
            with open("diary.txt", 'a') as f:
                content = input("Write Your Heart Out: ")
                f.write(f"{datetime.datetime.now()}  : {content}")
                print("Saved.")
        elif choice == "2":
            with open("diary.txt", 'r') as f:
                print(f"\n--- YOUR ENTRIES ---\n{f.read()}")
        elif choice == "3":
            break

diary()