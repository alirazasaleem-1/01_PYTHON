# a 2*3 matrix
matrix = [
    [1, 2, 3], # row 0
    [4, 5, 6] # row 1
]

# Access each element by matrix[row][column]
print(matrix[1][2]) 

# Loop in case of 2d lists
for row in matrix: # grabs the sublist 
    for element in row: # grabs the number 
        print(element)

# list comprehension: shorthand way to create a for loop that create a new list
# long way
my_list = []
for i in range (5):
    my_list.append(i*10)

# short way
my_list = [i * 10 for i in range(4)]