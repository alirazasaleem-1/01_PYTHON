name = "ali raza saleeM "
s = ("banana, cherry, apple")
fruits = [ "apple", "banana", "cherry"]
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip())
print(name.replace("saleeM", "Shah"))
print(s.split(","))
print(",".join(fruits))
print(name.find("saleeM"))
print(name.count("a"))
print(name.startswith('a'))
print(name.endswith("M"))

a = "Ali"
print(a.isalpha())
b = 123
print(b.is_integer())
c = "Ali123"
print(c.isalnum())

print(f"My name is {name}")