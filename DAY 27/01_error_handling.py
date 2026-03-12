try:
    # Code that might cause an error
    result = 10/0
except ZeroDivisionError:
    # Code that runs if error occur
    print("Oops! You can't divide by zero")