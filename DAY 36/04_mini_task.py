# Ask user for a number and handle errors like a pro

def get_user_input():
    try:
        user_input = input("Please enter a Number:  ")
        number = int(user_input)
        print(f"Success! Your Number is {number}")
    except ValueError:
        print("Please enter digits only. ")
    finally: 
        print("Input Attempt Successful.")
    

get_user_input()
        
