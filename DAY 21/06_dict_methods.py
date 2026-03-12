marks = {
    "Ali": 100,
    "Yasir": 99,
    "Ammar": 99.9
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ali": 99, "Junaid": 40})
print(marks)
# print(marks.get("Ali2")) # prints None
# print(marks["Ali2"]) # returns an error 