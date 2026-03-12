def safe_divide():
    try:
        n = int(input("Enter a Number to divide 100 by: "))
        d = 100 / n
        print(f"Successful! The result is {d}") 
    except ZeroDivisionError:
           print("Don't use zero, write a number greater than zero. ")
    except ValueError:
         print("Pllease Enter Digits Only. ")

safe_divide()