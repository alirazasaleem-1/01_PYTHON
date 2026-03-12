s = {1, 3, 5, "ali"}

print(s, type(s))
# sets are unordered
# sets are unindexed

s.add(5)
print(s)
print(len(s))
s.remove(5)
print(s)
print(s.pop()) # remove a random value and ruturn that value, not recommended
