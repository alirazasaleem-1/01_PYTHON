marks = {
    "math": 35,
    "English": 70,
    "Science": 30
}

for subject, score in marks.items():
    if score < 40:
        marks[subject] = 40
        print(f"{subject}: Fixed to 40")
    else:
        print(f"{subject}: Pass")
