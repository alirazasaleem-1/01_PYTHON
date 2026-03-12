# using default parameter in function
# This function is returning multiple values
def status(name, age= 18):
    category = "Adult" if age>=18 else "Minor"
    return f"Name: {name}, Age: {age}", category

# keyword argument: calling funciton using name of paramter which enables us to ignore paramter order
res_str_1 , status_1 = status(age = 16, name = "Ali")
print(f"{res_str_1} | Status = {status_1}")

# Using positional arguments in which order of paratmers matters
res_str_2 , status_2 = status("Ali", 25)
print(f"{res_str_2} | Status : {status_2}")