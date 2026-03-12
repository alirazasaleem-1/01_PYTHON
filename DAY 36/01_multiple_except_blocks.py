try:
    num = int(input("Enter a Number: "))
    result = 100 / num
except ValueError:
    print("Please enter a number. ")
except ZeroDivisionError:
    print("Please don't enter zero. ")
except Exception as e:
    print(f"An unexpected error occured: {e}")
