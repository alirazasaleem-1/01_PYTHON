# 3 Methods to modify lists in loops
# 1st Method: list comprehension - the most safest way
numbers = [2, 3, 4, 5]
numbers = [x*2 for x in numbers] # create a new list instead of changing original one
print(numbers)

# 2nd Method: Loop over a Copy list (not original list)
tasks = ["Python", "Skills", "Namaz", "Social Media"]
for x in tasks[:]: # [:] creates a copy of the list
    if x == "Social Media":
        tasks.remove(x)
print(tasks)

# 3rd Method: Use enumerate for index access
to_dos = ["Python", "Coding", "Social Media"]
for index, to_do in enumerate(to_dos):
     to_dos[1] = "Coding (Completed ! ✅)"

print(to_dos)
