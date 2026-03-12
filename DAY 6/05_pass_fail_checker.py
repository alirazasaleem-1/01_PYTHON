# the funtion to check if studnet is passed or failed

def exam_checker(score):
    if score > 50:
        return "Passed"
    else:
        return "Failed"
    

print(f"Student 1: {exam_checker(85)}")
print(f"Student 2: {exam_checker(42)}")
print(f"Student 2: {exam_checker(60)}")