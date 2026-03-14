import math

try:
    number = float(input("Enter a Number: "))
    sqroot = math.sqrt(number)
    round_up = math.ceil(number)
    round_down = math.floor(number)
    print(f"The Square root of the Number is: {sqroot}") 
    print(f"The Round up of the Number is: {round_up}")  
    print(f"The Round Down of the Number is: {round_down}")
except Exception as e:
    print(f"An error occured: {e}")  