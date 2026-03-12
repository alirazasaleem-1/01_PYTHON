matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("--- Matrix ---")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] = matrix[i][j] *2


for row in matrix:
    print(row)