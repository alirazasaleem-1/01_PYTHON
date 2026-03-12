# Sometimes python doesn't think of something as an error, but your business logic does, so you can
# manually raise errors

age = int(input("Enter Your age: "))

if age<0:
    raise ValueError("Age cannot be Negative Number. ")