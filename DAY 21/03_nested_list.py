# Task = create a 2 d list (matrix) and print each row nicely
matrix = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"]
]

print("----- Matrix -----")
for row in matrix:
    print(" ".join(row))
