# A set is a collection of unique values
# They are unordered, no duplicates and mutable.

numbers = {1, 2, 3, 4, 5}
print(numbers)

# If there are duplicated, python automatically removes them
numbers = {1, 2, 3, 4, 4, 5, 5}
print(numbers)

# To create an empty set
empty_set = set()
print(type(empty_set))