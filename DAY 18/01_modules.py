# import function
import math
result = math.sqrt(9)
print(result)

# from keyword 
from math import sqrt
result = sqrt(9)
print(result)

# importing multiple functions of module
from math import sqrt, pi
result = sqrt(9)
print(result)
print(pi)

# as keyword
import math as m
result = m.sqrt(16)
print(result)

from math import sqrt as q
result = q(64)
print(result)

# dir function : used to check all the variables that we are importing
print(dir(math))



