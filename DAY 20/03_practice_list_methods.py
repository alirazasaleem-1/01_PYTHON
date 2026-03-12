# List Methods change the orginial List unlike strings 
# strings are immutable while the lists are mutable.
# String methods return new values while the orinal string remains unchanges while the list methods change the original list
l1 = [1,2,6, 78, 54, 23, 9]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(4)
print(l1)
l1.insert(0,3)
print(l1)
l1.remove(23)
print(l1)
# print(l1.pop(0)) 
a = l1.pop(0)
print(a)
print(l1)