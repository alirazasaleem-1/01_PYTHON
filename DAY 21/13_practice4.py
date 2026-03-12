s = set()
s.add(20)
s.add(20.0)
s.add("20")

# question is what will be the length
# length will be 2 because in python when we check 20==20.0 it gives true
print(len(s))